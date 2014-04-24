#Imports
from appdata.models import BloodGroupType
from appdata.models import City
from appdata.models import Details
from appdata.models import Facts
from appdata.models import FamousQuotes
from appdata.models import Medication
from appdata.models import NotDonate
from appdata.models import State
from django.contrib import auth
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.core.context_processors import csrf
from django.http import HttpResponse
from django.http import HttpResponseRedirect
from django.shortcuts import render_to_response
from forms import DetailsForm
from forms import UrgentForm
from helper import HelperFunctions

#Captcha API objects
import CaptchasDotNet
captchas = CaptchasDotNet.CaptchasDotNet (
                                client   = 'devanshug', 
                                secret   = '6HdMmG1EgKnJEOqHfQ5r9ywhkUbcM42UaeA0ffK1',
                                alphabet = 'abcdefghkmnopqrstuvwxyz0123456789',
                                letters  = 6,
                                width    = 240,
                                height   = 80
                                )
helperfunction = HelperFunctions()

#Data Updates
def dataUpdates(data):
    data['bloodgroupsCount'] = helperfunction.getCount()

#Views
def bloodgroupsystem(request):
    template = 'bloodgroupsystem.html'
    data = {}
    if request.user.is_authenticated():
        data['authenticated'] = request.user.is_authenticated()
        data['username'] = request.user.get_username()
    dataUpdates(data)
    return render_to_response(template, data)

def calculate(request):
    template = 'calculate.html'
    data = {}
    if request.user.is_authenticated():
        data['authenticated'] = request.user.is_authenticated()
        data['username'] = request.user.get_username()
    dataUpdates(data)
    return render_to_response(template, data)

def details(request):
    if not request.user.is_authenticated():
        return HttpResponseRedirect('/')
    template = 'details.html'
    data = {'bloodgroups':BloodGroupType.objects.all(),
            'states':State.objects.all(),
	    'cap_val':captchas.random(),
	    'cap_img':captchas.image(),
	    'cap_id':captchas.get_id(),
            }
    data['authenticated'] = request.user.is_authenticated()
    data['username'] = request.user.get_username()
    data.update(csrf(request))
    dataUpdates(data)
    return render_to_response(template, data)

def exists(request, username):
    if User.objects.filter(username=username).count():
        return HttpResponse('Username Exists')
    return HttpResponse('')

def facts(request):
    template = 'facts.html'
    data = {'facts':Facts.objects.all()}
    if request.user.is_authenticated():
        data['authenticated'] = request.user.is_authenticated()
        data['username'] = request.user.get_username()
    dataUpdates(data)
    return render_to_response(template, data)

def famousquotes(request):
    template = 'famousquotes.html'
    data = {'quotes':FamousQuotes.objects.all()}
    if request.user.is_authenticated():
        data['authenticated'] = request.user.is_authenticated()
        data['username'] = request.user.get_username()
    dataUpdates(data)
    return render_to_response(template, data)

def getData(request, state="Assam"):
    return render_to_response('data.html', {'cities':City.objects.filter(state_name=state)})

def index(request):
    if request.user.is_authenticated():
        return HttpResponseRedirect('/wall')
    template = 'index.html'
    data = {}
    dataUpdates(data)
    data.update(helperfunction.getBloodRequirements(username=None))
    return render_to_response(template, data)

def login(request):
    if request.user.is_authenticated():
        return HttpResponseRedirect('/')
    data = {}
    if request.method=='POST':
        username = request.POST.get('username', '')
        password = request.POST.get('password', '')
        user = auth.authenticate(username=username, password=password)
        if user is not None:
            auth.login(request, user)
            return HttpResponseRedirect('/wall')
        else:
            data['invalid'] = True
    template = 'login.html'
    data.update(csrf(request))
    dataUpdates(data)
    return render_to_response(template, data)

def logout(request):
    if not request.user.is_authenticated():
        return HttpResponseRedirect('/')
    auth.logout(request)
    return HttpResponseRedirect('/')

def qualified(request):
    template = 'qualification.html'
    data = {'no_donation':NotDonate.objects.all(),
            'medications':Medication.objects.all()}
    if request.user.is_authenticated():
        data['authenticated'] = request.user.is_authenticated()
        data['username'] = request.user.get_username()
    dataUpdates(data)
    return render_to_response(template, data)

def register(request):
    if request.user.is_authenticated():
        return HttpResponseRedirect('/')
    if request.method=='POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            form = DetailsForm(request.POST,request.FILES)
            form.save()
            username = request.POST.get('username', '')
            password = request.POST.get('password1', '')
            user = auth.authenticate(username=username, password=password)
            if user is not None:
                auth.login(request, user)
                return HttpResponseRedirect('/wall')
    args = {'bloodgroups':BloodGroupType.objects.all(),
            'states':State.objects.all(),
	    'cap_val':captchas.random(),
	    'cap_img':captchas.image(),
	    'cap_id':captchas.get_id()}
    args.update(csrf(request))
    dataUpdates(args)
    return render_to_response('register.html', args)

def urgent_blood(request):
    if not request.user.is_authenticated():
        return HttpResponseRedirect('/')
    template = 'urgent_blood.html'
    data = {'bloodgroups':BloodGroupType.objects.all(),
            'states':State.objects.all(),
	    'cap_val':captchas.random(),
	    'cap_img':captchas.image(),
	    'cap_id':captchas.get_id()}
    data['authenticated'] = request.user.is_authenticated()
    data['username'] = request.user.get_username()
    data.update(csrf(request))
    dataUpdates(data)
    return render_to_response(template, data)

def verify(request, code="123456"):
    if not captchas.verify(code): return HttpResponse('Incorrect Captcha!!!')
    return HttpResponse('Verified Human!!!')

def wall(request):
    if not request.user.is_authenticated():
        return HttpResponseRedirect('/')
    data = {}
    if request.method=='POST':
        form = UrgentForm(request.POST)
        if form.is_valid():
            form.save()
            data['saved'] = True
    template = 'wall.html'
    data['authenticated'] = request.user.is_authenticated()
    data['username'] = request.user.get_username()
    dataUpdates(data)
    data.update(helperfunction.getBloodRequirements(username=data['username']))
    return render_to_response(template, data)
