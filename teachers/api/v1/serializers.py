from rest_framework import serializers

from django.contrib.auth import get_user_model

from teachers.models import *

User = get_user_model()


class TeacherSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = [
            'id',
            'first_name',
            'last_name',
            'email',
            'username',
            'full_name',
            'user_type',
            'is_active',
            'date_joined',
        ]
        extra_kwargs = {
            'password': {
                'write_only': True
            },
            'full_name': {
                'read_only': True
            }
        }