from django.shortcuts import render
from django.template import loader
from django.http import HttpResponse
# Create your views here.
#from rest_framework.response import Response

mydict={}

def index(request):
    template=loader.get_template('index.html')
    return HttpResponse(template.render())

def insert(request):
    return render(request,'insert.html',mydict)

def insertdata(request):
    global mydict
    a=request.GET
    key=a.get('key')
    val=a.get('val')
    if key in mydict.keys():
        return render(request,'file_exist.html')
    mydict[key]=val
    return render(request,'insertdata.html',locals())

def select(request):
    if len(mydict)==0:
        return render(request,'no_file_error.html')
    return render(request,'select.html')
    
def selectdevid(request):
    a=request.GET
    key=a.get('key')
    if key=='all':
        return selectall(request)
    return selectone(request)
    
def selectone(request):
    global mydict
    a=request.GET
    key=a.get('key')
    if key not in mydict.keys():
        return render(request,'not_found_error.html')
    val=mydict[key]
    return render(request,'selectone.html',locals())

def selectall(request):
    global mydict
    return render(request,'selectall.html', {'mydict': mydict})

def update(request):
    if len(mydict)==0:
        return render(request,'no_file_error.html')
    return render(request,'update.html')
    
def updatedata(request):
    global mydict
    a=request.GET
    key=a.get('key')
    if key not in mydict.keys():
        return render(request,'not_found_error.html')
    val=a.get('val')
    mydict[key]=val
    return render(request,'updatedata.html',locals())

def delete(request):
    if len(mydict)==0:
        return render(request,'no_file_error.html')
    return render(request,'delete.html')

def deletedevid(request):
    a=request.GET
    key=a.get('key')
    if key=='all':
        return deleteall(request)
    return deleteone(request)

def deleteone(request):
    global mydict
    a=request.GET
    key=a.get('key')
    if key not in mydict.keys():
        return render(request,'not_found_error.html')
    val=mydict[key]
    del mydict[key]
    return render(request,'deleteone.html',locals())
    
def deleteall(request):
    global mydict
    mydict={}
    return render(request,'deleteall.html', locals())






















