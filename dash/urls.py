from django.urls import path
from . import views

urlpatterns = [
    path('',views.adminlogin,name='adminlogin'),
    path('adminhome',views.adminhome,name='adminhome'),
    path('adminuser',views.adminuser,name='adminuser'),
    path('block',views.block,name='block'),
    path('adminproduct',views.adminproduct,name='adminproduct'),
    path('adminaddproduct',views.adminaddproduct,name='adminaddproduct'),
    path('delete',views.delete,name='delete'),
    path('edite',views.edite,name='edite'),
    path('admincategory',views.admincategory,name='admincategory'),

    path('adminbrand',views.adminbrand,name='adminbrand'),
    path('adminaddbrand',views.adminaddbrand,name='adminaddbrand'),
    path('admindeletebrand',views.admindeletebrand,name='admindeletebrand'),
    path('admineditebrand',views.admineditebrand,name='admineditebrand'),
    
    path('adminaddcategory',views.adminaddcategory,name='adminaddcategory'),
    path('admindeletecategory',views.admindeletecategory,name='admindeletecategory'),
    path('admineditecategory',views.admineditecategory,name='admineditecategory'),
    path('adminads',views.adminads,name='adminads'),
    path('adminadsedite',views.adminadsedite,name='adminadsedite'),
    path('adminadsadd',views.adminadsadd,name='adminadsadd'),
    path('adminlogout',views.adminlogout,name='adminlogout'),
    path('adminorder',views.adminorder,name='adminorder'),
    path('editestatus/<int:id>',views.editestatus,name='editestatus'),
    path('productoffer',views.productoffer,name='productoffer'),
    path('categoryoffer',views.categoryoffer,name='categoryoffer'),
    path('categoryofferedite/<int:id>',views.categoryofferedite,name='categoryofferedite'),
    path('productofferedite/<int:id>',views.productofferedite,name='productofferedite'),

    path('coupon',views.coupon,name='coupon'),
    path('coupondelete',views.coupondelete,name='coupondelete'),
    path('addcoupon',views.addcoupon,name='addcoupon'),


    path('adminsails',views.adminsails,name='adminsails'),

    path('exportexcel',views.exportexcel,name='exportexcel'),
    # path('month',views.month,name='month'),
    path('year',views.year,name='year'),
    path('date',views.date,name='date'),





]
