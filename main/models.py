# ALL OF THE DIFFERENT DATABASE TABLES WE WILL NEED FOR THIS WHOLE PROJECT WILL GO IN THIS MODELS SECTION                              

"""These comments are for u Dan :)
   Models map to a database. Every new model is a new table in the database
   After creating a model down below you must implement it into the actual database
   Open the command prompt and go to the location of the project and manage.py file
   type the line: python manage.py makemigrations
   This will create the table. (Of course make sure you habe all the code for it done first)
"""
# This is an example of what it looks like when its sucessful:
# C:\Users\mikha\SlayersecFloorManager>py manage.py makemigrations
#   Migrations for 'main':
#    main\migrations\0001_initial.py
#      - Create model Tutorial

""" Then all thats left is to type: py manage.py migrate
    This makes it so that model you just created actually gets added by running the migrations

 This command: python manage.py shell
 will put you into the actually database to look at and do stuff

Then you bring everything in:

>>> from main.models import Tutorial
>>> Tutorial.objects.all()
<QuerySet []>
>>> from django.utils import timezone
>>> new_tutorial = Tutorial(tutorial_title="To Be", tutorial_content="...or not to be", tutorial_published=timezone.now() )
>>> new_tutorial.save()
>>> Tutorial.objects.all()
<QuerySet [<Tutorial: To Be>]>

Now rinse and repeat for all db's
"""

from django.db import models

# Create your models here.
class Tutorial(models.Model):
    tutorial_title = models.CharField(max_length=200)
    tutorial_content = models.TextField()
    tutorial_published = models.DateTimeField("Date Published")

    def __str__(self):
        return self.tutorial_title
    

