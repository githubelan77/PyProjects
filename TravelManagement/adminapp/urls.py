from django.urls import path
from . import views
urlpatterns=[
    path('', views.homepage, name="home"),
    path("login", views.loginpage, name="login"),
    path("about", views.aboutpage, name="about"),
    path("contact", views.contactpage, name="contact"),
    path("TravelManagementhome", views.TravelManagementhome, name="TravelManagementhome"),
    path("checkadminlogin", views.checkadminlogin, name="checkadminlogin"),
    path("signup", views.signup, name="signup"),
    path("checkregistration", views.checkregistration, name="checkregistration"),
]
