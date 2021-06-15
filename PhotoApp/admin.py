from django.contrib import admin
from .models import User, Upload
# Register your models here.
admin.site.register(User)
admin.site.register(Upload)

class UserAdmin(admin.ModelAdmin):
    list_display = ("f_name", "l_name")
