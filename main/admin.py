from django.contrib import admin
from tinymce.widgets import TinyMCE
from django.db import models


formfield_overrides = {
    models.TextField: {'widget': TinyMCE()},
    }
#admin.site.register(mapdata)

# Register your models here.
