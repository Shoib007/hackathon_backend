from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated
from rest_framework import status
from rest_framework.response import Response
from ..models.contestModel import ContestModel
from django.shortcuts import get_object_or_404
from ..serializers.contestSerializer import ContestSerializer
from ..serializers.submissionSerializer import ContestSubmissionSerializer


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
    print(request.data)
    user = request.user
    serializer = ContestSubmissionSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save(user = user)
        return Response(serializer.data, status=status.HTTP_200_OK)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)