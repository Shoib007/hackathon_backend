from django.db import models
from .BaseModel import BaseModel
from uuid import uuid4
from .QuestionModel import QuestionModel
from Account.models.GradeModel import GradeModel

class ContestModel(BaseModel):
    id = models.UUIDField(primary_key=True, default=uuid4, unique=True, db_index=True, editable=False)
    title = models.CharField(max_length=100, default="Contest Title")
    grade = models.ManyToManyField(GradeModel)
    question = models.ManyToManyField(QuestionModel)
    startTime = models.DateTimeField()
    endTime = models.DateTimeField()
    active = models.BooleanField(default=True)
    
    
    def __str__(self) -> str:
        return str(self.title)
    