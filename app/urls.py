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
    path('show_cart/',views.show_cart,name='show_cart'),
    path('logout',views.logout,name='logout'),
    # path('phone',views.phone,name='phone'),
    path('otp',views.otp,name='otp'),
    path('regotp',views.regotp,name='regotp'),
    path('remove_cart',views.remove_cart,name='remove_cart'),
    path('pluscart',views.pluscart,name='pluscart'),
    path('minuscart',views.minuscart,name='minuscart'),
    path('profile',views.profile,name='profile'),
    path('checkout',views.checkout,name='checkout'),
    path('address',views.address,name='address'),
    path('order',views.order,name='order'),
    path('buynow',views.buynow,name='buynow'),
   
    # path('invoice',views.invoice,name='invoice'),
    
    path('search',views.search,name='search'),

    path('ordercancel/<int:id>',views.ordercancel,name='ordercancel'),
    path('orderreturn/<int:id>',views.orderreturn,name='orderreturn'),

    path('address1',views.address1,name='address1'),
    # path('rayzerpay',views.rayzerpay,name='rayzerpay'),
    path('brand',views.brand,name='brand'),
    path('orderlist',views.orderlist,name='orderlist'),
    path('pricesort',views.pricesort,name='pricesort'),
    

    path('profile',views.profile,name='profile'),
    path('personaddressview',views.personaddressview,name='personaddressview'),
    path('personaddressadd',views.personaddressadd,name='personaddressadd'),


    path('orderbuynow',views.orderbuynow,name='orderbuynow'),

]
