from rest_framework import viewsets, generics
from rest_framework.permissions import IsAuthenticatedOrReadOnly

from .models import PlayerStatistic
from .permissions import IsAdminOrReadOnly
from .serializers import StatsSerializer


# Create your views here.

# class StatsViewSet(viewsets.ModelViewSet):
#     queryset = PlayerStatistic.objects.all()
#     serializer_class = StatsSerializer

class StatsViewSet(generics.ListCreateAPIView):
    queryset = PlayerStatistic.objects.all()
    serializer_class = StatsSerializer
    permission_classes = (IsAuthenticatedOrReadOnly,)


class StatsViewUpdate(generics.RetrieveUpdateAPIView):
    queryset = PlayerStatistic.objects.all()
    serializer_class = StatsSerializer
    permission_classes = (IsAdminOrReadOnly,)


class StatsViewDestroy(generics.RetrieveDestroyAPIView):
    queryset = PlayerStatistic.objects.all()
    serializer_class = StatsSerializer
    permission_classes = (IsAdminOrReadOnly,)
