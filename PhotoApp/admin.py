from django.contrib import admin
from .models import User, Album, Upload
# Register your models here.
admin.site.register(User)
admin.site.register(Upload)
admin.site.register(Album)

class UserAdmin(admin.ModelAdmin):
    list_display = ("f_name", "l_name")
