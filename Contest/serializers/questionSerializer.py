from rest_framework import serializers
from ..models.QuestionModel import QuestionModel


class QuestionSerializer(serializers.ModelSerializer):
    class Meta:
        model = QuestionModel
        fields = ['id', 'title', 'question']