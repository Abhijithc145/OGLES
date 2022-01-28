import os
from django.shortcuts import render,redirect
from django.contrib.auth import authenticate
from app.forms import *
from app.models import *
from .form import *
from .models import *

# Create your views here.
def adminlogin(request):

    form = loginform(request.POST or None)
    if request.method == 'POST':
        if form.is_valid():
            user=authenticate(username=request.POST['username'],password=request.POST['password'])
            if user is not None:
                if user.is_superuser:

                    return render(request,'adminhome.html')
                else:
                    return render(request,'adminlogin.html',{'form':form,'error':'Invalid'})

            else:
                form = loginform()
            return render(request,'adminlogin.html',{'form':form,'error':'Invalid'})
    return render(request,'adminlogin.html',{'form':form})

def adminhome(request):
    return render(request,'adminhome.html')


def adminuser(request):
    user = CustomUser.objects.filter(is_superuser = False)
    return render(request,'adminuser.html',{'user':user})


def block(request):
    id = request.GET.get('id')
    unblock =  CustomUser.objects.get(id=id) 
    unblock.is_active = not(unblock.is_active)
    unblock.save()
    return redirect('adminuser')



def adminproduct(request):
    user = product.objects.all()

    return render(request,'adminproduct .html',{'user':user})


    

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

def delete(request):
    id = request.GET.get('id')
    user = product.objects.filter(id=id)
    user.delete()


    return redirect('adminproduct')    

def edite(request):
    id = request.GET.get('id')
    productid = product.objects.get(id=id)

    form = prodectdetai(instance=productid)

    if request.method=='POST':
        form= prodectdetai(request.POST,request.FILES,instance=productid)
        # form = os.remove(your_image_field.path)
        if form.is_valid():
            form.save()
            return redirect('adminproduct')
        else:
            return render(request,'adminedite.html',{'form':form,'id':id})


    return render(request,'adminedite.html',{'form':form,'id':id})


def admincategory(request):
    data = Category.objects.all()

    return render(request,'admincategory.html',{'data':data})    


def adminaddcategory(request):
    form = categoryform(request.POST or None ,request.FLLES)
    if request.method=='POST':
        if form.is_valid():
            form.save()
            return redirect('admincategory')
        else:
            print(form.errors)
            return render(request,'adminaddproduct.html',{'form':form})     

    return render(request,'adminaddcategory.html',{'form':form})

def admindeletecategory(request):
    id = request.GET.get('id')
    user = Category.objects.filter(id=id)
    user.delete()
    return redirect('admincategory')


def adminads(request):
    image = ads.objects.all()
    for i in image:
        print(i.homeimage)
    

    return render(request,'adminads.html',{'image':image})     





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

def adminadsedite(request):
    
    productid = ads.objects.get(id=5)
    form = adslist(instance=productid)
    
    if request.method=='POST':
        form= adslist(request.POST)
        
        if form.is_valid():
            form.save()
            print("Hello---------------------------")
            return redirect('adminads')
        else:
            return render(request,'adminadsedite.html',{'form':form}) 
    

    return render(request,'adminadsedite.html',{'form':form,'id':id})  

# def adminadsadd(request):
#     form = adslist(request.POST or None, request.FILES or None)
#     if request.method=='POST':
#         if form.is_valid():
#             form.save()
#             return redirect('adminads')
#         else:
            
#             return render(request,'adminadsadd.html',{'form':form})

#     return render(request,'adminadsadd.html',{'form':form})      