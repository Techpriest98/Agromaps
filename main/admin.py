from django.contrib import admin

# Register your models here.
from .models import Corp, Post, Preview

admin.site.register(Corp)
admin.site.register(Post)
admin.site.register(Preview)

