from django.contrib.auth import get_user_model
from rest_framework import status
from rest_framework.authentication import SessionAuthentication, BasicAuthentication
from rest_framework.permissions import IsAdminUser, IsAuthenticated
from rest_framework.response import Response

from rest_framework.views import APIView
from rest_framework_jwt.authentication import JSONWebTokenAuthentication

from users.api.v1.serializers import UserInfoSerializer

User = get_user_model()


class DashboardCounters(APIView):
    authentication_classes = [JSONWebTokenAuthentication, SessionAuthentication, BasicAuthentication]
    permission_classes = [IsAdminUser, IsAuthenticated]

    @staticmethod
    def get(request):
        total_students = User.objects.filter(user_type='student').count()
        total_teachers = User.objects.filter(user_type='teacher').count()

        data = {
            'counters': {
                'total_students': total_students,
                'total_teachers': total_teachers,
            }
        }

        return Response(data, status=status.HTTP_200_OK)


class DashboardIndexData(APIView):
    authentication_classes = [JSONWebTokenAuthentication, SessionAuthentication, BasicAuthentication]
    permission_classes = [IsAdminUser, IsAuthenticated]

    @staticmethod
    def get(request):
        students = User.objects.filter(user_type='student').order_by('-date_joined')[:10]
        teachers = User.objects.filter(user_type='teacher').order_by('-date_joined')[:10]

        students_data = UserInfoSerializer(students, many=True)
        teachers_data = UserInfoSerializer(teachers, many=True)
        data = {
            'students': students_data.data,
            'teachers': teachers_data.data,
        }
        return Response(data, status=status.HTTP_200_OK)
