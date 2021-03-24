"""
   This page is showing what is actually displayed on the webpage. So stuff like HTML and python can
   work together to create what is showing on the physical webpage hence the class name "views"
"""
from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth import login, logout, authenticate
from django.contrib import messages


# Create your views here.

def login_request(request):
    if request.user.is_authenticated():
        messages.info(request, f"Logging you in as {{user.username|title}}")
        return redirect('homepage')
    if request.method == 'POST':
        form = AuthenticationForm(request=request, data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                messages.info(request, f"You are now logged in as {username}")
                return redirect('main:homepage')
            else:
                messages.error(request, "Invalid username or password.")
        else:
            messages.error(request, "Invalid username or password.")
    form = AuthenticationForm()
    LOGIN_REDIRECT_URL = '/homepage'
    return render(request = request,
                    template_name = "main/login.html",
                    context={"form":form})

def logout_request(request):
    logout(request)
    messages.info(request, "Logged out successfully!")
    return redirect("main:login")

def register(request):
    if request.method == "POST":
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            username = form.cleaned_data.get('username')
            login(request, user)
            return redirect("main:homepage")

        else:
            for msg in form.error_messages:
                print(form.error_messages[msg])

            return render(request = request,
                          template_name = "main/register.html",
                          context={"form":form})

    form = UserCreationForm
    return render(request = request,
                  template_name = "main/register.html",
                  context={"form":form})

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
   #This code will create a database entry into the mapdata table (SAVING)
   #
   #Takes 2 variables: 
   #            name: (string at a max 20 characters) 
   #            dataset: (240 character string each being a 0 (floor), 1(wall), or 2(door)).
   #
   #  mapdata = mapdata(mapName=name, data=dataset)
   form = UserCreationForm
   return render(request, "main/maps2D.html", context={"formMaps":form})

def mapsView(request):
   form = UserCreationForm
   return render(request, "main/mapsView.html", context={"formMapsView":form})

def checkcred(request):
   form = UserCreationForm
   return render(request, "main/checkcred.py", context={"formCheckCred":form})
