from ..models.GradeModel import GradeModel
from rest_framework import serializers

class GradeSerializer(serializers.ModelSerializer):
    class Meta:
        model = GradeModel
        fields = ['grade']