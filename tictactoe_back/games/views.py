from rest_framework import viewsets
from .models import Game
from .serializers import GameSerializer
from rest_framework.response import Response
from rest_framework.views import APIView


# Create your views here.
class GamesViewSet(APIView):
    def get(self, request):
        u = Game.objects.all()
        return Response({'games': GameSerializer(u, many=True).data})

    def post(self, request):
        serializer = GameSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)

        post_new = Game.objects.create(
            player1=request.data['player1'],
            player2=request.data['player1'],
            date=request.data['date'],
            game_timing=request.data['game_timing'],
            winner=request.data['winner']
        )

        return Response({'game': GameSerializer(post_new).data})
