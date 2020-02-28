from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import viewsets
from rest_framework.authentication import SessionAuthentication, BasicAuthentication
from rest_framework.filters import OrderingFilter, SearchFilter
from rest_framework.permissions import IsAdminUser, IsAuthenticated
from rest_framework_jwt.authentication import JSONWebTokenAuthentication

from functions.paginations import *

from teachers.api.v1.serializers import *


class TeacherViewSet(viewsets.ModelViewSet):
    authentication_classes = [JSONWebTokenAuthentication, SessionAuthentication, BasicAuthentication]
    permission_classes = [IsAdminUser, IsAuthenticated]
    serializer_class = None

    pagination_class = PageNumberPagination

    queryset = User.objects.all()
    filter_backends = [SearchFilter, DjangoFilterBackend, OrderingFilter]

    search_fields = ['first_name', 'last_name', 'email', 'user_type', 'date_joined']
    filterset_fields = ['id', 'first_name', 'last_name', 'email', 'user_type', 'date_joined']

    def get_queryset(self):
        return User.objects.filter(user_type="teacher")

    def get_serializer_class(self):
        if self.request.method == 'POST':
            return TeacherSignupSerlizaer
        else:
            return TeacherSerializer




