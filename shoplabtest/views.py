from django.shortcuts import render,redirect, HttpResponse
import os,math,random,re
from django.contrib import messages
from login.models import log, logd
from shoplabtest.models import Product, Orders, OrderUpdate
import json,razorpay

# Create your views here.
def labtest(request):
    user=log.objects.all()
    products = Product.objects.all()
    #print(products)
    con = {'product' : products,'users' : user}
    return render(request, 'lab-test.html',con)

def tracker(request):
    user=log.objects.all()
    if request.method=="POST":
        orderId = request.POST.get('orderId')
        email = request.POST.get('email')
        print(orderId,email)
        try:
            order = Orders.objects.filter(order_id=orderId, email=email)
            if len(order)>0:
                update = OrderUpdate.objects.filter(order_id=orderId)
                updates = []
                for item in update:
                    updates.append({'text': item.update_desc, 'time': item.timestamp})
                    print(updates)
                    response = json.dumps(updates, default=str)
                return render(request, 'tracker.html',{'users' : user,'response':response,})
            else:
                return HttpResponse('{}')
        except Exception as e:
            return HttpResponse(e)
    return render(request, 'tracker.html',{'users' : user,})


def search(request):
    user=log.objects.all()
    return render(request, 'lab-test.html',{'users' : user,})

def productview(request, myid):
    user=log.objects.all()
    product=Product.objects.filter(product_id=myid)
    print(product)
    con =  {'product':product[0], 'users' : user,}
    return render(request, "productView.html", con)


def checkout(request):
    user=log.objects.all()
    if request.method=="POST":
        items_json= request.POST.get('itemsJson')
        name=request.POST.get('name')
        email=request.POST.get('email')
        address=request.POST.get('address')
        city=request.POST.get('city')
        state=request.POST.get('state')
        zip_code=request.POST.get('zip')
        phone=request.POST.get('phone')
        amount = request.POST.get('amount')
        order_currency = 'INR'
        client = razorpay.Client(auth=('rzp_test_og9ydZv8FXrqIe','8VFf0a28YI9QnvQ55rI6CfnA'))
        payment = client.order.create({'amount':amount,'currency':'INR', 'payment_capture':'1'})
        order = Orders(items_json= items_json, name=name, email=email, address= address, city=city, state=state, zip_code=zip_code, phone=phone, amount=amount)
        order.save()
        update= OrderUpdate(order_id= order.order_id, update_desc="The order has been placed")
        update.save()
        thank=True
        id=order.order_id
        return render(request, 'checkout.html', {'thank':thank, 'id':id, 'users' : user,})
    return render(request, 'checkout.html',{'users' : user,})


