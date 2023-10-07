from django.shortcuts import render,redirect
from .models import register
from .models import Admin_Detail
from django.http import HttpResponse,HttpResponseRedirect
from django.template import loader
from django.urls import reverse
from django.contrib.auth import authenticate,login
from django.core.mail import send_mail
import math, random

def index(request):
    return render(request,"index.html")

def contact(request):
    return render(request,"contact.html")

def registers(request):
    return render(request,"registers.html")

def login(request):
    return render(request,"login.html")

'''def registers(request):
    mymember = register.objects.all().values()
    template = loader.get_template('register.html')
    context = {
        'mymember' : mymember
    }
    return HttpResponse(template.render(context, request))'''

def datainsert(request):
    a = request.POST['name']
    b = request.POST['email']
    c = request.POST['password']
    d = request.POST['gender']
    enter = register(firstname = a, email = b, password = c, gender = d)
    enter.save()
    return HttpResponseRedirect(reverse('login'))

def checkdata(request):
    if request.method == 'POST':
        email1 = request.POST['email']
        password1 = request.POST['password']
        
        try:
            user = register.objects.get(email=email1,password=password1) 
            if user.email == email1 and user.password == password1:
                return render(request,'index.html')
            else:
                return render(request, 'error.html')
        except:
            pass
    return render(request, 'error.html')


def admin_index(request):
    return render(request,"admin_index.html")


def admin_form(request):
    return render(request,"admin_form.html")

def admin_login(request):
    return render(request,"admin_login.html")

def add_data(request):
    a = request.POST['name']
    b = request.POST['email']
    c = request.POST['contact']
    d = request.POST['password']
    enter = Admin_Detail(name = a, email = b, contact = c, password = d)
    enter.save()
    return HttpResponseRedirect(reverse('admin_index'))


def admin_checkdata(request):
    if request.method == 'POST':
        email1 = request.POST['login']
        password1 = request.POST['password']     
        try:
            user = Admin_Detail.objects.get(email=email1,password=password1)    
            if user.email == email1 and user.password == password1:
                return render(request,'admin_index.html')
            else:
                return render(request, 'admin_error.html')
        except:
            pass
    return render(request, 'admin_error.html')

def admin_table(request):
    details = Admin_Detail.objects.all().values()
    template = loader.get_template('admin_table.html')
    context = {
        'details' : details
    }
    return HttpResponse(template.render(context, request))
    

def delete(request, id):
    member = Admin_Detail.objects.get(id=id)
    member.delete()
    return HttpResponseRedirect(reverse('admin_table'))

def update(request, id):
    mymember = Admin_Detail.objects.get(id=id)
    template = loader.get_template('admin_update.html')
    context = {
      'mymember': mymember,
    }
    return HttpResponse(template.render(context, request))

def updatedata(request, id):
    a = request.POST['nme']
    b = request.POST['eml']
    c = request.POST['cont']
    d = request.POST['pswd']
    member = Admin_Detail.objects.get(id=id)
    member.name = a
    member.email = b
    member.contact = c
    member.password = d
    member.save()
    return HttpResponseRedirect(reverse('admin_table'))

def user_data(request):
    data = register.objects.all().values()
    template = loader.get_template('user_data.html')
    context = {
        'data' : data
    }
    return HttpResponse(template.render(context, request))