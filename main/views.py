"""
   This page is showing what is actually displayed on the webpage. So stuff like HTML and python can
   work together to create what is showing on the physical webpage hence the class name "views"
"""
import mysql.connector as mysql
from django.shortcuts import render
from django.http import HttpResponse
from django.contrib.auth.forms import UserCreationForm

# Create your views here.

def login(request):
   form = UserCreationForm
   if request.POST:
      uname = request.POST.get('uname', None)
      psw = request.POST.get('psw', None)
      print("Hello!")
      print(uname)
      print(psw)
      nav = 0
      db_connection = mysql.connect(host="slayersec.mysql.pythonanywhere-services.com", database="slayersec$testslayersecdatabase", user="slayersec", password="13146@Data")
      sql = "SELECT * FROM login_table WHERE username = '$uname'  and password= '$psw'"
      values = (uname,psw)
      user_cursor = db_connection.cursor()
      try:
         user_cursor.execute(sql, values)
         db_connection.commit()
         user_cursor.close()
         nav = 1
         html = "<html><body>Read $uname, $psw  .</body></html>" % now
         return HttpResponse(html)
         #return render(request, "main/login.html", context={"formLogin":form})
      except:
         user_cursor.close()
         nav = 0
         html = "<html><body>Read $uname, $psw in except .</body></html>" % now
         return HttpResponse(html)
         #return render(request, "main/login.html", context={"formLogin":form})
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

def checkcred(request):
   form = UserCreationForm
   return render(request, "main/checkcred.py", context={"formCheckCred":form})
