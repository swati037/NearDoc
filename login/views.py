import doctest
from django.shortcuts import render,redirect
import os,math,random,re
from django.contrib import messages
from login.models import log, logd
from book_doctor.models import Doctor, VAppointment

# Create your views here.

def home(request):
    user=log.objects.all()
    return render(request, 'home.html',{'users' : user,})

def cont(request):
    return render(request, 'contact.html')

def land(request):
    return render(request, 'Land.html')

def loginPa(request):
    return render(request, 'index.html')

def loginDr(request):
    return render(request, 'indexDoc.html')

def logout(request):
    del request.session['email']
    return redirect("/")

def logoutDr(request):
    del request.session['name']
    return redirect("/")

def loginP(request):
    if request.method == "POST":
        email = request.POST.get('email')
        password = request.POST.get('password')
        user=log.objects.all()
        a = log.objects.filter(email=email,password=password).values('email','password')
        print(a)
        if a:
            user1=log.objects.get(email=email)
            request.session['email'] = user1.email
            return render(request, 'home.html', {'users' : user,})
        else:
            messages.error(request, 'Invalid Credentials!')
            return redirect("/loginPa")
    else:
        return redirect("/registration")

def registration(request):
    if request.method == "POST":
        name = request.POST.get('username')
        email = request.POST.get('email')
        password = request.POST.get('password')
        def ispresent(str):
            if str == None:
                return True
            regex = ("^(?=.*[a-z])(?=." +
            "*[A-Z])(?=.*\\d)" +
            "(?=.*[-+_!@#$%^&*., ?]).+$")
            p = re.compile(regex)
            if(re.search(p, str) and len(str) >= 8):
                return True
            else:
                return False
        a = log.objects.filter(email=email).values('email')
        if a:
            messages.error(request, 'This email already exists!')
            return render(request, 'index.html')
        elif (ispresent(password)):
            user = log(username=name, email=email, password=password)
            user.save()
            return redirect("/loginPa")
        else:
            messages.error(request, 'Password error!')
            return render(request, 'registration.html')
    return render(request, 'registration.html')
   

def loginD(request):
    if request.method == "POST":
        email = request.POST.get('email')
        password = request.POST.get('password')
        user=logd.objects.all()
        a = logd.objects.filter(email=email,password=password).values('email','password')
        print(a)
        if a:
            user1=logd.objects.get(email=email)
            name = user1.username
            user2 = Doctor.objects.get(name = name)
            request.session['name'] = user2.name
            
            appointment = VAppointment.objects.filter(doctor__name = name).order_by('date')
            
            user3 = Doctor.objects.filter(name = name)
            return render(request, 'homed.html', {'users' : user3, 'appointment' : appointment})
        else:
            messages.error(request, 'Invalid Credentials!')
            return redirect("/loginDr")
    else:
        return redirect("/registrationd")

def registrationD(request):
    if request.method == "POST":
        name = request.POST.get('username')
        email = request.POST.get('email')
        password = request.POST.get('password')
        def ispresent(str):
            if str == None:
                return True
            regex = ("^(?=.*[a-z])(?=." +
            "*[A-Z])(?=.*\\d)" +
            "(?=.*[-+_!@#$%^&*., ?]).+$")
            p = re.compile(regex)
            if(re.search(p, str) and len(str) >= 8):
                return True
            else:
                return False
        a = logd.objects.filter(email=email).values('email')
        if a:
            messages.error(request, 'This email already exists!')
            return render(request, 'indexDoc.html')
        elif (ispresent(password)):
            user1 = logd(username=name, email=email, password=password)
            user1.save()
            return redirect("/loginDr")
        else:
            messages.error(request, 'Password error!')
            return render(request, 'registrationD.html')
    return render(request, 'registrationD.html')
    