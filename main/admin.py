from django.contrib import admin
from tinymce.widgets import TinyMCE
from django.db import models
from users import User


formfield_overrides = {
    models.TextField: {'widget': TinyMCE()},
    }
admin.site.register(User)

# Register your models here.
