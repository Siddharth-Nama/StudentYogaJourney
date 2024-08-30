# Inside admin.py of your app
from django.contrib import admin
from .models import *
from exercise.models import *

# admin.site.register(CustomUser)
admin.site.register(CustomUser)
admin.site.register(exercises)
admin.site.register(detail)
