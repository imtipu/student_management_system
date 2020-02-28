from rest_framework import serializers
from django.contrib.auth import get_user_model

User = get_user_model()


class LoggedUserSerializer(serializers.ModelSerializer):

    class Meta:
        model = User
        fields = [
            'id',
            'username',
            'full_name',
            'email',
            'first_name',
            'last_name',
            'user_type',
            'is_active',
            'is_staff',
            'is_superuser',
            'date_joined',
        ]