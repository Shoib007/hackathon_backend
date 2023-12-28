from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated
from rest_framework import status
from rest_framework.response import Response
from ..models.contestModel import ContestModel
from ..models.SubmissionModel import responseModel
from django.shortcuts import get_object_or_404
from ..serializers.contestSerializer import ContestSerializer
from ..serializers.submissionSerializer import ContestSubmissionSerializer, responseSerializer


@api_view(['GET'])
@permission_classes([IsAuthenticated])
def ContestView(request, grade):
    contest = ContestModel.objects.filter(grade__grade = grade, active = True)
    serializer = ContestSerializer(contest, many = True)
    return Response(serializer.data, status = status.HTTP_200_OK)


@api_view(['GET'])
@permission_classes([IsAuthenticated])
def ContestByIdView(request, id):
    contest = get_object_or_404(ContestModel, id=id)
    serializer = ContestSerializer(contest)
    return Response(serializer.data, status = status.HTTP_200_OK)



@api_view(["POST"])
@permission_classes([IsAuthenticated])
def SubmitContestResponseView(request):
    user = request.user
    serializer = ContestSubmissionSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save(user = user)
        return Response(serializer.data, status=status.HTTP_200_OK)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET'])
@permission_classes([IsAuthenticated])
def get_question_submission_status(request, question_id):
    try:
        response = get_object_or_404(responseModel, question_id = question_id)
        serializer = responseSerializer(response)
        return Response(serializer.data, status=status.HTTP_200_OK)
    except Exception as e:
        return Response(status=status.HTTP_404_NOT_FOUND)