# Register your models here.
from django.contrib import admin
from home.models import Problem, StarterCode
from .models import HiddenTestCase

admin.site.register(HiddenTestCase)
admin.site.register(StarterCode) 
admin.site.register(Problem)

