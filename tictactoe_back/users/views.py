from rest_framework import generics
from rest_framework.response import Response
from rest_framework.views import APIView
from .models import Profile
from django.contrib.auth.models import User
from .serializers import UserSerializer
from .serializers import ProfileSerializer


# Create your views here.
class UserViewSet(generics.ListCreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer


class ProfileViewSet(generics.ListCreateAPIView):
    queryset = Profile.objects.all()
    serializer_class = ProfileSerializer

# class UserViewSetCustom(APIView):
#     def get(self, request, *args, **kwargs):
#         u = User.objects.all()
#         return Response({'users': UserSerializer(u, many=True).data})
#
#     def post(self, request, *args, **kwargs):
#         serializer = UserSerializer(data=request.data)
#         serializer.is_valid(raise_exception=True)
#         serializer.save()
#         return Response({'user': serializer.data})
#
#     def put(self, request, *args, **kwargs):
#         pk = kwargs.get("pk", None)
#         if not pk:
#             return Response({"error": "Method PUT is not allowed."})
#
#         try:
#             instance = User.objects.get(pk=pk)
#         except:
#             Response({"error": "Object does not exists."})
#
#         serializer = UserSerializer(data=request.data, instance=instance)
#         serializer.is_valid(raise_exception=True)
#         serializer.save()
#         return Response({"user": serializer.data})
#
#     def delete(self, request, *args, **kwargs):
#         pk = kwargs.get("pk", None)
#         if not pk:
#             return Response({"error": "Method DELETE is not allowed."})
#
#         try:
#             record = User.objects.get(pk=pk)
#             record.delete()
#         except:
#             return Response({"error": "Object does not exists"})
#
#         return Response({"user": "delete user " + str(pk)})
