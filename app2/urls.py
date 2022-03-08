
from django.urls import path

from app1.urls import urlpatterns
from app2 import views

urlpatterns=[
    path('',views.app2),
    path('login/',views.login),
    path('logout/',views.logout),

]

