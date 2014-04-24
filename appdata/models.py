from django.db import models
from django.contrib.auth.models import User
from time import time

# Create your models here.
class State(models.Model):
    state_name = models.CharField(max_length=200,primary_key=True)

    def __unicode__(self):
        return self.state_name


class City(models.Model):
    city_name = models.CharField(max_length=200)
    state_name = models.ForeignKey(State)

    def __unicode__(self):
        return self.city_name

class BloodGroupType(models.Model):
    bloodtype = models.CharField(max_length=100, primary_key=True)
    
    def __unicode__(self):
        return self.bloodtype

class Facts(models.Model):
    fact_id = models.AutoField(primary_key=True)
    fact = models.CharField(max_length=500)

    def __unicode__(self):
        return self.fact

class NotDonate(models.Model):
    notdonate_id = models.AutoField(primary_key=True)
    notdonate = models.CharField(max_length=500)

    def __unicode__(self):
        return self.notdonate

class Medication(models.Model):
    medication_id = models.AutoField(primary_key=True)
    medication = models.CharField(max_length=500)
    waiting_time = models.CharField(max_length=500)

    def __unicode__(self):
        return self.medication

class FamousQuotes(models.Model):
    quote_id = models.AutoField(primary_key=True)
    quote = models.TextField()
    author = models.CharField(max_length=50)
    #CharField or TextField need not to be null, storage is empty string when null
    link = models.CharField(max_length=150,null=True)
    reference = models.CharField(max_length=150,null=True)

    def __unicode__(self):
        return self.quote

def getFilename(instance, filename):
    return "site_images/%s_%s" % (str(time()).replace('.','_'), filename)

class Details(models.Model):
    username = models.CharField(max_length=75, primary_key=True)
    email = models.EmailField(max_length=75)
    firstname = models.CharField(max_length=30)
    lastname = models.CharField(max_length=30)
    bloodgroup = models.CharField(max_length=20)
    gender = models.CharField(max_length=10)
    day = models.IntegerField()
    month = models.IntegerField()
    year = models.IntegerField()
    line1 = models.CharField(max_length=50,null=True)
    line2 = models.CharField(max_length=50,null=True)
    state = models.CharField(max_length=50)
    city = models.CharField(max_length=50)
    pin = models.IntegerField(null=True)
    line1perm = models.CharField(max_length=50,null=True)
    line2perm = models.CharField(max_length=50,null=True)
    stateperm = models.CharField(max_length=50,null=True)
    cityperm = models.CharField(max_length=50,null=True)
    pinperm = models.IntegerField(null=True)
    mobile = models.IntegerField()
    landline = models.IntegerField(null=True)
    pic = models.FileField(upload_to=getFilename,null=True)

class UrgentBlood(models.Model):
    username = models.CharField(max_length=75, primary_key=True)
    bloodgroup = models.CharField(max_length=20)
    name = models.CharField(max_length=40)
    mobile = models.IntegerField()
    location = models.CharField(max_length=40)
    state = models.CharField(max_length=40)
    city = models.CharField(max_length=40)
    message = models.CharField(max_length=200)
