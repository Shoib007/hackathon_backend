from django.db import models
from ..models.contestModel import ContestModel
from Account.models.UserModel import UserModel
from .QuestionModel import QuestionModel
from .BaseModel import BaseModel

class responseModel(BaseModel):
    question_id = models.ForeignKey(QuestionModel, on_delete=models.DO_NOTHING, blank=True, null=True)
    code = models.JSONField()
    submitted = models.BooleanField(default=False)
    
    def __str__(self) -> str:
        return str(self.question_id.title)
    


class Submissions(BaseModel):
    contest = models.ForeignKey(ContestModel, on_delete=models.DO_NOTHING, blank=True)
    user = models.ForeignKey(UserModel, on_delete=models.DO_NOTHING, blank=True)
    response = models.ManyToManyField(responseModel)
    submitted = models.BooleanField(default=False)
    
    
    
    def __str__(self) -> str:
        return str(self.user)