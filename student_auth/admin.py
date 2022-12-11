from django.contrib import admin
from .models import User
# Register your models here. 

class UserAdmin(admin.ModelAdmin):

    List_display = ('name','email','is_email_verified')
    search_fields = ('name','email','is_email_verified')
    List_per_page=25

admin.site.register(User,UserAdmin)