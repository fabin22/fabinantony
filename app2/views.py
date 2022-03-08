from django.http import HttpResponse
from django.shortcuts import render

def login(request):
    return HttpResponse("THANK YOU FOR VISITING")
def logout(request):
    return HttpResponse("SEE U LATER")
def app2(request):
    return HttpResponse("VIJAY")



