from django.urls import path
from .views.ContestView import ContestView, ContestByIdView, SubmitContestResponseView, get_question_submission_status

urlpatterns = [
    path('grade/<str:grade>/', ContestView, name="ContestView"),
    path('id/<str:id>/', ContestByIdView, name='ContestByIdView'),
    path('submit/', SubmitContestResponseView, name='SubmitContestResponseView'),
    path('status/<str:question_id>/', get_question_submission_status, name="get_question_status")
]