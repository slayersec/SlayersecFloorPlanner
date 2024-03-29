from django.shortcuts import render, redirect
from django.views.generic.edit import UpdateView
from django.views import generic
from django.http import HttpResponse
from django.contrib.auth.forms import AuthenticationForm
from users.forms import CustomUserCreationForm, CustomUserChangeForm, ProfileCustomizeForm
from django.contrib.auth import login, logout, authenticate
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.contrib.auth import get_user_model
from django.contrib.auth.models import User
from django.shortcuts import get_object_or_404



# Create your views here.

def login_request(request):
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
        User = get_user_model()
        form = CustomUserCreationForm(request.POST, instance=request.user)
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

    form = CustomUserCreationForm(instance=request.user)
    return render(request = request,
                  template_name = "main/register.html",
                  context={"form":form})

@login_required
def homepage(request):
   return render(request, "main/homepage.html")

# Profile and uploading an image are on the same form
@login_required
def displayProfile(request): 
   return render(request, "main/displayProfile.html")


@login_required
def editProfile(request):
    if request.method == 'POST':
        form = ProfileCustomizeForm(request.POST, request.FILES, instance=request.user)
        if form.is_valid():
            form.save()
            messages.success(request,'Your Profile has been updated!')
            return redirect('main:homepage')
    else:  # display empty form
        form = ProfileCustomizeForm(instance=request.user)
    return render(request, "main/editProfile.html", context={"form":form})

@login_required
def imageUpload(request):
   return render(request, "main/imageUpload.html")


@login_required
def maps2D(request):
   #This code will create a database entry into the mapdata table (SAVING)
   #
   #Takes 2 variables: 
   #            name: (string at a max 20 characters) 
   #            dataset: (240 character string each being a 0 (floor), 1(wall), or 2(door)).
   #
   #  mapdata = mapdata(mapName=name, data=dataset)
   if request.method == 'POST':
       mapdata = mapdata(mapName='test', data='myImage.png')
       return redirect(saveGrid)
       
   return render(request, "main/maps2D.html")

@login_required
def mapsView(request):
   return render(request, "main/mapsView.html")

@login_required
def checkcred(request):
   return render(request, "main/checkcred.py")

@login_required
def mapsList(request):
   return render(request, "main/mapsList.html")
