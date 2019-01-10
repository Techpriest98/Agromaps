from django.contrib import admin

# Register your models here.
from .models import Field, Culture, Process, SeedProcess

admin.site.register(Field)
admin.site.register(Culture)
admin.site.register(Process)
admin.site.register(SeedProcess)