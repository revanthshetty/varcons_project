from django.contrib import admin
from .models import signup
class signupadmin(admin.ModelAdmin):
    list_display=('username','email','password')
admin.site.register(signup,signupadmin)
# Register your models here.
