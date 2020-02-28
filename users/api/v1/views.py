from rest_framework import status
from rest_framework.authentication import SessionAuthentication, BasicAuthentication
from rest_framework.permissions import IsAuthenticated, IsAdminUser
from rest_framework.generics import RetrieveAPIView
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework_simplejwt.authentication import JWTAuthentication
from rest_framework_jwt.authentication import JSONWebTokenAuthentication
from users.api.v1.serializers import *

User = get_user_model()


class LoggedUserProfile(APIView):
    authentication_classes = [JSONWebTokenAuthentication, SessionAuthentication, BasicAuthentication, ]
    permission_classes = [IsAuthenticated, ]
    # serializer_class = LoggedUserSerializer

    def get(self, request):
        serializer = LoggedUserSerializer(request.user, read_only=True)
        return Response({'user': serializer.data}, status=status.HTTP_200_OK)


