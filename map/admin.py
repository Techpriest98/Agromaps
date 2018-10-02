from django.contrib import admin

# Register your models here.
from .models import Field, Culture, Process

admin.site.register(Culture)
admin.site.register(Field)
admin.site.register(Process)

