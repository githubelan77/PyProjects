from django.http import HttpResponse
from django.shortcuts import render
from django.contrib import messages
from . models import Admin , Register

def TravelManagementhome(request):
    return render(request, "TravelManagementhome.html")
def checkadminlogin(request):
    if request.method == "POST":
        adminuname = request.POST["uname"]  # gets user name
        adminpwd = request.POST["pwd"]
        flag = Admin.objects.filter(username=adminuname, password=adminpwd).values()
        if flag:
            return render(request, "TravelManagementhome.html")
        else:
            return HttpResponse("Login Failed")


def signup(request):
    return render(request, "signup.html")
def homepage(request):
    return render(request, "index.html")

def loginpage(request):
    return render(request, "login.html")

def aboutpage(request):
    return render(request, "about.html")

def contactpage(request):
    return render(request, "contact.html")

def checkregistration(request):
    if request.method == "POST":
        name = request.POST["name"]
        addr = request.POST["addr"]
        email = request.POST["email"]
        phno = request.POST["phno"]
        uname = request.POST["uname"]
        pwd = request.POST["pwd"]
        cpwd = request.POST["cpwd"]
        if pwd == cpwd:
            if Register.objects.filter(username=uname).exists():
                messages.info(request,"username already exists......")
                return render(request,"register.html")
            elif Register.objects.filter(email=email).exists():
                messages.info(request,"email already exists.....")
                return render(request,"request.html")
            else:
                user=Register.objects.create(name=name,address=addr,email=email,phno=phno,username=uname,password=pwd)
                user.save()
                messages.info(request,"user created successfully....")
                return render(request,"login.html")
        else:
            messages.info(request, "Password not matching......")
            return render(request, "register.html")