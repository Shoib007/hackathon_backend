from django.db import models
from .BaseModel import BaseModel
from uuid import uuid4

class QuestionModel(BaseModel):
    id = models.UUIDField(primary_key=True, unique=True, db_index = True, default=uuid4, editable=False)
    title = models.CharField(max_length=100, blank=True, default="Question Title")
    question = models.TextField()
    
    def __str__(self) -> str:
        return self.title