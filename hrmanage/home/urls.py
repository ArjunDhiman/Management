from os import name
from django.urls import path
from .import views 


urlpatterns = [
    path('',views.index),
    path('index',views.index,name='index'),
    path('signup',views.signup,name='signup'),
    path('signin',views.signin,name='signin'),
    path('userhome',views.index,name='userhome'),
    path('signuppage',views.signuppage,name='signuppage'),
     path('signinpage',views.signinpage,name='signinpage'),
    path('logout',views.logout,name='logout'),

    
 
]