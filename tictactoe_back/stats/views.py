from rest_framework import viewsets
from .models import PlayerStatistic
from .serializers import StatsSerializer


# Create your views here.
class StatsViewSet(viewsets.ModelViewSet):
    queryset = PlayerStatistic.objects.all()
    serializer_class = StatsSerializer
