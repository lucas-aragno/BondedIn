import oauth2 as oauth
import cgi
import simplejson as json
import datetime
import time
import re
import urllib
import logging
import pickle


from cache.Company import *
from cache.Person import *
from cache.Location import *
from cache.MongoConnection import  *


# Django
from django.http import HttpResponse
from django.shortcuts import render_to_response
from django.http import HttpResponseRedirect
from django.conf import settings
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from linkedinapp.models import *

from django.contrib.auth.decorators import login_required
from django.core import serializers
from django.conf.urls.static import static
from pymongo import *
from cStringIO import StringIO


from cache.Company import Company



import sys, traceback

# Project
from linkedinapp.models import UserProfile

# from settings.py
consumer = oauth.Consumer(settings.LINKEDIN_TOKEN, settings.LINKEDIN_SECRET)
client = oauth.Client(consumer)

request_token_url = 'https://api.linkedin.com/uas/oauth/requestToken'
access_token_url = 'https://api.linkedin.com/uas/oauth/accessToken'
authenticate_url = 'https://www.linkedin.com/uas/oauth/authenticate'

def get_oauth_url(request):
    logger = logging.getLogger('BondedIn.linkedinapp')
    logger.debug("Called function get_oauth_url")
    # Step 0. Get the current hostname and port for the callback
    if request.META['SERVER_PORT'] == 443:
   	    current_server = "https://" + request.META['HTTP_HOST']
    else:
	    current_server = "http://" + request.META['HTTP_HOST']
    logger.debug("Current server: " + current_server)
    oauth_callback = current_server + "/login/authenticated"
    # Step 1. Get a request token from Provider.
    resp, content = client.request("%s?oauth_callback=%s" % (request_token_url,oauth_callback), "GET")
    if resp['status'] != '200':
        raise Exception("Invalid response from Provider.")

    # Step 2. Store the request token in a session for later use.
    request.session['request_token'] = dict(cgi.parse_qsl(content))

    # Step 3. Redirect the user to the authentication URL.
    url = "%s?oauth_token=%s" % (authenticate_url,
        request.session['request_token']['oauth_token'])
    logger.debug(url)
    return url

def mobile_login(request):
    logger = logging.getLogger('BondedIn.linkedinapp')
    logger.debug("Called function mobile_login")
    url = get_oauth_url(request)
    return HttpResponse(json.dumps(url))

def oauth_login(request):
    logger = logging.getLogger('BondedIn.linkedinapp.oauth_login')
    logger.debug("Called function oauth_login")
    url = get_oauth_url(request)
    return HttpResponseRedirect(url)

def test(request):
    logger = logging.getLogger('BondedIn.linkedinapp.test')
    logger.debug("Called function test")

    c=MongoConnection()
    print c.printConnection()
    
    
    company= Company()
    company.setId(1)
    company.setName("Devspark")
    company.setLogoUrl("www.devspark.com")
    
    #c.saveCompnay(company)

    company.setName("Intercomgi")
    c.save(company)

    


    html = "<html><body>"

    return HttpResponse(html)





def province_list(request, country):
    logger = logging.getLogger('BondedIn.linkedinapp')
    logger.error("Called function province_list")
    if country == '':
        country = 1
    headers = {'x-li-format':'json'}
    provinces = Province.objects.using('Geo').all().filter(id_country = country).order_by('name')
    html = serializers.serialize('json',provinces)
    #html += json.dumps(provinces)
    return HttpResponse(html)

def city_list(request, province):
    logger = logging.getLogger('BondedIn.linkedinapp')
    logger.debug("Called function city_list")
    if province == '':
        province = 2
    headers = {'x-li-format':'json'}
    cities = City.objects.using('Geo').all().filter(id_province = province).order_by('name')
    html = serializers.serialize('json', cities)
    return HttpResponse(html)


@login_required
def home(request):
    logger = logging.getLogger('BondedIn.linkedinapp')
    logger.debug("Called function home")
    now = datetime.datetime.now()
    token = oauth.Token(request.user.get_profile().oauth_token,request.user.get_profile().oauth_secret)
    client = oauth.Client(consumer,token)
    headers = {'x-li-format':'json'}
    url = "http://api.linkedin.com/v1/people/~:(id,first-name,last-name,headline)"
    resp, content = client.request(url, "GET", headers=headers)
    profile = json.loads(content)
    return render_to_response('index.html', {"firstName": profile['firstName'],"lastName": profile["lastName"],"headline": profile['headline']})

def people_search(request, client, token, headers, skill):
    logger = logging.getLogger('BondedIn.linkedinapp')
    logger.debug("Called function people_search")
    results = []
    i=0
    while i < 500:
        i += 25
        url = "https://api.linkedin.com/v1/people-search:(people:(public-profile-url,first-name,last-name,picture-url,positions:(company:(name))))?country-code=ar&keywords=" + skill + "&start=" + str(i) + "&count=25"
        resp,result = client.request(url, "GET", headers=headers)
        object_result = json.loads(result)
        if ('people' not in object_result) or ('values' not in object_result['people']):
            continue
        for people in object_result['people']['values']:
            results.append(people)
    return results
 
@login_required
def company_search(request, client, token, headers, name):
    logger = logging.getLogger('BondedIn.linkedinapp')
    logger.debug("Called function company_search")
    url = "http://api.linkedin.com/v1/companies/universal-name=" + name + ":(name,locations)"
    result = client.request(url, "GET", headers=headers)
    return result

def format_name(name):
   name  = name.lower()
   return name.replace(" ","-")

def get_company_location(person, locations, client, token, headers, request):
    logger = logging.getLogger('BondedIn.linkedinapp')
    logger.debug("Called function get_company_location con person: " + person['firstName'] + " " + person['lastName'])
    result = None
    # Se ignoran los person que no tienen positions o values
    if ('positions' not in person) or ('values' not in person['positions']) :
        logger.debug(person['firstName'] + " " + person['lastName'] + "Se ignora por no tener positions o values")
        return result
    company_name = person['positions']['values'][0]['company']['name']
    resp2,content = company_search(request, client, token, headers, format_name(company_name))
    #print resp2,content
    company = json.loads(content)

    # Si la company no tiene location retorno false
    if 'locations' not in company:
        logger.debug(company_name + " no tiene location retorno false")
        return result
    
    for location in company['locations']['values']:
        #print location
        # Si city no esta en location sigo con la prox location
        if 'city' not in location['address']:
            logger.debug("Si city no esta en location sigo con la prox location")
            continue
        # Si se especifica city y no es la que se encuentra en location sigo con la prox location
        if (locations != None):
            province = locations.keys()
            #print locations[province[0]]
            if not any(format_name(location['address']['city'].lower()) in s.lower() for s in locations[province[0]]):
                logger.debug("No city in locations[province[0]]")
                continue
            result = {"companyName":company_name, "location":location['address']['city']}
            break
        if location['address']['city'] in province_by_city:
            result = {"companyName":company_name, "location":location['address']['city']}
            break

    return result


def get_developers_by_location(locations,profile,request,client,token,headers):
    logger = logging.getLogger('BondedIn.linkedinapp')
    logger.debug("Called function get_developers_by_location")
    developer_list = []
    for person in profile:
        company_location = get_company_location(person, locations, client, token, headers, request)
        
        if company_location != None:
            del person['positions']
            person['company'] = company_location['companyName']
            person['city'] = company_location['location']
            person['province'] = province_by_city[company_location['location']]
            developer_list.append(person)
        else:
            logger.debug("company_location is None")

    return developer_list

province_by_city = {}
city_by_province = {}
@login_required
def list(request, skill, province_id=None, city_name=None):
    logger = logging.getLogger('BondedIn.linkedinapp')
    logger.debug("Called function list con skill: " + str(skill) + " province_id: " + str(province_id) + " city_name: " + str(city_name))
    now = datetime.datetime.now()
    token = oauth.Token(request.user.get_profile().oauth_token, request.user.get_profile().oauth_secret)
    client = oauth.Client(consumer,token)
    headers = {'x-li-format':'json'}
    content = people_search(request, client, token, headers, skill)

    html=''

    provinces = Province.objects.using('Geo').all()
    for province in provinces:
        cities = province.city_set.all()
        for city in cities:
            province_by_city[city.name] = province.name

    if province_id != None:
        province_name = format_name(Province.objects.using('Geo').get(id = province_id).name)
        if city_name != None:
            city_by_province = {province_name:[city_name]}
        else:
            cities = City.objects.using('Geo').all().filter(id_province = province_id)
            city_by_province = {province_name:cities.values_list('name', flat=True)}
    else:
        city_by_province = None

    people = get_developers_by_location(city_by_province, content, request, client, token, headers)
    if people != None:
        html = json.dumps(people)

    return HttpResponse(html, content_type="application/json")

@login_required
def oauth_logout(request):
    # Log a user out using Django's logout function and redirect them
    # back to the homepage.
    logout(request)
    return HttpResponseRedirect('/')

def oauth_authenticated(request):
    logger = logging.getLogger('BondedIn.linkedinapp')
    logger.debug("Called oauth_authenticated function")
    # Step 1. Use the request token in the session to build a new client.
    token = oauth.Token(request.session['request_token']['oauth_token'],
        request.session['request_token']['oauth_token_secret'])
    if 'oauth_verifier' in request.GET:
        token.set_verifier(request.GET['oauth_verifier'])
    client = oauth.Client(consumer, token)

    # Step 2. Request the authorized access token from Provider.
    resp, content = client.request(access_token_url, "GET")
    if resp['status'] != '200':
        logger.error('No pudo autenticar')
        print content
        raise Exception("Invalid response from Provider.")
    access_token = dict(cgi.parse_qsl(content))

    headers = {'x-li-format':'json'}
    url = "http://api.linkedin.com/v1/people/~:(id,first-name,last-name,industry)"
    token = oauth.Token(access_token['oauth_token'],
        access_token['oauth_token_secret'])
    client = oauth.Client(consumer,token)
    resp, content = client.request(url, "GET", headers=headers)
    profile = json.loads(content)
    
    # Step 3. Lookup the user or create them if they don't exist.
    firstname = profile['firstName']
    lastname = profile['lastName']
    identifier = profile['id']
    try:
        user = User.objects.get(username=identifier)
    except User.DoesNotExist:
        user = User.objects.create_user(identifier,
            '%s@linkedin.com' % identifier,
            access_token['oauth_token_secret'])
        
        user.first_name = firstname
        user.last_name = lastname
        user.save()
        # Save our permanent token and secret for later.
        userprofile = UserProfile()
        userprofile.user = user
        userprofile.oauth_token = access_token['oauth_token']
        userprofile.oauth_secret = access_token['oauth_token_secret']
        userprofile.save()

    # Authenticate the user and log them in using Django's pre-built 
    # functions for these things.
    user = authenticate(username=identifier,
        password=access_token['oauth_token_secret'])
    login(request, user)
    return HttpResponseRedirect('/')
