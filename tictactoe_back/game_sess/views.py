from django.db.models import Q

from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import permissions

from django.contrib.auth.models import User

from .models import Session, Chat
from .serializers import (SessionSerializers, ChatSerializers, ChatPostSerializers, UserSessionSerializer)


class Sessions(APIView):
    """Комнаты чата"""
    permission_classes = [permissions.IsAuthenticated, ]

    def get(self, request):
        sessions = Session.objects.filter(Q(creator=request.user) | Q(invited=request.user))
        serializer = SessionSerializers(sessions, many=True)
        return Response({"data": serializer.data})

    def post(self, request):
        Session.objects.create(creator=request.user)
        return Response(status=201)


class Dialog(APIView):
    """Диалог чата, сообщение"""
    permission_classes = [permissions.IsAuthenticated, ]

    # permission_classes = [permissions.AllowAny, ]

    def get(self, request):
        room = request.GET.get("room")
        chat = Chat.objects.filter(room=room)
        serializer = ChatSerializers(chat, many=True)
        return Response({"data": serializer.data})

    def post(self, request):
        # room = request.data.get("room")
        dialog = ChatPostSerializers(data=request.data)
        if dialog.is_valid():
            dialog.save(user=request.user)
            return Response(status=201)
        else:
            return Response(status=400)


class AddUsersRoom(APIView):
    """Добавление юзера в комнату"""

    def get(self, request):
        users = User.objects.all()
        serializer = UserSessionSerializer(users, many=True)
        return Response(serializer.data)

    def post(self, request):
        room = request.data.get("room")
        user = request.data.get("user")
        try:
            room = Session.objects.get(id=room)
            room.invited.add(user)
            room.save()
            return Response(status=201)
        except:
            return Response(status=400)