from rest_framework import serializers
from django.contrib.auth.models import User
from .models import Profile


# class UserModel:
#     def __init__(self, title, content):
#         self.title = title
#         self.content = content


class ProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = Profile
        fields = ('id', 'patronymic_name', 'birth_date', 'sex')


class UserSerializer(serializers.ModelSerializer):
    detail = ProfileSerializer(source='profile')

    class Meta:
        model = User
        fields = ('id', 'first_name', 'last_name', 'detail')
