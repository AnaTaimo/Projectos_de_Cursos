#from datetime import datetime
from pydoc import ModuleScanner
import string
from django.shortcuts import render
import datetime
from django.template import loader
from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse
from .models import Informationn



# Create your views here.
def index(request):
    now = datetime.datetime.now()
    dayy = now.day
    monthh = now.month
    yearr = now.year

    if len(str(dayy)) == 1:
        dayy = "0" + str(dayy)
    if len(str(monthh)) == 1:
        monthh = "0" + str(monthh)
    
    myInformationn = Informationn.objects.all().values().order_by("-id")
    template = loader.get_template('index.html')
    context = {
        'informatio' : myInformationn,
        'dayyy' : dayy,
        'monthhh': monthh,
        'yearrr': yearr
    }
    return HttpResponse(template.render(context, request))


def add(request):
    template = loader.get_template('add.html')
    return HttpResponse(template.render({}, request))

def addrecord(request):
    
    fname = request.POST['user']
    lname = request.POST['messag']
    fff = fname.lower()
    informat = Informationn(username=fff, messagee=lname)
    
    informat.save()
    return HttpResponseRedirect(reverse('index'))