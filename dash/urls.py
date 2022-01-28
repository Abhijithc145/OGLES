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
    path('adminaddcategory',views.adminaddcategory,name='adminaddcategory'),
    path('admindeletecategory',views.admindeletecategory,name='admindeletecategory'),
    path('admineditecategory',views.admineditecategory,name='admineditecategory'),
    path('adminads',views.adminads,name='adminads'),
    path('adminadsedit',views.adminadsedite,name='adminadsedite'),
    # path('adminadsadd',views.adminadsadd,name='adminadsadd'),
  
]
