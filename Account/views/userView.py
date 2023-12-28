from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated
from rest_framework import status
from rest_framework.response import Response
from rest_framework_simplejwt.tokens import RefreshToken
from ..Serializers.userSerializer import UserSerializer


@api_view(["GET"])
@permission_classes([IsAuthenticated])
def UserLoginView(request):
    user = request.user
    serializer = UserSerializer(user)
    return Response(serializer.data, status=status.HTTP_200_OK)


@api_view(['POST'])
def UserRegisterView(request):
    print(request.data)
    serializer = UserSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_406_NOT_ACCEPTABLE)
    

@api_view(['POST'])
@permission_classes([IsAuthenticated])
def UserLogoutView(request):  
    refresh_token = request.data.get('refresh_token')
    if not refresh_token:
        return Response({'error' : 'Refresh token not found'}, status=status.HTTP_400_BAD_REQUEST)
    
    try:
        token = RefreshToken(refresh_token)
        token.blacklist()
    except Exception as e:
        return Response({'error':str(e)}, status=status.HTTP_400_BAD_REQUEST)
    
    return Response({'message':'Loged out successfully'}, status=status.HTTP_200_OK)