from django.contrib import admin
from django.urls import path 
from . import views
urlpatterns=[
    path('' , views.home , name='home'),
    path('about/', views.about , name='about'),
    path('contact/', views.contact , name='contact'),
    path('dashboard/', views.dashboard, name='dashboard'),
    path('logout/' , views.user_logout , name='logout'),
    path('login/' , views.user_login , name='login'),
    path('signup/' , views.signup , name='signup'),
    path('addpost', views.addpost , name='addpost'),
    path('editpost/<int:id>' ,views.editpost , name='editpost'),
    path('deletepost/<int:id>',views.deletepost , name='deletepost'),
]