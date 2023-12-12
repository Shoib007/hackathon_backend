from django.db import models
from .enums.GradeEnum import GradeEnum

class GradeModel(models.Model):
    grade = models.CharField(max_length=20, blank=True, choices=GradeEnum.choices(), unique=True)
    
    def __str__(self) -> str:
        return self.grade