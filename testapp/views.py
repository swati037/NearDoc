from .models import Contact
from django.shortcuts import render
from django.http import HttpResponse

def contact(request):
    if request.method=="POST":
        name=request.POST['name']
        email=request.POST['email']
        phone=request.POST['phone']
        #content =request.POST['content']
        file = request.POST['file']
        contact=Contact(name=name, email=email, phone=phone, file=file)
        contact.save()
    return render(request, 'contact1.html')

# def contact1(request):
#     return render(request, 'index.html')

def finance(request):
    return render(request, 'finance.html')

def bloodbank(request):
    # name_site = request.POST['name_site']
    # site = request.POST['site']
    # phone_site = request.POST['phone_site']
    return render(request, 'bloodbank.html')
