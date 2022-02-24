
import os
from unittest import result
from django.contrib import messages
import re
from wsgiref.util import request_uri
from django.http import JsonResponse
from django.shortcuts import render,redirect
from .forms import *
from dash.models import *
from .models import *
from django.contrib.auth import authenticate
from django.views.decorators.cache import never_cache
from django.contrib import messages
from django.db.models import Q
from django.db.models import Sum

from twilio.rest import Client
import razorpay

from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required

client = razorpay.Client(auth=("rzp_test_xFSWIL714S4Ayy", "qpHgGRQLtFruIlax45rLXP0M"))


key ={'0':'paypal','1':'cash_on_delivery', '3': 'razorpay'}

def moveguest(request):
    
    guest = request.session.session_key
    if cartproduct.objects.filter(guest = guest).exists():
        guestvalue = cartproduct.objects.filter(guest = guest)
        users = CustomUser.objects.get(username = request.session["user"])
        for i in guestvalue:
            print("ggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggg")
             
            if cartproduct.objects.filter(products = i.products,user__username = request.session["user"]).exists():
                
                guests = cartproduct.objects.get(products = i.products,user__username = request.session["user"]) 
                print(guests)
                var =  i.quantity + guests.quantity
                guests.quantity = var
                guests.user = users
                guests.guest = ''
                guests.save()
                i.delete()
                
                

            else:
                # guests = cartproduct.objects.filter(products = i.products,user__username = request.session["user"]) 
                cartproduct.objects.filter(id=i.id).update(user = users,guest = "")


    


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
                request.session['user'] = request.POST['username']
                print(user)

                
                moveguest(request)
                return redirect('home')
            else:
                form = loginform()
            return render(request,'login.html',{'form':form,'error':'Invalid'})

    return render(request,'login.html',{'form':form})
    
@never_cache
def signup(request): 
  

    form = CustomUserCreationForm(request.POST or None)
    if request.method == "POST":
        if form.is_valid():
            num = request.POST.get("number")
            

            try:
                print("1234 ")
                account_sid = os.environ['TWILIO_ACCOUNT_SID'] = 'AC0cd89e6a2967043b31b326bf43c970e6'
                auth_token = os.environ['TWILIO_AUTH_TOKEN'] = 'a272df0f0165a7911100ea7d372940d0'
                client = Client(account_sid, auth_token)
                
                verification = client.verify \
                                .services('VAa2d5b75d4f3752b5f4cdb33425b40f65') \
                                .verifications \
                                .create(to="+91"+num, channel='sms')
                form.save()     
                return render(request, 'regotp.html', {'userNum': num, 'url': '/regotp','form': form})           
                                
            except:
                print("qwertyuio")
                messages.success(request,"Please try again")
                return render(request, 'signup.html',{'err': "number doesn't exist",'form': form})


        return render(request, 'signup.html',{'err': "number doesn't exist",'form': form})


        

            
        return render(request, 'signup.html', {'form': form})
                        
                        
    # 
    #     phone = request.127.0.0.1:8000POST['number']
    #     print(phone)
    #     
    #             try:
    #                     print("1234 ")
    #                     account_sid = os.environ['TWILIO_ACCOUNT_SID'] = 'AC0cd89e6a2967043b31b326bf43c970e6'
    #                     auth_token = os.environ['TWILIO_AUTH_TOKEN'] = 'a272df0f0165a7911100ea7d372940d0'
    #                     client = Client(account_sid, auth_token)
    #                     verification = client.verify \
    #                                     .services('VAa2d5b75d4f3752b5f4cdb33425b40f65') \
    #                                     .verifications \
    #                                     .create(to="+91"+phone, channel='sms')
                               

                # except:
                #         print("qwertyuio")
                #         return render(request, 'signup.html') 

                                               
                    
        
    return render(request, 'signup.html', {'form': form})



@never_cache
def regotp(request):

    num = request.POST['number']
    otp = request.POST['otp']

    print(num, '--------------------------')

    account_sid = os.environ['TWILIO_ACCOUNT_SID'] = 'AC0cd89e6a2967043b31b326bf43c970e6'
    auth_token = os.environ['TWILIO_AUTH_TOKEN'] = 'a272df0f0165a7911100ea7d372940d0'
    print("123456789")
    client = Client(account_sid, auth_token)

    verification_check = client.verify \
                            .services('VAa2d5b75d4f3752b5f4cdb33425b40f65') \
                            .verification_checks \
                            .create(to="+91"+num, code=otp)

    print("asdfghjktryuiocvbnmfghjkasdfghjklwertyuiopxcvhjnm")
    print( verification_check.status  ) 

    if verification_check.status == "approved":
        print("2134567890-54432134567890987654432314567")

        
        
        
        return redirect('login')
    else:
        print("]'/[;.]'/[;.'[;.['[;.[';'")
        messages.success(request,"Please try again")
        return render(request, 'regotp.html', {'userNum': num, 'url': '/regotp'})







# AC0cd89e6a2967043b31b326bf43c970e6
@never_cache
def phone(request):
    # global num,username
    print('-----------------------')
    if request.method =='POST':
        phone = request.POST['number']

        if CustomUser.objects.filter(number=phone).exists():
            user = CustomUser.objects.get(number=phone)
            # username = user.username    
            num = phone

            try:
                print("1234 ")
                account_sid = os.environ['TWILIO_ACCOUNT_SID'] = 'AC0cd89e6a2967043b31b326bf43c970e6'
                auth_token = os.environ['TWILIO_AUTH_TOKEN'] = 'a272df0f0165a7911100ea7d372940d0'
                client = Client(account_sid, auth_token)
                verification = client.verify \
                                .services('VAa2d5b75d4f3752b5f4cdb33425b40f65') \
                                .verifications \
                                .create(to="+91"+num, channel='sms')

            except:
                print("qwertyuio")
                messages.success(request,"Please try again")
                return render(request, 'phone.html',{'err': "number doesn't exist"})
            return render(request, 'otp.html', {'userNum': num, 'url': '/otp'})
        print('nottttttttttttttttttttttttt')
        messages.success(request,"Please try again")
    return render(request,'phone.html')
@never_cache
def otp(request):
    num = request.POST['number']
    otp = request.POST['otp']

    print(num, '///////////////////////////')

    account_sid = os.environ['TWILIO_ACCOUNT_SID'] = 'AC0cd89e6a2967043b31b326bf43c970e6'
    auth_token = os.environ['TWILIO_AUTH_TOKEN'] = 'a272df0f0165a7911100ea7d372940d0'
    client = Client(account_sid, auth_token)

    verification_check = client.verify \
                            .services('VAa2d5b75d4f3752b5f4cdb33425b40f65') \
                            .verification_checks \
                            .create(to="+91"+num, code=otp)

    
    print( verification_check.status  ) 

    if verification_check.status == "approved":
        u = CustomUser.objects.get(number=num)
        name = u.username
        print(name)
        request.session['user'] = name
        moveguest(request)
        
        return redirect('/')
    else:
        messages.success(request,"Please try again")
        return render(request, 'otp.html', {'userNum': num, 'url': '/otp'})

def resendotp(request):
    
    print(request.GET['num'])
    try:
        var =request.GET['num']
        print(var)
    
        account_sid = os.environ['TWILIO_ACCOUNT_SID'] = 'AC0cd89e6a2967043b31b326bf43c970e6'
        auth_token = os.environ['TWILIO_AUTH_TOKEN'] = 'a272df0f0165a7911100ea7d372940d0'
        client = Client(account_sid, auth_token)
        verification = client.verify \
                        .services('VAa2d5b75d4f3752b5f4cdb33425b40f65') \
                        .verifications \
                        .create(to="+91"+var, channel='sms')
    except:
        pass
    return JsonResponse({'status': True,})


    
    
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
    brand = Brand.objects.all()

    if request.session.has_key('user'):
        user = request.session['user']
        user1 =CustomUser.objects.get(username=user)
        cart = []
        cart_product = [p for p  in cartproduct.objects.all() if  p.user==user1]
        
        
        count = 0
        for i in cart_product:
            count = count+1
            cart.append(i.products.name)
        products = product.objects.all()
    
    
        u = found(request)
    

        return render(request,'home.html',{'products':products,'brand':brand, 'found': u,'carts':cart,'count':count}) 
    else:
        if not request.session.session_key:
            request.session.create()
        guestuser = request.session.session_key
        cart = []
        cart_product = [p for p  in cartproduct.objects.all() if  p.guest==guestuser]
        print("///////////////////////////////////")
        
        count = 0
        for i in cart_product:
            count = count+1
            cart.append(i.products.name)

        # if 'user' in request.session:
        
        products = product.objects.all()
        
        u = found(request)
    

        return render(request,'home.html',{'products':products,'found': u,'carts':cart,'brand':brand})

def men(request):
    id = request.GET.get('id')
    brand1 = [i.brand for i in  product.objects.filter(category_id = 1)]
    brand=list(set(brand1))
    menproduct = product.objects.filter(category_id = 1)
    if request.session.has_key('user'):
        user = request.session['user']
        user1 =CustomUser.objects.get(username=user)
        
        cart = []
        cart_product = [p for p  in cartproduct.objects.all() if  p.user==user1]
        
        count = 0
        for i in cart_product:
            count = count+1
            cart.append(i.products.name)

        print(",,,,,,,,,,,,,,")
        print(count)
        print(",,,,,,,,,,,,,,")
        cart_product = [p for p  in cartproduct.objects.all() if  p.user==user1]
        id = request.GET.get('id')
        image = ads.objects.all()
        for i in image:
          print(i.homeimage)
        u = found(request)
        menproduct = product.objects.filter(category_id = 1)

        return render(request,'men.html',{'menproduct':menproduct,'carts':cart,'brand':brand ,'found': u,'image':image,'count':count})
    else:
        if not request.session.session_key:
            request.session.create()
        guestuser = request.session.session_key
        brand1 = [i.brand for i in  product.objects.filter(category_id = 1)]
        brand=list(set(brand1))
        cart = []
        cart_product = [p for p  in cartproduct.objects.all() if  p.guest==guestuser]
        print("///////////////////////////////////")
        
        count = 0
        for i in cart_product:
            count = count+1
            cart.append(i.products.name)
   
   
       
        u = found(request)
   

        return render(request,'men.html',{'menproduct':menproduct,'found': u,'brand':brand, 'carts':cart})

def women(request):
    id = request.GET.get('id')
    brand1 = [i.brand for i in  product.objects.filter(category_id = 2)]
    brand=list(set(brand1))
    womenproduct = product.objects.filter(category_id = 2)
    if request.session.has_key('user'):
        user = request.session['user']
        user1 =CustomUser.objects.get(username=user)
        cart = cartproduct.objects.filter(user = user1)
        cart_product = [p for p  in cartproduct.objects.all() if  p.user==user1]
        cart = []
        count = 0
        for i in cart_product:
            count = count+1
            cart.append(i.products.name)

       
        id = request.GET.get('id')
        u = found(request)
        

        return render(request,'women.html',{'womenproduct':womenproduct,'brand':brand, 'found': u,'carts':cart,'count':count})
    
    else:
        if not request.session.session_key:
            request.session.create()
        guestuser = request.session.session_key
        cart = []
        cart_product = [p for p  in cartproduct.objects.all() if  p.guest==guestuser]
        print("///////////////////////////////////")
        brand1 = [i.brand for i in  product.objects.filter(category_id = 2)]
        brand=list(set(brand1))
        count = 0
        for i in cart_product:
            count = count+1
            cart.append(i.products.name)

    
        u = found(request)
   

        return render(request,'women.html',{'womenproduct':womenproduct,'brand':brand, 'carts':cart,'found': u})


    

def sports(request):
    
    id = request.GET.get('id')
    sportsproduct = product.objects.filter(category_id = 3)
    if request.session.has_key('user'):
        user = request.session['user']
        user1 =CustomUser.objects.get(username=user)
        cart = cartproduct.objects.filter(user = user1)
        cart_product = [p for p  in cartproduct.objects.all() if  p.user==user1]
        cart = []
        count = 0
        for i in cart_product:
            count = count+1
            cart.append(i.products.name)
        brand1 = [i.brand for i in  product.objects.filter(category_id = 3)]
        brand=list(set(brand1))

        
        id = request.GET.get('id')
        u = found(request)
        return render(request,'sports.html',{'sportsproduct':sportsproduct,'carts':cart,'brand':brand ,'found': u,'count':count})
    else:
        if not request.session.session_key:
            request.session.create()
        guestuser = request.session.session_key
        brand1 = [i.brand for i in  product.objects.filter(category_id = 3)]
        brand=list(set(brand1))
        cart = []
        cart_product = [p for p  in cartproduct.objects.all() if  p.guest==guestuser]
        
        count = 0
        for i in cart_product:
            count = count+1
            cart.append(i.products.name)
         
        
    
        u = found(request)
    
        return render(request,'sports.html',{'sportsproduct':sportsproduct,'brand':brand, 'carts':cart, 'found': u})        



    # return render(request,'sports.html',{'sportsproduct':sportsproduct,'found': u,'image':image,'count':count})


def productdetail(request):

    if request.session.has_key('user'):
        user = request.session['user']
        user1 =CustomUser.objects.get(username=user)
        cart = cartproduct.objects.filter(user = user1)
        cart_product = [p for p  in cartproduct.objects.all() if  p.user==user1]
        cart = []
        count = 0
        for i in cart_product:
            count = count+1
            cart.append(i.products.name)


        
        id = request.GET.get('id')
        products = product.objects.get(id=id)
        products.save()
    
        u = found(request)
        details  = [p for p  in user_details.objects.all() if  p.user==user1]

        # cart = False
        # cart = cartproduct.objects.filter(Q(products=products) 
        # &  Q(user=CustomUser.objects.get(username=request.session['user']))).exists()


        return render(request,'productdetail.html',{'products':products,'found': u,'carts':cart,'count':count})
    
    else:
        if not request.session.session_key:
            request.session.create()
        guestuser = request.session.session_key
        cart_product = [p for p  in cartproduct.objects.all() if  p.guest==guestuser]

        id = request.GET.get('id')
        products = product.objects.get(id=id)
        products.save()
            
        u = found(request)
        cart = []
        count = 0
        for i in cart_product:
            count = count+1
            cart.append(i.products.name)
   


        return render(request,'productdetail.html',{'products':products,'found': u,'cart':cart})



def brand(request):
    brand = Brand.objects.all()
    id = request.GET.get('id')
    newbrand = Brand.objects.filter(id = id)
    print(newbrand)
    u = found(request)
    prod = product.objects.filter(brand=id)

    if request.session.has_key('user'):
        user = request.session['user']
        user1 =CustomUser.objects.get(username=user)
        cart = []
        cart_product = [p for p  in cartproduct.objects.all() if  p.user==user1]
        count = 0
        for i in cart_product:
            count = count+1
            cart.append(i.products.name)
        return render(request,'brand.html',{'found': u,'brand':brand,'count':count, 'prod':prod})    
    
    
    return render(request,'brand.html',{'found': u,'brand':brand,'prod':prod})


def womenbrand(request):
    brand1 = [i.brand for i in  product.objects.filter(category_id = 2)]
    brand=list(set(brand1))
    id = request.GET.get('id')
    print(id)
    newbrand = Brand.objects.get(id = id)
    print(newbrand)
    u = found(request)
    prod = product.objects.filter(brand=newbrand)

    if request.session.has_key('user'):
        user = request.session['user']
        user1 =CustomUser.objects.get(username=user)
        cart = []
        cart_product = [p for p  in cartproduct.objects.all() if  p.user==user1]
        count = 0
        for i in cart_product:
            count = count+1
            cart.append(i.products.name)
        return render(request,'womwnbrand.html',{'found': u,'brand':brand,'count':count, 'prod':prod})    

    return render(request,'womwnbrand.html',{'found': u,'brand':brand,'prod':prod})


def menbrand(request):
    brand1 = [i.brand for i in  product.objects.filter(category_id = 1)]
    brand=list(set(brand1))
    id = request.GET.get('id')
    print(id)
    newbrand = Brand.objects.get(id = id)
    print(newbrand)
    u = found(request)
    prod = product.objects.filter(brand=newbrand)

    if request.session.has_key('user'):
        user = request.session['user']
        user1 =CustomUser.objects.get(username=user)
        cart = []
        cart_product = [p for p  in cartproduct.objects.all() if  p.user==user1]
        count = 0
        for i in cart_product:
            count = count+1
            cart.append(i.products.name)
        return render(request,'menbrand.html',{'found': u,'brand':brand,'count':count, 'prod':prod})    

    return render(request,'menbrand.html',{'found': u,'brand':brand,'prod':prod})    


def sportsbrand(request):
    brand1 = [i.brand for i in  product.objects.filter(category_id = 3)]
    brand=list(set(brand1))
    id = request.GET.get('id')
    print(id)
    newbrand = Brand.objects.get(id = id)
    print(newbrand)
    u = found(request)
    prod = product.objects.filter(brand=newbrand)

    if request.session.has_key('user'):
        user = request.session['user']
        user1 =CustomUser.objects.get(username=user)
        cart = []
        cart_product = [p for p  in cartproduct.objects.all() if  p.user==user1]
        count = 0
        for i in cart_product:
            count = count+1
            cart.append(i.products.name)
        return render(request,'sportsbrand.html',{'found': u,'brand':brand,'count':count, 'prod':prod})    

    return render(request,'sportsbrand.html',{'found': u,'brand':brand,'prod':prod})    




@never_cache
def logout(request):
    if request.session.has_key('user'):
        del request.session['user']
        messages.success(request,"Please try again")

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
#         verification = client.verify \cart_product = [p for p  in cartproduct.objects.all() if  p.user==user1]
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
    id = request.GET['id']
    products = product.objects.get(id = id)
    if request.session.has_key('user'):
        user = request.session['user']
        
        user1 = CustomUser.objects.get(username = user) 
        # product_id = request.GET.get('prod_id')
        
        
        cart_product = [p for p  in cartproduct.objects.all() if  p.user==user1]
        count = 0
        for i in cart_product:
            count = count+1
       
        cartproduct(user = user1,products=products).save()
        
       
    else:
        if not request.session.session_key:
            request.session.create()
        guestuser = request.session.session_key

        cartproduct(guest = guestuser,products=products).save()
        
    return JsonResponse({'f':0})      
    


def show_cart(request):
    u = found(request)

   
    

    if request.session.has_key('user'):
        tot=0
        user = request.session['user']
        user1 =CustomUser.objects.get(username=user)
        cart = cartproduct.objects.filter(user = user1)
        cart_product = [p for p  in cartproduct.objects.all() if  p.user==user1]
      
        count = 0
        for i in cart_product:
            count = count+1
      
        
        if cart_product:
            for p in cart_product:
            
                tot = (p.quantity * p.products.discount_price)+tot
                p.total=tot
                p.save()
                
        
        if cart_product:
            if tot > 500:
                alltotal = tot
                shipping = "Free"
            else:
                alltotal = tot+40
                shipping = 40    
            
        else:
            alltotal = tot
            shipping = 00

        
        

        


        return render(request,'cart.html',{'cart':cart,'found': u, 'total':tot, 'alltotal':alltotal,'shipping':shipping,'count':count})   
    else:

        if not request.session.session_key:
            request.session.create()
        guestuser = request.session.session_key

        cart = cartproduct.objects.filter(guest = guestuser)
        cart_product = [p for p  in cartproduct.objects.all() if  p.guest==guestuser]
        tot=0
        if cart_product:
            for p in cart_product:
            
                tot = (p.quantity * p.products.discount_price)+tot
                p.total=tot
                p.save()
                
        
        if cart_product:
            if tot > 500:
                alltotal = tot
                shipping = "Free"
            else:
                alltotal = tot+40
                shipping = 40    
            
        else:
            alltotal = tot
            shipping = 00


        return render(request,'cart.html',{'cart':cart,'found': u, 'total':tot, 'alltotal':alltotal,'shipping':shipping}) 








def remove_cart(request):
    id = request.GET.get('id')
    user = cartproduct.objects.filter(id=id)
    user.delete()
    return redirect('show_cart')

def pluscart(request):
    if request.method == 'GET':
        pid = int(request.GET.get('id'))
        cart = cartproduct.objects.get(id = pid)
        price = cart.products.discount_price
        print(price)
         
        if cart.products.stock-cart.quantity > 1:
           

            newQty = cart.quantity + 1
            newTotal = cart.total + price
            cart.total = newTotal
            cart.quantity = newQty
           
            cart.save()
            try:
                user = request.session['user']

                cartTotal = cartproduct.objects.filter(user = CustomUser.objects.get(username=user)).aggregate(Sum('total'))
                print(cartTotal)
           
            except:
                guest = request.session.session_key
                cartTotal = cartproduct.objects.filter(guest = guest).aggregate(Sum('total'))
                print(cartTotal)
           
            cartTotal = cartTotal['total__sum']
            print(cartTotal)
            
            return JsonResponse({'result': 'success', 'quantity':newQty, 'total':newTotal, 'cartTotal': cartTotal})
        else:

            return JsonResponse({'result':'fail'})    

def minuscart(request): 
    if request.method == 'GET': 
        pid = request.GET.get('id')
        cart = cartproduct.objects.get(id = pid)
        price = cart.products.discount_price
       
        
           
        if cart.quantity > 1   : 
                     
            newQty = cart.quantity - 1
            newTotal = cart.total - price  
            cart.total = newTotal
            cart.quantity = newQty
            
            cart.save()  
            try:
                user = request.session['user']
                cartTotal = cartproduct.objects.filter(user = CustomUser.objects.get(username=user)).aggregate(Sum('total'))
            # cartTotal = cartTotal.get('total__sum') 
            except:
                guest = request.session.session_key
                cartTotal = cartproduct.objects.filter(guest = guest).aggregate(Sum('total'))
           
            cartTotal = cartTotal['total__sum']
            return JsonResponse({'result': 'success', 'quantity':newQty, 'total':newTotal, 'cartTotal': cartTotal})
        else:
           
            return JsonResponse({'result':'fail'})

@never_cache
def checkout(request):
    u = found(request)
    if request.session.has_key('user'):
        user = request.session['user']
        user1 =CustomUser.objects.get(username=user)
        carts = cartproduct.objects.filter(user = user1)
        print("CHECKOUT ------------------------------")
        # details = user_details.objects.get(user=user1)
        details  = [p for p  in user_details.objects.all() if  p.user==user1]
        print(details)
        count = 0
        for i in carts:
            count = count+1
        
        
        cart_product = [p for p  in cartproduct.objects.all() if  p.user==user1]
        tot = 0
        if cart_product:
            for p in cart_product:

                tot = (p.quantity * p.products.discount_price)+tot
                p.total=tot
                
        request.session['checkoutamt'] = tot
                
                
        
        if cart_product:
            if tot > 500:
                alltotal = tot
                shipping = "Free"
            else:
                alltotal = tot+40
                shipping = 40    
            
        else:
            alltotal = tot
            shipping = 00
        

     

        DATA = {
                 "amount": alltotal * 100,
                 "currency": "INR",
                 "receipt": "receipt#1",
                 "notes": {
                "key1": "value3",
                "key2": "value2"
                      }
            }
        var = client.order.create(data=DATA)
        var1 = var["id"]
        
       


        print(alltotal)
        print("??????????????????????????????????????????????")
        return render(request,'checkout.html',{'found': u,'cart':cart_product,'alltotal':alltotal, 'total':tot,'count':count,'var1':var1, 'details':details})
        

    return render(request,'checkout.html',{'found': u}) 

def address(request):
    u = found(request)
    form = addressform(request.POST or None)
    if request.session.has_key('user'):
        user = request.session['user']
        user1 =CustomUser.objects.get(username=user)
        cart = cartproduct.objects.filter(user = user1)
        cart_product = [p for p  in cartproduct.objects.all() if  p.user==user1]
        
        
        count = 0
        for i in cart_product:
            count = count+1
        
        
    
        u = found(request)

        # productid = user_details.objects.get(username=user)
        # form = profileform(instance=productid)
        form = addressform(request.POST or None)
        if request.method=='POST':
            
                # return redirect('checkout')    
            form = addressform(request.POST or None)
            if form.is_valid():
                id = request.POST['id']
                location = request.POST['locality']
                city = request.POST['city']
                pincode = request.POST['pincode']
                state = request.POST['state']
                user_details(user=user1,locality=location,city=city,pincode=pincode,state=state).save()
                return redirect('checkout')
            else:
            
                return render(request,'address.html',{'form':form}) 

        return render(request,'address.html',{'found': u,'count':count,'form':form}) 

    return render(request,'address.html',{'found': u})       


def addressedite(request):
    u = found(request)
    id = int(request.GET.get('id'))
    print(id)
    userdetail = user_details.objects.get(id=id)
    form = addressform(request.POST or None,instance=userdetail)
    if request.session.has_key('user'):
        user = request.session['user']
        user1 =CustomUser.objects.get(username=user)
        cart = cartproduct.objects.filter(user = user1)
        cart_product = [p for p  in cartproduct.objects.all() if  p.user==user1]
        
        
        count = 0
        for i in cart_product:
            count = count+1
        u = found(request)
        print(userdetail)
        print("lllll")

        if request.method=='POST':
            if form.is_valid():
                form.save()
                return redirect('checkout')
            else:
                return render(request,'addressedite.html',{'form':form,'id':id,'userdetail':userdetail})
        else:
            return render(request,'addressedite.html',{'found': u,'count':count,'form':form,'id':id,})  

    return render(request,'addressedite.html',{'found': u})


@never_cache
def order(request):
    u = found(request)
    total=0
    coupen = request.GET.get('coupenId')
    print(coupen)

    if request.session.has_key('user'):
        user = request.session['user']
        user1 =CustomUser.objects.get(username=user)
    
        
        id = request.GET.get('custid')
        
       
        orderdat = order_place.objects.all()
       
        addres = user_details.objects.get(id=id)
        # stockless = product.objects.filter(id = i.id)
        i = cartproduct.objects.filter(user = user1)
        neworder=[]

        

        key ={'0':'paypal','1':'cash_on_delivery', '3': 'razorpay'}
        value = request.GET.get('paypalnum')
        print(value)
        

        for i in cartproduct.objects.filter(user = user1):
            prod = i.products
            id = request.GET.get('custid')
            addres = user_details.objects.get(id=id)
            qunt = i.quantity
            total += i.total
            stockless = product.objects.filter(id = i.id)
            orderdata = order_place()
            
    
            
            if coupen:
                print("rrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrr")
                c = Coupon.objects.get(id=coupen)
                total = total - (total * c.coupon_offer) / 100
                print(total)
                orderdata.coupons = c
                

            print(total)
            orderdata.user=user1
            orderdata.products=prod
            orderdata.address=addres
            orderdata.quantity=qunt
            orderdata.subtotal=total
    
            

            orderdata.paymentmode=key[value]
            

                

            orderdata.save()
            i.delete()
            p = i.products.stock
            c = i.products.stock - qunt
            print(c, '---------------------------------')
            stockless = product.objects.filter(stock = p).update(stock = c)
            print(p)
            neworder.append(orderdata)
            total = orderdata.subtotal

        if 'coupen_id' in request.session:
            del request.session['coupen_id']
         
         

        return render(request,'invoice.html',{'neworder':neworder,'found': u,'user':user1,'dat':id, 'addres':addres,'total':total})
        
    return redirect('/')




@never_cache
def invoice(request):
    u = found(request)
    if request.session.has_key('user'):
        user = request.session['user']
        user1 =CustomUser.objects.get(username=user)
        cart = order_place.objects.filter(user = user1)
        cart_product = [p for p  in cartproduct.objects.all() if  p.user==user1]
        count=0
        addres = user_details.objects.get(id=cart)
        tot = 0
        if cart_product:
            for p in cart_product:

                tot = (p.quantity * p.products.price)+tot
                p.total=tot
                
                
        
        if cart_product:
            if tot > 500:
                alltotal = tot
                shipping = "Free"
            else:
                alltotal = tot+40
                shipping = 40    
            
        else:
            alltotal = tot
            shipping = 00

        for i in cart_product:
            count = count+1
            print("-----------------------------")
            print(count)
            print("::::::::::::::::::::::;;;;;")

        return render(request,'invoice.html',{'cart':cart,'found': u,'addres':addres,'count':count,'alltotal':alltotal,'user':user1, 'total':tot})
    
    return render(request,'invoice.html')        

def search(request):
    # u = found(request)
    print("")
    if request.session.has_key('user'):
        user = request.session['user']
        user1 =CustomUser.objects.get(username=user)
        search = request.POST.get("Search")
        print(search)

        searchresult = product.objects.filter(name__startswith=search)
        return render(request,'search.html',{'search':searchresult})


    
    return render(request,'search.html')



def orderlist(request):
    u = found(request)
    if request.session.has_key('user'):
        user = request.session['user']
        user1 =CustomUser.objects.get(username=user)
        cart_product = [p for p  in cartproduct.objects.all() if  p.user==user1]
        count = 0
        for i in cart_product:
            count = count+1


        order = order_place.objects.filter(user = user1).order_by('-orderdate')    
        return render(request,'order.html',{'found': u,'count':count,'cart':order})



    return render(request,'order.html',{'found': u,'count':count})


def ordercancel(request,id):

    var = order_place.objects.get(id = id)
    var.status = "cancelled"
    order_place.objects.filter(id = id).update(status = var.status)
    orderquntity = var.quantity
    
    qunt = var.products.stock + orderquntity
    value = var.products
    product.objects.filter(id = value.id).update(stock = qunt)


    print(orderquntity)
    print("kkkkkkkkkkkkkkkkkkk")
    print(qunt)
    return redirect('orderlist')

def orderreturn(request,id):
    var = order_place.objects.get(id = id)
    var.status = "Return"
    order_place.objects.filter(id = id).update(status = var.status)
    return redirect('orderlist')
    


def pricesort(request):
    if request.method == 'POST':
        min =int(request.POST.get('minvalue'))
        max = int(request.POST.get('maxvalue'))
        value = product.objects.filter(discount_price__range=[min,max]).order_by('price')
    brand = Brand.objects.all()
    u = found(request)
   
    if request.session.has_key('user'):
        user = request.session['user']
        user1 =CustomUser.objects.get(username=user)
        
        cart_product = [p for p  in cartproduct.objects.all() if  p.user==user1]
        count = 0
        for i in cart_product:
            count = count+1
            
        return render(request,'brand.html',{'prod':value,'found': u,'count':count,'brand':brand}) 


    return render(request,'brand.html',{'prod':value,'found': u,'brand':brand})



def womenpricesort(request):
    if request.method == 'POST':
        min =int(request.POST.get('minvalue'))
        max = int(request.POST.get('maxvalue'))
        value = product.objects.filter(discount_price__range=[min,max],category_id = 2).order_by('price')

    brand1 = [i.brand for i in  product.objects.filter(category_id = 2)]
    brand=list(set(brand1))
    u = found(request)
   
    if request.session.has_key('user'):
        user = request.session['user']
        user1 =CustomUser.objects.get(username=user)
        
        cart_product = [p for p  in cartproduct.objects.all() if  p.user==user1]
        count = 0
        for i in cart_product:
            count = count+1
            
        return render(request,'womwnbrand.html',{'prod':value,'found': u,'count':count,'brand':brand}) 


    return render(request,'womwnbrand.html',{'prod':value,'found': u,'brand':brand})

def menpricesort(request):
    if request.method == 'POST':
        min =int(request.POST.get('minvalue'))
        max = int(request.POST.get('maxvalue'))
        value = product.objects.filter(discount_price__range=[min,max],category_id = 1).order_by('price')
    cart = []
    brand1 = [i.brand for i in  product.objects.filter(category_id = 1)]
    brand=list(set(brand1))
    u = found(request)
   
    if request.session.has_key('user'):
        user = request.session['user']
        user1 =CustomUser.objects.get(username=user)
        
        cart_product = [p for p  in cartproduct.objects.all() if  p.user==user1]
        count = 0
        for i in cart_product:
            count = count+1
            cart.append(i.products.name)
            
        return render(request,'menbrand.html',{'prod':value,'found': u,'count':count,'cart':cart, 'brand':brand}) 


    return render(request,'menbrand.html',{'prod':value,'found': u,'brand':brand})


def sportspricesort(request):
    if request.method == 'POST':
        min =int(request.POST.get('minvalue'))
        max = int(request.POST.get('maxvalue'))
        value = product.objects.filter(discount_price__range=[min,max],category_id = 3).order_by('price')

    brand1 = [i.brand for i in  product.objects.filter(category_id = 3)]
    brand=list(set(brand1))
    u = found(request)
    cart = []
    if request.session.has_key('user'):
        user = request.session['user']
        user1 =CustomUser.objects.get(username=user)
        
        cart_product = [p for p  in cartproduct.objects.all() if  p.user==user1]
        count = 0
        for i in cart_product:
            count = count+1
            cart.append(i.products.name)
            
        return render(request,'sportsbrand.html',{'prod':value,'cart':cart, 'found': u,'count':count,'brand':brand}) 


    return render(request,'sportsbrand.html',{'prod':value,'found': u,'brand':brand})






def profile(request):
    u = found(request)

    if request.session.has_key('user'):
        user = request.session['user']
        user1 =CustomUser.objects.get(username=user)
        cart_product = [p for p  in cartproduct.objects.all() if  p.user==user1]
        count = 0
        for i in cart_product:
            count = count+1 

        if user_details.objects.filter(user=user1).exists():
            person  =  user_details.objects.filter(user=user1)[0]
        else:
            person=None
        print(person)
        


    

        return render(request,'profile.html',{'found': u,'count':count,'user':person,'user1':user1}) 

    return render(request,'profile.html',{'found': u})     

def personaddressview(request):
    u = found(request)
    if request.session.has_key('user'):
        user = request.session['user']
        user1 =CustomUser.objects.get(username=user)
        cart_product = [p for p  in cartproduct.objects.all() if  p.user==user1]
        count = 0
        for i in cart_product:
            count = count+1 

        if user_details.objects.filter(user=user1).exists():
            person  =  user_details.objects.filter(user=user1)
        else:
            person=None
        

        return render(request,'personaddressview.html',{'found': u,'count':count,'person':person})

    return render(request,'personaddressview.html',{'found': u,'count':count})    

def personaddressadd(request):
    form = addressform(request.POST or None)
    u = found(request)
    if request.session.has_key('user'):
        user = request.session['user']
        user1 =CustomUser.objects.get(username=user)
        cart_product = [p for p  in cartproduct.objects.all() if  p.user==user1]
        count = 0
        for i in cart_product:
            count = count+1 


        form = addressform(request.POST or None)
        if request.method=='POST':
             
            form = addressform(request.POST or None)
            if form.is_valid():
                id = request.POST['id']
                location = request.POST['locality']
                city = request.POST['city']
                pincode = request.POST['pincode']
                state = request.POST['state']
                user_details(user=user1,locality=location,city=city,pincode=pincode,state=state).save()
                return redirect('personaddressview')    
    
        return render(request,'personaddressadd.html',{'found': u,'count':count,'form':form})
    return render(request,'personaddressadd.html',{'found': u,'count':count,'form':form})




@never_cache    
def buynow(request):
    
    u = found(request)
    if request.session.has_key('user'):

        user = request.session['user']
        user1 =CustomUser.objects.get(username=user)
        details  = [p for p  in user_details.objects.all() if  p.user==user1]
        cart_product = [p for p  in cartproduct.objects.all() if  p.user==user1]
        count = 0
        for i in cart_product:
             count = count+1

        prod_id = request.GET.get('id')   
        buynow = product.objects.get(id = prod_id)
        order =  buyproduct()
        order.id = 1
        order.products = buynow
        order.total=buynow.discount_price
        request.session['checkoutamt'] = order.total
        order.quantity = 1
        order.value = 0

        order.save()
        valu = buyproduct.objects.get(value = 0)
        print(valu.value)

        return redirect('showcheckout')
        
        
    #     return render(request,'checkout1.html',{'found': u,'buynow': order,'id':id,'valu':valu, 'count':count,'details':details})    

    # return render(request,'checkout1.html',{'found': u,'buynow':buynow, 'count':count,'details':details})    
@never_cache
def showcheckout(request):
    u = found(request)
    if request.session.has_key('user'):
        user = request.session['user']
        user1 =CustomUser.objects.get(username=user)
        details  = [p for p  in user_details.objects.all() if  p.user==user1]
        cart_product = [p for p  in cartproduct.objects.all() if  p.user==user1]
        count = 0
        for i in cart_product:
             count = count+1
        buynow = buyproduct.objects.get(id = 1)
        

        DATA = {
                 "amount": buynow.total * 100,
                 "currency": "INR",
                 "receipt": "receipt#1",
                 "notes": {
                "key1": "value3",
                "key2": "value2"
                      }
            }

        var = client.order.create(data=DATA)
        var1 = var["id"]




    return render(request,'checkout1.html',{'found': u,'buynow':buynow,'var1':var1,  'count':count,'details':details})





def address1(request):
    u = found(request)
    form = addressform(request.POST or None)
    if request.session.has_key('user'):
        user = request.session['user']
        user1 =CustomUser.objects.get(username=user)
        cart_product = [p for p  in cartproduct.objects.all() if  p.user==user1]
        count = 0
        for i in cart_product:
            count = count+1
        form = addressform(request.POST or None)
        if request.method=='POST':

            form = addressform(request.POST or None)
            if form.is_valid():
                id = request.POST['id']
                location = request.POST['locality']
                city = request.POST['city']
                pincode = request.POST['pincode']
                state = request.POST['state']
                user_details(user=user1,locality=location,city=city,pincode=pincode,state=state).save()
                return redirect('showcheckout')
            else:
            
                return render(request,'address1.html',{'form':form}) 
        





        return render(request,'address1.html',{'found': u,'count':count,'form':form}) 

    return render(request,'address1.html',{'found': u,'count':count,'form':form})     
        
@never_cache
def orderbuynow(request):
    u = found(request)
    value = request.GET.get('paypalnum')
    coupen = request.GET.get('coupenId')

    if request.session.has_key('user'):
        user = request.session['user']
        user1 =CustomUser.objects.get(username=user)
        id = request.GET.get('id')
        print("::::::::::::::::::::")
        print(id)
        prod_id = request.GET.get('custid')
        addres = user_details.objects.get(id=prod_id)
        print(addres)
        orderdat = order_place.objects.all()
        print(coupen)
        print("llllllllllllllllllllllll")
        if  buyproduct.objects.all():

            prod_details = buyproduct.objects.get()
            cart = buyproduct.objects.get()
            print(cart)
            total = prod_details.total
            orderdata = order_place()

            if coupen:
                c = Coupon.objects.get(id=coupen)
                total = total - (total * c.coupon_offer / 100)
                orderdata.coupons = c
                


            
            orderdata.user=user1
            orderdata.products=prod_details.products
            orderdata.address=addres
            orderdata.quantity=1
            orderdata.subtotal=prod_details.total
            orderdata.paymentmode=key[value]

            
            prod_details.value = 1
            prod_details.save()
            orderdata.save()
            
            if 'coupen_id' in request.session:
                 del request.session['coupen_id']
                 
            
            return render(request,'buynowinvoice.html',{'found': u,'cart':cart, 'user':user1,'dat':prod_id,'total':total, 'addres':addres,})        
        return redirect('orderlist')    



def addressedite1(request):
    u = found(request)
    id = int(request.GET.get('id'))
    print(id)
    userdetail = user_details.objects.get(id=id)
    form = addressform(request.POST or None,instance=userdetail)
    if request.session.has_key('user'):
        user = request.session['user']
        user1 =CustomUser.objects.get(username=user)
        cart = cartproduct.objects.filter(user = user1)
        cart_product = [p for p  in cartproduct.objects.all() if  p.user==user1]
        
        
        count = 0
        for i in cart_product:  
            count = count+1
        u = found(request)
        print(userdetail)
        print("lllll")

        if request.method=='POST':
            if form.is_valid():
                form.save()
                return redirect('showcheckout')
                
            else:
                return render(request,'addressedite1.html',{'form':form,'id':id,'userdetail':userdetail})
        else:
            return render(request,'addressedite1.html',{'found': u,'count':count,'form':form,'id':id,})  

    return render(request,'addressedite1.html',{'found': u})

        
def CheckCoupen(request):
    code = request.GET['code']
    print(code)
    if Coupon.objects.filter(coupon_id=code).exists():
        c = Coupon.objects.get(coupon_id=code)
        print(c)
        print(request.session['user'])
        if not order_place.objects.filter(coupons=c, user__username=request.session['user']).exists():
            print(request.session['checkoutamt'])
            amt = request.session['checkoutamt']
            print(amt)
            coupen = Coupon.objects.get(coupon_id=code)
            final = (amt) - (amt *  coupen.coupon_offer / 100)
            # request.session['finalamt'] = final
            # print(final)
            # request.session['coupen_id'] = coupen.id

            print(c.id, '------------------------------------------')

            return JsonResponse({'result': 'success','final_amt': final, 'coupen_id': c.id})
    return JsonResponse({'result': 'fail',})



# def CheckCoupen1(request):
#     code = request.GET['code']
#     print(code)
#     if Coupon.objects.filter(coupon_id=code).exists():
#         c = Coupon.objects.get(coupon_id=code)
#         print(c)
#         print(request.session['user'])
#         if not order_place.objects.filter(coupons=c, user__username=request.session['user']).exists():
#             print(request.session['checkoutamt'])
#             amt = request.session['checkoutamt']
#             print(amt)
#             coupen = Coupon.objects.get(coupon_id=code)
#             final = (amt) - (amt *  coupen.coupon_offer / 100)
#             request.session['finalamt'] = final
#             print(final)
#             request.session['coupen_id'] = coupen.id

#             return JsonResponse({'result': 'success','final_amt': final})
#     return JsonResponse({'result': 'fail',})



def Editeprofile(request):
    form = editeprofileform(request.POST or None)
    if request.session.has_key('user'):
        user = request.session['user']
        user1 =CustomUser.objects.get(username=user)
        if request.method=='POST':
            form= editeprofileform(request.POST,instance=user1)
            if form.is_valid():
                form.save()
            
            return redirect('profile')
            
        
        u = found(request)
        cart_product = [p for p  in cartproduct.objects.all() if  p.user==user1]
        
        
        count = 0
        for i in cart_product:  
            count = count+1

        form = editeprofileform(instance=user1) 

       
        return render(request,'Editeprodile.html', {'form': form,'found': u,'count':count})



def checkoutaddressdelete(request):
    id = request.GET.get('id')
    user = user_details.objects.filter(id=id)
    user.delete()

    return redirect('checkout')

def checkoutaddressdelete1(request):
    id = request.GET.get('id')
    user = user_details.objects.filter(id=id)
    user.delete()

    return redirect('showcheckout')    


def Deleteaccount(request):

    return redirect('profile')



