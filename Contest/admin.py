from django.contrib import admin
from .models.contestModel import ContestModel
from .models.QuestionModel import QuestionModel
from .models.SubmissionModel import Submissions, responseModel

class ContestAdmin(admin.ModelAdmin):
    list_display = ['id','startTime','endTime','active']

class SubmissionAdmin(admin.ModelAdmin):
    list_display = ['contest', 'user', 'submitted']

class ResponseAdmin(admin.ModelAdmin):
    list_display = ['question_id', 'submitted']

admin.site.register(ContestModel, ContestAdmin)
admin.site.register(Submissions, SubmissionAdmin)
admin.site.register(responseModel, ResponseAdmin)

admin.site.register([QuestionModel])
