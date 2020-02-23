from User.models import User
from django.contrib import admin

# Register your models here.
class UserAdmin(admin.ModelAdmin):
    list_display = ['userId']

admin.site.register(User, UserAdmin)