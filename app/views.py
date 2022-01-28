import os
import re
from django.shortcuts import render,redirect
from .forms import *
from dash.models import *
from .models import *
from django.contrib.auth import authenticate
from django.views.decorators.cache import never_cache
from django.contrib import messages

from twilio.rest import Client


def found(request):
    if 'user' in request.session:
        return True
    return False

# Create your views here.
@never_cache
def login(request):
    if 'user' in request.session:
        return redirect('/')

    form = loginform(request.POST or None)
    if request.method == 'POST':
        if form.is_valid():
            user=authenticate(username=request.POST['username'],password=request.POST['password'])
            if user is not None:
                request.session['user'] = username=request.POST['username']
                return redirect('home')
            else:
                form = loginform()
            return render(request,'login.html',{'form':form,'error':'Invalid'})

    return render(request,'login.html',{'form':form})
    

def signup(request):
    # print("lknsdkfjn")
    # if request.method == 'POST':
    #     form = CustomUserCreationForm(request.POST)
    #     print('k')
    #     print(form) 
    #     if form.is_valid():
    #         print('validdddddddddd')
    #         form.save()
    #         messages.success(request,"Account was created")
    #         return redirect('login')
    #     else:    
    #         form = CustomUserCreationForm()
    #         messages.success(request,"Please try again")
    #         return render(request,'signup.html',{'form':form})    
    # else:    
    #     form = CustomUserCreationForm()
    #     return render(request,'signup.html',{'form':form})

    # return render(request,'signup.html',{'form':form})

    form = CustomUserCreationForm(request.POST or None)
    if request.method == "POST":
        if form.is_valid():
            form.save()
            return redirect('/login')
    return render(request, 'signup.html', {'form': form})



def phone(request):
    # global num,username
    print('-----------------------')
    if request.method =='POST':
        phone = request.POST['number']
        print(phone)

        if CustomUser.objects.filter(number=phone).exists():
            user = CustomUser.objects.get(number=phone)
            # username = user.username    
            num = phone
            print('nummmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmm')

            try:
                account_sid = os.environ['TWILIO_ACCOUNT_SID'] = 'ACba338ac9b1f4db23a8a813312ec5a12b'
                auth_token = os.environ['TWILIO_AUTH_TOKEN'] = 'c413144c264d4ac353511706016ee443'
                client = Client(account_sid, auth_token)
                verification = client.verify \
                                .services('VAb6edc28e3758f37bef1650062e5b45fd') \
                                .verifications \
                                .create(to="+91"+num, channel='sms')
            except:
                return render(request, 'phone.html',{'err': "number doesn't exist"})
            return render(request, 'otp.html', {'userNum': num, 'url': '/otp'})
        print('nottttttttttttttttttttttttt')
    return render(request,'phone.html')

def otp(request):
    num = request.POST['number']
    otp = request.POST['otp']

    print(num, '///////////////////////////')

    account_sid = os.environ['TWILIO_ACCOUNT_SID'] = 'ACba338ac9b1f4db23a8a813312ec5a12b'
    auth_token = os.environ['TWILIO_AUTH_TOKEN'] = 'c413144c264d4ac353511706016ee443'
    client = Client(account_sid, auth_token)

    verification_check = client.verify \
                            .services('VAb6edc28e3758f37bef1650062e5b45fd') \
                            .verification_checks \
                            .create(to="+91"+num, code=otp)

    
    print( verification_check.status  ) 

    if verification_check.status == "approved":
        u = CustomUser.objects.get(number=num)
        name = u.username
        print(name)
        request.session['user'] = name
        return redirect('/')
    else:
        return render(request, 'otp.html', {'userNum': num, 'url': '/otp'})



    
    
#     return render(request,'phone.html')

# def send_otp(number):
#     global num
#     num = number
#     try:
#         account_sid = os.environ['TWILIO_ACCOUNT_SID'] = 'ACba338ac9b1f4db23a8a813312ec5a12b'
#         auth_token = os.environ['TWILIO_AUTH_TOKEN'] = 'c413144c264d4ac353511706016ee443'
#         client = Client(account_sid, auth_token)
#         verification = client.verify \
#                         .services('VAb6edc28e3758f37bef1650062e5b45fd') \
#                         .verifications \
#                         .create(to=num, channel='sms')
#         return True
#     except:
#         return False

# def verify_otp(otp):
#     account_sid = os.environ['TWILIO_ACCOUNT_SID'] = 'ACba338ac9b1f4db23a8a813312ec5a12b'
#     auth_token = os.environ['TWILIO_AUTH_TOKEN'] = 'c413144c264d4ac353511706016ee443'
#     client = Client(account_sid, auth_token)

#     verification_check = client.verify \
#                             .services('VAb6edc28e3758f37bef1650062e5b45fd') \
#                             .verification_checks \
#                             .create(to=num, code=otp)

    
#     return verification_check.status        

    

def home(request):
    # if 'user' in request.session:
    image = ads.objects.all()
    for i in image:
        print(i.homeimage)
    products = product.objects.all()
    
    u = found(request)
    return render(request,'home.html',{'products':products,'found': u,'image':image })

def men(request):
    id = request.GET.get('id')
    image = ads.objects.all()
    for i in image:
        print(i.homeimage)
    u = found(request)
    menproduct = product.objects.filter(category_id = 8)

    return render(request,'men.html',{'menproduct':menproduct,'found': u,'image':image})

def women(request):
    id = request.GET.get('id')
    image = ads.objects.all()
    for i in image:
        print(i.homeimage)
    u = found(request)
    womenproduct = product.objects.filter(category_id = 12)

    return render(request,'women.html',{'womenproduct':womenproduct,'found': u,'image':image})

def sports(request):
    id = request.GET.get('id')
    u = found(request)
    image = ads.objects.all()
    for i in image:
        print(i.homeimage)
    sportsproduct = product.objects.filter(category_id = 4)

    return render(request,'sports.html',{'sportsproduct':sportsproduct,'found': u,'image':image})


def productdetail(request):
    id = request.GET.get('id')
    products = product.objects.get(id=id)
    products.save()
    
    u = found(request)

    return render(request,'productdetail.html',{'products':products,'found': u})


# def cart(request):
#     id = request.GET.get('id')
#     p=product.objects.get(id=id)
#     print(p)
#     price = p.price
#     u = CustomUser.objects.get(username=request.session['user'])
#     cartproduct.objects.create(user=u, products=p, price=price)
    

#     return render(request,'cart.html',{'products':cartproduct.objects.all(), 'found': found})


# .............ADDING PRODUCT TO CART..............
# @never_cache
# def cart(request,pk):
#     if request.session.has_key('user'):
#         user = request.session['user']
#         newuser  = CustomUser.objects.get(username = user)
#         product_id = product.objects.get(pk=pk)
#         cartproduct(user = newuser,products = product_id,sub_total = product_id.discounted_price,
        
#                  quantity=1).save()
#         cart = cartproduct.objects.filter(user = newuser)

#         return redirect('cart')
#     else:
#         return redirect('productdetail')




def logout(request):
    del request.session['user']

    return redirect('/')    

# VAb6edc28e3758f37bef1650062e5b45fd
# ACba338ac9b1f4db23a8a813312ec5a12b Account cid
# c413144c264d4ac353511706016ee443 AUTH TOKEN

# def send_otp(number):
#     global num
#     num = number
#     try:
#         account_sid = os.environ['TWILIO_ACCOUNT_SID'] = 'AC3207c2b834a4fb5d151a073c8cd9d7ec'
#         auth_token = os.environ['TWILIO_AUTH_TOKEN'] = 'db3193b8d624c6bb7607e3e6d375fe8c'
#         client = Client(account_sid, auth_token)
#         verification = client.verify \
#                         .services('VA68685e82ab5c6aa20cf8cf3082bddce2') \
#                         .verifications \
#                         .create(to=num, channel='sms')
#         return True
#     except:
#         return False
# @never_cache

# def add_to_cart(request):
#     product = request.GET.get('prod_id')
#     print(product)
#     print("123456789012345678234567890")
#     return render(request,'cart.html')


def add_to_cart(request):
    user = request.user
    product_id = request.GET.get('prod_id')
    products = product.objects.get(id = product_id)
    cartproduct(user = user,products=products).save()
    
    return redirect('show_cart') 

def show_cart(request):
    if request.user.is_authenticated:
        user = request.user
        cart = cartproduct.objects.filter(user = user)
    return render(request,'cart.html',{'carts':cart})    