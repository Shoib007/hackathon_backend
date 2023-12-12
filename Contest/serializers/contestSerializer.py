from rest_framework import serializers
from ..models.contestModel import ContestModel
from Account.Serializers.gradeSerializer import GradeSerializer
from ..serializers.questionSerializer import QuestionSerializer

class ContestSerializer(serializers.ModelSerializer):
    grade = GradeSerializer(many=True)
    question = QuestionSerializer(many=True)
    class Meta:
        model = ContestModel
        fields = ['id', 'title', 'grade', 'question', 'startTime', 'endTime', 'active']