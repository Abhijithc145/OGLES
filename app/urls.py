from django.urls import path
from  . import views

urlpatterns = [
    path('login',views.login,name='login'),
    path('signup',views.signup,name='signup'),
    path('phone',views.phone,name='phone'),
    path('',views.home,name='home'),
    path('men',views.men,name='men'),
    path('women',views.women,name='women'),
    path('sports',views.sports,name='sports'),
    path('productdetail',views.productdetail,name='productdetail'),
    path('add_to_cart',views.add_to_cart,name='add_to_cart'),
    path('show_cart',views.show_cart,name='show_cart'),
    path('logout',views.logout,name='logout'),
    # path('phone',views.phone,name='phone'),
    path('otp',views.otp,name='otp'),
    
]
