from django.contrib import admin
from django.urls import path,include
from userapp import views

urlpatterns = [
    
    path('',views.index,name='index'),
    path('login/',views.login,name='login'),
    path('signup/',views.signup,name='signup'),
    path('courses/',views.courses,name='courses'),
    path('profile/',views.profile,name='profile'),
    path('logout/',views.logout,name='logout'),

]
