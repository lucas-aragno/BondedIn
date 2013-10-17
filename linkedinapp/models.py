from django.db import models
from django.contrib.auth.models import User


class UserProfile(models.Model):
    user = models.ForeignKey(User)
    oauth_token = models.CharField(max_length=200)
    oauth_secret = models.CharField(max_length=200)

class Country(models.Model):
    id = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=150)
    class Meta:
        db_table = u'Country'

class Province(models.Model):
    id = models.IntegerField(primary_key=True)
    id_country = models.ForeignKey(Country, null=True, db_column='id_country', blank=True)
    name = models.CharField(max_length=150)
    class Meta:
        db_table = u'Province'

class City(models.Model):
    id = models.IntegerField(primary_key=True)
    id_province = models.ForeignKey(Province, null=True, db_column='id_province', blank=True)
    name = models.CharField(max_length=150)
    class Meta:
        db_table = u'City'
