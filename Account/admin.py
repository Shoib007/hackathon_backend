from django.contrib import admin
from .models.GradeModel import GradeModel
from .models.UserModel import UserModel

admin.site.register([UserModel, GradeModel])