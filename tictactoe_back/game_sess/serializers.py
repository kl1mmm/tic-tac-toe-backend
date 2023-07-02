from rest_framework import serializers
from django.contrib.auth.models import User

from .models import Session, Chat


class UserSessionSerializer(serializers.ModelSerializer):
    """Сериализация пользователя"""

    class Meta:
        model = User
        fields = ("id", "username", "first_name", "last_name")


class SessionSerializers(serializers.ModelSerializer):
    """Сериализация комнат чата"""
    player1 = UserSessionSerializer()
    player2 = UserSessionSerializer()

    class Meta:
        model = Session
        fields = ("id", "player1", "player2", "date")


class ChatSerializers(serializers.ModelSerializer):
    """Сериализация чата"""
    user = UserSessionSerializer()

    class Meta:
        model = Chat
        fields = ("user", "text", "date")


class ChatPostSerializers(serializers.ModelSerializer):
    """Сериализация чата"""

    class Meta:
        model = Chat
        fields = ("room", "text")
