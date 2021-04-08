"""SlayersecFloorManager URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.urls import path
from . import views

app_name = "main"

urlpatterns = [
    # main path is changed to view the profile. Original is: path("", views.login, name="login"),
    path("", views.login_request, name="login"),
    path("login", views.login_request, name="login"),
    path("displayProfile", views.displayProfile, name="displayProfile"),
    path("logout", views.logout_request, name="logout"),
    path("checkcred", views.checkcred, name="checkcred"),
    path("register", views.register, name="register"),
    path("homepage", views.homepage, name="homepage"),
    path("editProfile", views.editProfile, name="editProfile"),
    path("imageUpload", views.imageUpload, name="imageUpload"),
    path("maps2D", views.maps2D, name="maps2D"),
    path("mapsView", views.mapsView, name="mapsView"),
    path("saveGrid", views.saveGrid, name="saveGrid"),
    path("mapsList", views.mapsList, name="mapsList")












]
