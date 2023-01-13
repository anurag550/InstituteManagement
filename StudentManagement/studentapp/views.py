from django.contrib.auth import logout
from django.db.models import Q
from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.contrib.auth.models import User, auth

# Create your views here.
from studentapp.models import Student, City, Course


def login_fun(request):
    if request.method == "POST":
        username = request.POST['txtname']
        password = request.POST['txtpassword']
        user = auth.authenticate(username=username, password=password)
        if user is not None:
            auth.login(request, user)
            return redirect("home")
        else:
            return render(request, "login.html",{'data':'Username and email is invalid'})
    else:
        return render(request,"login.html",{'data':''})


def register_fun(request):
    # if request.method == "POST":
    #     username = request.POST['txtname']
    #     password = request.POST['txtpassword']
    #     email = request.POST['txtmail']
    #     if User.objects.filter(Q(username=user_name) | Q(email=user_email)).exists():
    #         return render(request, "register.html",{'data':'Username and email is already exists'})
    #     else:
    #         user = User.objects.create_superuser(username=user_name, email=user_email, password=user_password)
    #         user.save()
    #         return render(request,'login.html')
    # else:
        return render(request,"register.html",{'data':''})

def regdata_fun(request):
    user_name = request.POST['txtname']
    user_password = request.POST['txtpassword']
    user_email = request.POST['txtmail']
    if User.objects.filter(Q(username=user_name) | Q(email=user_email)).exists():
        return render(request, "register.html",{'data':'Username and email is already exists'})
    else:
        user = User.objects.create_superuser(username=user_name, email=user_email, password=user_password)
        user.save()
        return redirect('login')

def home_fun(request):
    return render(request,"home.html")


def add_fun(request):
    city=City.objects.all()# the data will be in list format
    course=Course.objects.all()
    s1=Student()
    if request.method=='POST':
        s1.Stud_Name=request.POST['txtname']
        s1.Stud_Age=request.POST['txtage']
        s1.Stud_Phone=request.POST['txtphno']
        s1.Stud_City=City.objects.get(City_Name=request.POST['ddlcity'])
        s1.Stud_Course=Course.objects.get(Course_Name=request.POST['ddlcourse'])
        s1.save()
        return redirect("add")
    else:
        return render(request,"add.html",{'City_Data':city,'Course_Data':course})


def logout_fun(request):
    logout(request)
    return redirect("/")


def disp_fun(request):
    s1 = Student.objects.all()
    return render(request,"display.html",{'data':s1})

def update_fun(request,id):
    s1 = Student.objects.get(id=id)
    city=City.objects.all()
    course=Course.objects.all()
    if request.method=='POST':
        s1.Stud_Name = request.POST['txtname']
        s1.Stud_Age = request.POST['txtage']
        s1.Stud_Phone = request.POST['txtphno']
        s1.Stud_City = City.objects.get(City_Name=request.POST['ddlcity'])
        s1.Stud_Course = Course.objects.get(Course_Name=request.POST['ddlcourse'])
        s1.save()
        return redirect('display')
    return render(request,'update.html',{'data':s1,'City_Data':city,'Course_Data':course})


def delete_fun(request,id):
    s1 = Student.objects.get(id=id)
    s1.delete()
    return redirect('display')