from django.urls import path
from .views.ContestView import ContestView, ContestByIdView, SubmitContestResponseView

urlpatterns = [
    path('grade/<str:grade>/', ContestView, name="ContestView"),
    path('id/<str:id>/', ContestByIdView, name='ContestByIdView'),
    path('submit/', SubmitContestResponseView, name='SubmitContestResponseView'),
]