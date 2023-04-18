from django.contrib.auth.models import User
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import viewsets
from .models import Profile
from .serializers import UserSerializer


# Create your views here.
class UserViewSet(APIView):
    def get(self, request):
        u = User.objects.all()
        return Response({'users': UserSerializer(u, many=True).data})

    def post(self, request):
        serializer = UserSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)

        post_new = User.objects.create(
            first_name=request.data['first_name'],
            last_name=request.data['last_name']
        )

        return Response({'user': UserSerializer(post_new).data})
