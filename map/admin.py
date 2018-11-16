from django.contrib import admin

# Register your models here.
from .models import Field, Culture, Process, SeedProcess

admin.site.site_header = 'Панель адміністрування'
admin.site.login_template = 'admin/admin_login.html'
admin.site.index_template = 'admin/admin_index.html'

admin.site.register(Culture)
admin.site.register(Process)
admin.site.register(SeedProcess)

class FieldAdmin(admin.ModelAdmin):
	list_display = ('title',)
	change_list_template = 'admin/fields_change_list.html'

admin.site.register(Field, FieldAdmin)
		