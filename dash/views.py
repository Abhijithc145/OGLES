import datetime
import os
from unicodedata import category
from urllib import response
from django.http import HttpResponse
from django.shortcuts import render,redirect
from django.contrib.auth import authenticate
from app.forms import *
from app.models import *
from .form import *
from .models import *
import xlwt
from django.db.models import Sum

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

@never_cache
@login_required(login_url='/dash')
def adminhome(request):
    user = CustomUser.objects.filter(is_superuser = False)
    order_datas = order_place.objects.all().order_by('-orderdate')
    deliv = order_place.objects.filter(status = 'Delivered')
    de = order_place.objects.filter(status = 'Shipped')

    

    count= 0
    ord = 0
    ship =0
    sss =0
    for i in user:
        count += 1
    for i in de:
        sss += 1    
   
    for i in order_datas:
        ord += 1
    for i in deliv:
        ship += 1  
      
      
    orderplace = order_place.objects.filter(status='Placed').count()
    ordershiped = order_place.objects.filter(status='Shipped').count()
    orderdelivered = order_place.objects.filter(status='Delivered').count()


    ordercashondelivery = order_place.objects.filter(paymentmode='cash_on_delivery').count()
    orderpaypal = order_place.objects.filter(paymentmode='paypal').count()
    orderrazorpay = order_place.objects.filter(paymentmode='razorpay').count()




        # daily sales
    dialy_sales = order_place.objects.values('orderdate__day', 'orderdate__month', 'orderdate__year').filter(status="Delivered").annotate(Sum('subtotal')).order_by('-orderdate__date')[:7]

   
    monthly_sales = order_place.objects.values('orderdate__month').filter(status="Delivered").annotate(Sum('subtotal'))[:4]
    # products  = product.objects.all()

    print(dialy_sales)
    print(monthly_sales)
    


    return render(request,'adminhome.html', {'orderplace':orderplace,'dialy_sales':dialy_sales,'monthly_sales':monthly_sales, 'orderpaypal':orderpaypal,'orderrazorpay':orderrazorpay,'sss':sss, 'ordercashondelivery':ordercashondelivery, 'count':count,'ord':ord,'ship':ship, 'ordershiped':ordershiped,'orderdelivered':orderdelivered})



@never_cache
@login_required(login_url='/dash')
def adminuser(request):
    user = CustomUser.objects.filter(is_superuser = False)
    return render(request,'adminuser.html',{'user':user})


@never_cache
@login_required(login_url='/dash/')
def block(request):
    id = request.GET.get('id')
    unblock =  CustomUser.objects.get(id=id) 
    unblock.is_active = not(unblock.is_active)
    unblock.save()
    return redirect('adminuser')

@never_cache
@login_required(login_url='/dash/')
def adminproduct(request):
    user = product.objects.all()

    return render(request,'adminproduct .html',{'user':user})


@never_cache    
@login_required(login_url='/dash/')
def adminaddproduct(request):
    form = prodectdetai(request.POST or None )
    if request.method=='POST':
        form = prodectdetai(request.POST or None ,request.FILES)
        if form.is_valid():
            forms =form.save(commit=False)
            print(request.POST['category'])
            print(".................................................")
            catrgory = Category.objects.get(id = request.POST['category'])
            

            var = int(request.POST['price'])
            if catrgory.category_offer > 0:
                
                forms.discount_price = var - ((var*int(catrgory.category_offer))/100)
            else:
                forms.discount_price  = var 
            forms.save()     



            return redirect('adminproduct')
        else:
            print(form.errors)
     
            return render(request,'adminaddproduct.html',{'form':form}) 

    

    return render(request,'adminaddproduct.html',{'form':form})         

    

@never_cache
@login_required(login_url='/dash/')
def delete(request):
    id = request.GET.get('id')
    user = product.objects.filter(id=id)
    user.delete()


    return redirect('adminproduct')  

@never_cache
@login_required(login_url='/dash/')
def edite(request):
    
    id = request.GET.get('id')

    productid = product.objects.get(id=id)
    print(productid)
    form= prodectdetai(request.POST,request.FILES,instance=productid)
    
    if request.method=='POST':
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


@never_cache
@login_required(login_url='/dash/')
def adminbrand(request):
    data = Brand.objects.all()

    return render(request,'adminbrand.html',{'data':data}) 

@never_cache
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


@never_cache
@login_required(login_url='/dash/')
def admindeletebrand(request):
    id = request.GET.get('id')
    user = Brand.objects.filter(id=id)
    user.delete()
    return redirect('adminbrand') 


@never_cache
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


@never_cache
@login_required(login_url='/dash/')
def admincategory(request):
    data = Category.objects.all()

    return render(request,'admincategory.html',{'data':data})        



@never_cache
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



@never_cache
@login_required(login_url='/dash/')
def admindeletecategory(request):
    id = request.GET.get('id')
    user = Category.objects.filter(id=id)
    user.delete()
    return redirect('admincategory')


@never_cache
@login_required(login_url='/dash/')
def adminads(request):
    image = ads.objects.all()
    for i in image:
        print(i.homeimage)
    

    return render(request,'adminads.html',{'image':image})     


@never_cache

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


@never_cache
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



@never_cache

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


@never_cache
@login_required(login_url='/dash/')
def adminlogout(request):
    logout(request)
    return redirect('adminlogin')


@never_cache
@login_required(login_url='/dash/')
def adminorder(request):
    order_datas = order_place.objects.all().order_by('-orderdate')

    return render(request,'adminorder.html',{'order_datas':order_datas})   


@never_cache
@login_required(login_url='/dash/')
def editestatus(request,id):
    if request.method=='POST':
        status = order_place.objects.get(id = id)
        value = request.POST['fff']
        order_place.objects.filter(id = id).update(status=value)
    return redirect('adminorder')   
     
@never_cache
@login_required(login_url='/dash/')
def productoffer(request):
    products = product.objects.all()

    return render(request,'productoffer.html',{'products':products})

@never_cache
@login_required(login_url='/dash/')
def categoryoffer(request):
    datas = Category.objects.all()
   

    return render(request,'category.html',{'datas':datas})    



@never_cache
@login_required(login_url='/dash/')
def categoryofferedite(request,id):
    
    if request.method == 'POST':
        value = request.POST['number']
        data = Category.objects.get(id = id)
        Category.objects.filter(id = id).update(category_offer=value)
        prod = product.objects.filter(category = data) 
        for i in prod:
            if i.category.category_offer >= i.product_offer:
                i.discount_price = (i.price) - ((i.price)*(i.category.category_offer) /100)
            else:

                i.discount_price = (i.price) - ((i.price)*(i.product_offer) /100)
            i.save()

        return redirect('categoryoffer') 



@never_cache     
@login_required(login_url='/dash/')
def productofferedite(request,id): 
    if request.method == 'POST':
        print("zzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzz")
        value =int(request.POST['number'])
        
        product.objects.filter(id = id).update(product_offer=value)
        data = product.objects.get(id = id)
        if data.category.category_offer >= data.product_offer:
            data.discount_price = (data.price) - ((data.price)*(data.category.category_offer) /100)
        else:

            data.discount_price = (data.price) - ((data.price)*(data.product_offer) /100)
        data.save()
    
        return redirect('productoffer') 

@never_cache
@login_required(login_url='/dash/')
def coupon(request):
    data = Coupon.objects.all()
    form = couponform(request.POST or None)
    if request.method=='POST':  
        if form.is_valid():
            print("jjjjjjjjjjjjjjjjjjj")
            form.save()
            data = Coupon.objects.all() 
            return render(request,'coupon.html',{'data':data,'form':form})
    return render(request,'coupon.html',{'data':data,'form':form})



@never_cache
@login_required(login_url='/dash/')
def addcoupon(request):
    form = couponform(request.POST or None)
    
    return redirect('coupon')    

@never_cache
@login_required(login_url='/dash/')
def coupondelete(request):
    id = request.GET.get('id')
    user = Coupon.objects.filter(id=id)
    user.delete()
    return redirect('coupon')  



@never_cache
@login_required(login_url='/dash/')
def adminsails(request):
    order = order_place.objects.filter(status = 'Delivered')
    return render(request,'adminsails.html',{'order':order})


def exportexcel(request):
    response = HttpResponse(content_type='application/ms-excel')
    response['Content-Disposition'] = 'attachment;filename=SalesReport' +\
        str(datetime.datetime.now())+'.xls'
    wb = xlwt.Workbook(encoding='utf-8')
    print("aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa")
    ws = wb.add_sheet('SalesReport')
    row_num = 0
    font_style = xlwt.XFStyle()
    font_style.font.bold = True
    print("bbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbb")
    columns = ['Products', 'quantity', 'date', 'total']
    for col_num in range(len(columns)):
        ws.write(row_num, col_num, columns[col_num], font_style)
    font_style = xlwt.XFStyle()
    print("ccccccccccccccccccccccccccccccccccccccccc")
    rows = order_place.objects.filter(status = 'Delivered').values_list(
        'products', 'quantity', 'orderdate__date', 'subtotal')
    for row in rows:
        print("dddddddddddddddddddddddddddddddddddddddddddd")
        row_num += 1
        for col_num in range(len(row)):
            if col_num==0:
                print("eeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeee")
                pro=product.objects.get(id=row[col_num])
                ws.write(row_num, col_num, str(pro.name), font_style)
            else:
                print("ffffffffffffffffffffffffffffffffffffffffffffffffff")
                ws.write(row_num, col_num, str(row[col_num]), font_style)
    wb.save(response)
    return response


def date(request):


    return redirect('adminsails')


# def month(request):
#     if request.method == "POST":
#         month_report = request.POST['month']
#         if month_report!='':
#             monthr = month_report.split('-')
            
#             report = order_place.objects.filter(orderdate__month = str(monthr[1]),orderdate__year = str(monthr[0])).order_by('-orderdate')
#             print(report)
#         else:
#             report = order_place.objects.all().order_by('-orderdate')
#         return render(request, 'adminsails.html',{'order':report})
    

#     return redirect('adminsails')


def year(request):
    if request.method == "POST":
        year = int(request.POST['year'])
        if year!='':
            report =order_place.objects.filter(orderdate__year = year,status = 'Delivered').order_by('-orderdate')
        else:
            report = order_place.objects.all().order_by('-orderdate')


        return render(request, 'adminsails.html',{'order':report})
    
    return redirect('adminsails') 
