from django.contrib.auth.base_user import BaseUserManager
from django.contrib.auth.models import AbstractUser, PermissionsMixin
from django.utils.translation import gettext_lazy as _
from .BaseModel import BaseModel
from django.db import models
from .enums.GradeEnum import GradeEnum
from .enums.SectionEnum import SectionEnum


class UserManager(BaseUserManager):
    def create_user(self, email, password, **kwargs):
        if not email:
            raise ValueError(_("The email must be provided"))
        email = self.normalize_email(email)
        user = self.model(email = email, **kwargs)
        user.set_password(password)
        user.save()
        return user
    
    def create_superuser(self, email, password, **kwargs):
        kwargs.setdefault('is_staff', True)
        kwargs.setdefault('is_superuser', True)
        kwargs.setdefault('is_active', True)
        
        if kwargs.get('is_staff') != True:
            raise ValueError(_('is_staff must be True'))
        if kwargs.get('is_superuser') != True:
            raise ValueError(_('is_superuser must be True'))
        
        return self.create_user(email, password, **kwargs)
    
    


class UserModel(BaseModel, AbstractUser):
    username = None
    email = models.EmailField(unique=True, db_index=True)
    erp_number = models.CharField(max_length=15, unique=True)
    grade = models.CharField(max_length=10, choices=GradeEnum.choices())
    section = models.CharField(max_length=20, choices=SectionEnum.choices())
    
    objects = UserManager()
    
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []
    
    def __str__(self) -> str:
        return self.email