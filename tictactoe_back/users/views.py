from django.contrib.auth.models import User
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import viewsets
from .models import Profile
from .serializers import UserSerializer


# Create your views here.
class UserViewSet(APIView):
    def get(self, request, *args, **kwargs):
        u = User.objects.all()
        return Response({'users': UserSerializer(u, many=True).data})

    def post(self, request, *args, **kwargs):
        serializer = UserSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response({'user': serializer.data})

    def put(self, request, *args, **kwargs):
        pk = kwargs.get("pk", None)
        if not pk:
            return Response({"error": "Method PUT is not allowed."})

        try:
            instance = User.objects.get(pk=pk)
        except:
            Response({"error": "Object does not exists."})

        serializer = UserSerializer(data=request.data, instance=instance)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response({"user": serializer.data})

    def delete(self, request, *args, **kwargs):
        pk = kwargs.get("pk", None)
        if not pk:
            return Response({"error": "Method DELETE is not allowed."})

        try:
            record = User.objects.get(pk=pk)
            record.delete()
        except:
            return Response({"error": "Object does not exists"})

        return Response({"user": "delete user " + str(pk)})
