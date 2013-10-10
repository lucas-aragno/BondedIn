import oauth2 as oauth
import cgi
import simplejson as json
import datetime
import re
import urllib

# Django
from django.http import HttpResponse
from django.shortcuts import render_to_response
from django.http import HttpResponseRedirect
from django.conf import settings
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required

# Project
from linkedinapp.models import UserProfile

# from settings.py
consumer = oauth.Consumer(settings.LINKEDIN_TOKEN, settings.LINKEDIN_SECRET)
client = oauth.Client(consumer)

request_token_url = 'https://api.linkedin.com/uas/oauth/requestToken'
access_token_url = 'https://api.linkedin.com/uas/oauth/accessToken'
authenticate_url = 'https://www.linkedin.com/uas/oauth/authenticate'

def oauth_login(request):
    # Step 0. Get the current hostname and port for the callback
    if request.META['SERVER_PORT'] == 443:
    	current_server = "https://" + request.META['HTTP_HOST']
    else:
	current_server = "http://" + request.META['HTTP_HOST']
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
    print url
    return HttpResponseRedirect(url)

@login_required
def home(request):
    now = datetime.datetime.now()
    html = "<html><body>"
    token = oauth.Token(request.user.get_profile().oauth_token,request.user.get_profile().oauth_secret)
    client = oauth.Client(consumer,token)
    headers = {'x-li-format':'json'}
    url = "http://api.linkedin.com/v1/people/~:(id,first-name,last-name,headline)"
    resp, content = client.request(url, "GET", headers=headers)
    profile = json.loads(content)
    html += profile['firstName'] + " " + profile['lastName'] + "<br/>" + profile['headline']
    return HttpResponse(html)
   
@login_required
def people_search(request, client, token, headers, skill):
    url = "https://api.linkedin.com/v1/people-search:(people:(first-name,last-name,picture-url,positions:(company:(name))))?country-code=ar&keywords=" + skill
    result = client.request(url, "GET", headers=headers)
    return result

@login_required
def company_search(request, client, token, headers, name):
    url = "http://api.linkedin.com/v1/companies/universal-name=" + name + ":(name,locations)"
    result = client.request(url, "GET", headers=headers)
    return result

def format_name(name):
   name  = name.lower()
   return name.replace(" ","-")

def get_company_location(person, client, token, headers, request):
    # Se ignoran los person que no tienen positions o values
    if ('positions' not in person) or ('values' not in person['positions']) :
        return None
    company_name = person['positions']['values'][0]['company']['name']
    resp2,content = company_search(request, client, token, headers, format_name(company_name))
    company = json.loads(content)

    if 'locations' in company:
        for location in company['locations']['values']:
            if 'city' in location['address']:
                return location['address']['city']

    return None



def get_developers_by_location(location,profile,request,client,token,headers):
    locationList = location.split('-',1)
    developer_list = []
    #Se retorna None si no hay datos de people
    if 'people' not in profile:
        return None
    data = profile['people']
    #Se retorna None si no hay datos de values
    if 'values' not in data:
        return None
    people = data['values']
    for person in people:
        location = get_company_location(person, client, token, headers, request)
        if location != None:
            del person['positions']
            person['location'] = location
            developer_list.append(person)
    return developer_list

@login_required
def list(request, skill):
    now = datetime.datetime.now()
    html = "<html><body>"
    token = oauth.Token(request.user.get_profile().oauth_token,request.user.get_profile().oauth_secret)
    client = oauth.Client(consumer,token)
    headers = {'x-li-format':'json'}
    resp,content = people_search(request, client, token, headers, skill)
    profile = json.loads(content)
    people = get_developers_by_location('tandil',profile,request,client,token,headers)
    if people != None:
        html += json.dumps(people)

    return HttpResponse(html)

@login_required
def oauth_logout(request):
    # Log a user out using Django's logout function and redirect them
    # back to the homepage.
    logout(request)
    return HttpResponseRedirect('/')

def oauth_authenticated(request):
    # Step 1. Use the request token in the session to build a new client.
    token = oauth.Token(request.session['request_token']['oauth_token'],
        request.session['request_token']['oauth_token_secret'])
    if 'oauth_verifier' in request.GET:
        token.set_verifier(request.GET['oauth_verifier'])
    client = oauth.Client(consumer, token)

    # Step 2. Request the authorized access token from Provider.
    resp, content = client.request(access_token_url, "GET")
    if resp['status'] != '200':
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
