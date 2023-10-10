from django.shortcuts import render
from django.template import loader
from django.http import JsonResponse,HttpResponse
from backend.models import Customers,Employees,Products,Bill
import re
import hashlib
# Create your views here.

#opendata=None

def index(request):
    template=loader.get_template('index.html')
    return HttpResponse(template.render())

def insert(request):
    return render(request,'insert.html')

# 判斷所選為何
def insertoption(request):
    #global opendata
    try:
        if request.method=='POST':
            getrequest=request.POST.get('database')
            if getrequest=='Customers':
                opendata='Customers'.lower()
            elif getrequest=='Employees':
                opendata='Employees'.lower()
            elif getrequest=='Products':
                opendata='Products'.lower()
            elif getrequest=='Bill':
                opendata='Bill'.lower()
            else:
                return render(request,'please_choose_insertoption.html')
            return render(request,f'insert_{opendata}.html')
    except Exception as e:
        print('insertoption_Error:',e)
        return HttpResponse('404')
        
def insertdata_customers_success(request):
    try:
        if request.method=='POST':
            a=request.POST
            
            first_name=a.get('first_name')
            last_name=a.get('last_name')
            account=a.get('account')
            born=a.get('born')
            sex=a.get('sex')
            country=a.get('country')
            city=a.get('city')
            address=a.get('address')
            if a.get('note')=='':
                note='None'
            else:
                note=a.get('note')
                
            # sha256加密
            password,true_password=match_password(a.get('password'))
            if not true_password:
                return render(request,'password_error.html')
            ascii_password=sha256_password(password)
            
            # 判斷電話號碼格式
            phone_number,true_phone_number=match_phone_number(a.get('phone_number'))
            if not true_phone_number:
                return render(request,'phone_number_error.html')
            # 判斷email格式
            email,true_mail=match_email(a.get('email'))
            if not true_mail:
                return render(request,'email_format_error.html')
            
            ins=Customers.objects.create(first_name=first_name,
                                       last_name=last_name,
                                       account=account,
                                       password=ascii_password,
                                       born=born,
                                       sex=sex,
                                       phone_number=phone_number,
                                       email=email,
                                       country=country,
                                       city=city,
                                       address=address,
                                       note=note,
                                       )
            ins.save()
            return render(request,'insertdata_customers_success.html',locals())

    except Exception as e:
        print('insertdata_customers_success_Error:',e)
        return HttpResponse('404')

def insertdata_customers_again(request):
    return render(request,'insert_customers.html')






################# not yet ###############

def test(request):
    return render(request,'test.html')

#########################################
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


#######this is function##########

def match_password(password):
    password=password
    true_password=re.findall('.{8,20}',password)
    return password,true_password

def sha256_password(password):
    password=password
    password_bytes=password.encode('utf-8')
    ascii_password=hashlib.sha256(password_bytes).hexdigest()
    return ascii_password

def match_phone_number(phone_number):
    phone_number=phone_number
    true_phone_number=re.findall('(09[^_%\.-][\d]{7})|(02[^_%\.-][\d]{7})|(0[^_%\.-][\d]{7})',phone_number)
    return phone_number,true_phone_number

def match_email(email):
    email=email
    true_mail=re.findall('^[A-Za-z0-9\._%-]*@?[A-Za-z0-9\.]+$',email)
    return email,true_mail

def restful_c(state):
    pass














