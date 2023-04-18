from rest_framework import viewsets
from .models import PlayerStatistic
from .serializers import StatsSerializer
from rest_framework.response import Response
from rest_framework.views import APIView


# Create your views here.
class StatsViewSet(APIView):
    def get(self, request):
        p = PlayerStatistic.objects.all()
        return Response({'stats': StatsSerializer(p, many=True).data})

    def post(self, request):
        serializer = StatsSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)

        post_new = PlayerStatistic.objects.create(
            user=request.data['user'],
            count_of_games=request.data['count_of_games'],
            count_of_wins=request.data['count_of_games'],
            count_of_loses=request.data['count_of_games']
        )

        return Response({'statistic': PlayerStatistic(post_new).data})
