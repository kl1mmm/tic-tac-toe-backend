from rest_framework import viewsets, generics
from rest_framework.pagination import PageNumberPagination
from rest_framework.permissions import IsAuthenticatedOrReadOnly, IsAuthenticated

from .models import PlayerStatistic
from .permissions import IsAdminOrReadOnly
from .serializers import StatsSerializer, RatingSerializer


# Create your views here.

# class StatsViewSet(viewsets.ModelViewSet):
#     queryset = PlayerStatistic.objects.all()
#     serializer_class = StatsSerializer

class StatsViewPagination(PageNumberPagination):
    page_size = 25
    page_query_param = 'page_size'
    max_page_size = 10000


class StatsViewSet(generics.ListCreateAPIView):
    queryset = PlayerStatistic.objects.all()
    serializer_class = StatsSerializer
    permission_classes = (IsAuthenticatedOrReadOnly,)
    pagination_class = StatsViewPagination


class StatsViewUpdate(generics.RetrieveUpdateAPIView):
    queryset = PlayerStatistic.objects.all()
    serializer_class = StatsSerializer
    permission_classes = (IsAuthenticated,)


class StatsViewDestroy(generics.RetrieveDestroyAPIView):
    queryset = PlayerStatistic.objects.all()
    serializer_class = StatsSerializer
    permission_classes = (IsAdminOrReadOnly,)


class RatingViewSet(generics.ListCreateAPIView):
    queryset = PlayerStatistic.objects.all()
    serializer_class = RatingSerializer
    permission_classes = (IsAdminOrReadOnly,)
