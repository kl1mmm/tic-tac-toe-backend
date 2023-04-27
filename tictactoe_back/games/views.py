from rest_framework import generics, viewsets
from rest_framework.pagination import PageNumberPagination
from rest_framework.permissions import IsAuthenticatedOrReadOnly, IsAuthenticated

from .permissions import IsAdminOrReadOnly
from .models import Game
from .serializers import GameSerializer, GameInfoSerializer


# Create your views here.
# class GamesViewSet(viewsets.ModelViewSet):
#     queryset = Game.objects.all()
#     serializer_class = GameSerializer

class GameViewPagination(PageNumberPagination):
    page_size = 15
    page_query_param = 'page_size'
    max_page_size = 10000


class GamesViewSet(generics.ListCreateAPIView):
    queryset = Game.objects.all()
    serializer_class = GameSerializer
    permission_classes = (IsAuthenticatedOrReadOnly,)
    pagination_class = GameViewPagination


class GamesViewUpdate(generics.RetrieveUpdateAPIView):
    queryset = Game.objects.all()
    serializer_class = GameSerializer
    permission_classes = (IsAdminOrReadOnly,)


class GamesViewDestroy(generics.RetrieveDestroyAPIView):
    queryset = Game.objects.all()
    serializer_class = GameSerializer
    permission_classes = (IsAdminOrReadOnly,)


class LastGamesViewSet(generics.ListCreateAPIView):
    queryset = Game.objects.all()
    serializer_class = GameInfoSerializer
    permission_classes = (IsAuthenticated,)
    pagination_class = GameViewPagination
