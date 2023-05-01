from rest_framework import viewsets, generics
from rest_framework.pagination import PageNumberPagination
from rest_framework.permissions import IsAuthenticatedOrReadOnly, IsAdminUser, IsAuthenticated
from .models import Profile
from django.contrib.auth.models import User

from .permissions import IsAdminOrReadOnly
from .serializers import UserSerializer, UserCreatingSerializer
from .serializers import ProfileSerializer, ProfileCreatingSerializer


# Create your views here.

# class UserViewSet(viewsets.ModelViewSet):
#     queryset = User.objects.all()
#     serializer_class = UserSerializer
#
#
# class ProfileViewSet(viewsets.ModelViewSet):
#     queryset = Profile.objects.all()
#     serializer_class = ProfileSerializer

class UserViewPagination(PageNumberPagination):
    page_size = 25
    page_query_param = 'page_size'
    max_page_size = 10000


class UserViewSet(generics.ListCreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = (IsAuthenticated,)
    pagination_class = UserViewPagination


class UserViewUpdate(generics.RetrieveUpdateAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = (IsAdminOrReadOnly,)


class UserViewDestroy(generics.RetrieveDestroyAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = (IsAdminOrReadOnly,)


class ProfileViewSet(generics.ListCreateAPIView):
    queryset = Profile.objects.all()
    serializer_class = ProfileSerializer
    permission_classes = (IsAuthenticatedOrReadOnly,)


class ProfileViewUpdate(generics.RetrieveUpdateAPIView):
    queryset = Profile.objects.all()
    serializer_class = ProfileSerializer
    permission_classes = (IsAuthenticatedOrReadOnly,)


class ProfileViewDestroy(generics.RetrieveDestroyAPIView):
    queryset = Profile.objects.all()
    serializer_class = ProfileSerializer
    permission_classes = (IsAdminOrReadOnly,)


# Класс для создания профиля и пользователя из клиентской части приложения
class ProfileViewAdd(generics.ListCreateAPIView):
    queryset = Profile.objects.all()
    serializer_class = ProfileCreatingSerializer
    permission_classes = (IsAdminUser,)


# Класс для создания профиля и пользователя из клиентской части приложения
class UserViewAdd(generics.ListCreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserCreatingSerializer
    permission_classes = (IsAdminUser,)