import os
from unicodedata import category
from django.shortcuts import render,redirect
from django.contrib.auth import authenticate
from app.forms import *
from app.models import *
from .form import *
from .models import *

from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.views.decorators.cache import never_cache

# Create your views here.


@never_cache
def adminlogin(request):
    if request.user.is_authenticated:
        return redirect('adminhome')
   
    

    form = loginform(request.POST or None)
    if request.method == 'POST':
        if form.is_valid():
            user=authenticate(username=request.POST['username'],password=request.POST['password'])
            if user is not None:
                if user.is_superuser:
                    login(request, user)
                    return redirect('adminhome')
                else:
                    return render(request,'adminlogin.html',{'form':form,'error':'Invalid'})

            else:
                form = loginform()
            return render(request,'adminlogin.html',{'form':form,'error':'Invalid'})
    return render(request,'adminlogin.html',{'form':form})


@login_required(login_url='/dash')
def adminhome(request):
    orders = order_place.objects.all()
    products  = product.objects.all()
    



    return render(request,'adminhome.html',{'orders':orders,'products':products})

@login_required(login_url='/dash')
def adminuser(request):
    user = CustomUser.objects.filter(is_superuser = False)
    return render(request,'adminuser.html',{'user':user})

@login_required(login_url='/dash/')
def block(request):
    id = request.GET.get('id')
    unblock =  CustomUser.objects.get(id=id) 
    unblock.is_active = not(unblock.is_active)
    unblock.save()
    return redirect('adminuser')


@login_required(login_url='/dash/')
def adminproduct(request):
    user = product.objects.all()

    return render(request,'adminproduct .html',{'user':user})


    
@login_required(login_url='/dash/')
def adminaddproduct(request):
    form = prodectdetai(request.POST or None )
    if request.method=='POST':
        form = prodectdetai(request.POST or None ,request.FILES)
        if form.is_valid():
            form.save()
            return redirect('adminproduct')
        else:
            print(form.errors)
     
            return render(request,'adminaddproduct.html',{'form':form}) 

    

    return render(request,'adminaddproduct.html',{'form':form})         

    


@login_required(login_url='/dash/')
def delete(request):
    id = request.GET.get('id')
    user = product.objects.filter(id=id)
    user.delete()


    return redirect('adminproduct')  

@login_required(login_url='/dash/')
def edite(request):
    
    id = request.GET.get('id')

    productid = product.objects.get(id=id)
    print(productid)
    form= prodectdetai(request.POST,request.FILES,instance=productid)
    
    if request.method=='POST':
        print("llllllllllllllllllllllllllll")
        form= prodectdetai(request.POST,request.FILES,instance=productid)
        # form = os.remove(your_image_field.path)
        if form.is_valid():
            form.save()
            return redirect('adminproduct')
        else:
            return render(request,'admineditproduct.html',{'form':form,'id':id,'productid':productid})
    else:
        form = prodectdetai(instance=productid)



    return render(request,'admineditproduct.html',{'form':form,'id':id,'productid':productid})

@login_required(login_url='/dash/')
def adminbrand(request):
    data = Brand.objects.all()

    return render(request,'adminbrand.html',{'data':data}) 


@login_required(login_url='/dash/')
def adminaddbrand(request):
    form = brandform(request.POST or None)
    if request.method=='POST':
        if form.is_valid():
            form.save()
            return redirect('adminbrand')
        else:
            print(form.errors)
            return render(request,'adminaddbrand.html',{'form':form})     

    return render(request,'adminaddbrand.html',{'form':form})   



@login_required(login_url='/dash/')
def admindeletebrand(request):
    id = request.GET.get('id')
    user = Brand.objects.filter(id=id)
    user.delete()
    return redirect('adminbrand') 

@login_required(login_url='/dash/')
def admineditebrand(request):
    id = request.GET.get('id')
    productid = Brand.objects.get(id=id)
    form = brandform(instance=productid)
    if request.method=='POST':
        form= brandform (request.POST,instance=productid)
        if form.is_valid():
            form.save()
            return redirect('adminbrand')
        else:
            return render(request,'admineditebrand.html',{'form':form ,'id':id})



    return render(request,'admineditebrand.html',{'form':form ,'id':id})    



@login_required(login_url='/dash/')
def admincategory(request):
    data = Category.objects.all()

    return render(request,'admincategory.html',{'data':data})        

@login_required(login_url='/dash/')
def adminaddcategory(request):
    form = categoryform(request.POST or None)
    if request.method=='POST':
        if form.is_valid():
            form.save()
            return redirect('admincategory')
        else:
            print(form.errors)
            return render(request,'adminaddcategory.html',{'form':form})     

    return render(request,'adminaddcategory.html',{'form':form})


@login_required(login_url='/dash/')
def admindeletecategory(request):
    id = request.GET.get('id')
    user = Category.objects.filter(id=id)
    user.delete()
    return redirect('admincategory')

@login_required(login_url='/dash/')
def adminads(request):
    image = ads.objects.all()
    for i in image:
        print(i.homeimage)
    

    return render(request,'adminads.html',{'image':image})     




@login_required(login_url='/dash/')
def admineditecategory(request):
    id = request.GET.get('id')
    productid = Category.objects.get(id=id)
    form = categoryform(instance=productid)
    if request.method=='POST':
        form= categoryform (request.POST,instance=productid)
        if form.is_valid():
            form.save()
            return redirect('admincategory')
        else:
            return render(request,'admineditecategory.html',{'form':form ,'id':id})



    return render(request,'admineditecategory.html',{'form':form ,'id':id})

@login_required(login_url='/dash/')
def adminadsedite(request):
    
    productid = ads.objects.get(id=5)
    
    
    if request.method=='POST':
        form= adslist(request.POST,request.FILES,instance=productid)
        
        if form.is_valid():
        
            form.save()
            print("Hello---------------------------")
            return redirect('adminads')
        else:
            print("eeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeee")
            return render(request,'adminadsedite.html',{'form':form}) 

    form = adslist(instance=productid)        
    

    return render(request,'adminadsedite.html',{'form':form,'id':id})  

@login_required(login_url='/dash/')
def adminadsadd(request):
    form = adslist(request.POST or None, request.FILES or None)
    if request.method=='POST':
        if form.is_valid():
            form.save()
            return redirect('adminads')
        else:
            
            return render(request,'adminadsadd.html',{'form':form})

    return render(request,'adminadsadd.html',{'form':form})  


@login_required(login_url='/dash/')
def adminlogout(request):
    logout(request)
    return redirect('adminlogin')


@login_required(login_url='/dash/')
def adminorder(request):
    order_datas = order_place.objects.all().order_by('-orderdate')

    return render(request,'adminorder.html',{'order_datas':order_datas})   


@login_required(login_url='/dash/')
def editestatus(request,id):
    if request.method=='POST':
        status = order_place.objects.get(id = id)
        value = request.POST['fff']
        order_place.objects.filter(id = id).update(status=value)
    return redirect('adminorder')   
     
@login_required(login_url='/dash/')
def productoffer(request):
    products = product.objects.all()

    return render(request,'productoffer.html',{'products':products})


@login_required(login_url='/dash/')
def categoryoffer(request):
    datas = Category.objects.all()
    

    return render(request,'category.html',{'datas':datas})    




@login_required(login_url='/dash/')
def categoryofferedite(request,id):
    if request.method == 'POST':
        value = request.POST['number']
        status = Category.objects.get(id = id)
        Category.objects.filter(id = id).update(status=value)

        
    return redirect('categoryoffer') 
