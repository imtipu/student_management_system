from allauth.utils import generate_unique_username
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


class TeacherSignupSerlizaer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = [
            'id',
            'first_name',
            'last_name',
            'email',
            'full_name',
            'user_type',
            'is_active',
            'password',
            'date_joined',
        ]
        extra_kwargs = {
            'password': {
                'write_only': True,
                'style': {
                    'input_type': 'password'
                }
            },
            'full_name': {
                'read_only': True
            },
            'user_type': {
                'read_only': True
            },
            'is_active': {
                'read_only': True
            },
            'date_joined': {
                'read_only': True
            }
        }

    def create(self, validated_data):
        user = User(
            first_name=validated_data.get('first_name'),
            last_name=validated_data.get('last_name'),
            email=validated_data.get('email'),
            username=generate_unique_username([
                validated_data.get('first_name'),
                validated_data.get('last_name'),
                validated_data.get('email'),
                'user'
            ]),
            user_type='teacher',
            is_active=True,
        )
        user.set_password(validated_data.get('password'))
        user.save()
        return user

    def save(self, **kwargs):
        return super().save()
