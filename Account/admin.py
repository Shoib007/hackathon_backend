from django.contrib import admin
from .models.GradeModel import GradeModel
from .models.UserModel import UserModel

class UserAdmin(admin.ModelAdmin):
    list_display = ['email', 'first_name', 'last_name']
    

admin.site.register(UserModel, UserAdmin)

admin.site.register([GradeModel])