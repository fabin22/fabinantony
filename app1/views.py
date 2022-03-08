from django.http import HttpResponse
from django.shortcuts import render, redirect

from app1.models import student


def login(request):
    return render(request,'htmlprgt.html')

def logout(request):
    return HttpResponse("SEE U LATER")

def app1(request):
    return HttpResponse("vijay")




def register(request):
    if request.method == "GET":
        return render(request, "insert.html")
    else:
        name = request.POST.get("name")
        username = request.POST.get("username")
        password = request.POST.get("password")
        dob = request.POST.get("dob")
        mark = request.POST.get("mark")

    student.objects.create(name=name, username=username, password=password, dob=dob, mark=mark)
    return render(request, "insert.html")

def display(request):
    ob=student.objects.all()
    return render(request,"display.html",{"ob":ob})

def delete(request,id):
    student.objects.get(id=id).delete()
    return redirect('app1:display')

def update(request,id):
    if request.method=='GET':
        ob=student.objects.get(id=id)
        return render(request,'update.html',{"ob":ob})
    else:
        name=request.POST.get('name')
        username=request.POST.get('username')
        password=request.POST.get('password')
        dob= request.POST.get('dob')
        mark = request.POST.get('mark')

    student.objects.filter(id=id).update(name=name,username=username,password=password,dob=dob,mark=mark)
    return redirect('app1:display')
