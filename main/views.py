"""
   This page is showing what is actually displayed on the webpage. So stuff like HTML and python can
   work together to create what is showing on the physical webpage hence the class name "views"
"""

from django.shortcuts import render
from django.http import HttpResponse
from django.contrib.auth.forms import UserCreationForm

# Create your views here.

def login(request):
   form = UserCreationForm
   return render(request, "main/login.html", context={"formLogin":form}) 

def register(request):
   form = UserCreationForm
   return render(request, "main/register.html", context={"formRegister":form})  

def homepage(request):
   form = UserCreationForm
   return render(request, "main/homepage.html", context={"formHomepage":form})  

# Profile and uploading an image are on the same form

def profile(request):
   form = UserCreationForm
   return render(request, "main/profile.html", context={"formProfile":form})  

def imageUpload(request):
   form = UserCreationForm
   return render(request, "main/imageUpload.html", context={"formProfile":form})

def maps2D(request):
   form = UserCreationForm
   return render(request, "main/maps2D.html", context={"formMaps":form})

def mapsView(request):
   form = UserCreationForm
   return render(request, "main/mapsView.html", context={"formMapsView":form})