from ..models.SubmissionModel import Submissions, responseModel
from ..models.QuestionModel import QuestionModel
from ..serializers.questionSerializer import QuestionSerializer
from rest_framework import serializers

class responseSerializer(serializers.ModelSerializer):
    # question = QuestionSerializer()
    class Meta:
        model = responseModel
        fields = ['question_id', 'code', 'submitted']


class ContestSubmissionSerializer(serializers.ModelSerializer):
    response = responseSerializer(many = True)
    
    class Meta:
        model = Submissions
        fields = ['contest', 'user', 'response', 'submitted']
        

    def create(self, validated_data):
        response_data = validated_data.pop('response')
        submission = Submissions.objects.create(**validated_data)
        
        for response_data in response_data:
            question_id = response_data.pop('question_id').id  # The response is the object of question, that's why I'm using ( .id ) after pop 
            code_data = response_data.get('code')
            question = QuestionModel.objects.get(id = question_id)
            response = responseModel.objects.create(question_id = question, code = code_data, submitted = True)
            submission.response.add(response)
        return submission   