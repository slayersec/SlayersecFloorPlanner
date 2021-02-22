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
   return render(request, "main/login.php", context={"formLogin":form}) 

def register(request):
   form = UserCreationForm
   return render(request, "main/register.php", context={"formRegister":form})  

def homepage(request):
   form = UserCreationForm
   return render(request, "main/homepage.php", context={"formHomepage":form})  

# Profile and uploading an image are on the same form

def profile(request):
   form = UserCreationForm
   return render(request, "main/profile.php", context={"formProfile":form})  

def imageUpload(request):
   form = UserCreationForm
   return render(request, "main/imageUpload.php", context={"formProfile":form})