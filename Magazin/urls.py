from django.urls import path
from . import views


urlpatterns=[
    path('',views.home,name='home'),  #links the home view to the root url
    path('products/',views.product_list,name='product_list'), 
    path('products/<int:product_id>/',views.product_detail,name='product_detail'), 
    path('cart/add/<int:product_id>/',views.addtocart,name='addtocart'),
    path('cart/',views.viewCart,name='viewCart'), 
    #path('checkout/',views.checkout,name='checkout'), 
    path('payment/create-checkout-session/', views.create_checkout_session, name='create_checkout_session'),
    path('payment/success/', views.payment_success, name='payment_success'),
    path('payment/cancel/', views.payment_cancel, name='payment_cancel'),
   
]