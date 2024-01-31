from django.http import HttpResponse
from django.shortcuts import render

from .models import Admin


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



def homepage(request):
    return render(request, "index.html")

def loginpage(request):
    return render(request, "login.html")

def aboutpage(request):
    return render(request, "about.html")

def contactpage(request):
    return render(request, "contact.html")

