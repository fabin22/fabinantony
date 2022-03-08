from django.contrib import admin
from django.urls import path
from app1 import views
app_name='app1'

urlpatterns=[
    path('',views.app1),
    path('login/',views.login),
    path('register/', views.register,name='register'),
    path('display/', views.display,name='display'),
    path('delete/<int:id>',views.delete,name='delete'),
    path('update/<int:id>',views.update,name='update'),

]