from django.contrib import admin
from .models.contestModel import ContestModel
from .models.QuestionModel import QuestionModel
from .models.SubmissionModel import Submissions, responseModel

admin.site.register([QuestionModel, ContestModel, Submissions, responseModel])
