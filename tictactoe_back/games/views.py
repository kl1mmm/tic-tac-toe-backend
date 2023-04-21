from rest_framework import generics
from .models import Game
from .serializers import GameSerializer
from rest_framework.response import Response
from rest_framework.views import APIView


# Create your views here.
class GamesViewSet(generics.ListCreateAPIView):
    queryset = Game.objects.all()
    serializer_class = GameSerializer


# class GamesViewSetCustom(APIView):
#     def get(self, request, *args, **kwargs):
#         g = Game.objects.all()
#         return Response({"games": GameSerializer(g, many=True).data})
#
#     def post(self, request, *args, **kwargs):
#         serializer = GameSerializer(data=request.data)
#         serializer.is_valid(raise_exception=True)
#         serializer.save()
#         return Response({"game": serializer.data})
#
#     def put(self, request, *args, **kwargs):
#         pk = kwargs.get("pk", None)
#         if not pk:
#             return Response({"error": "Method PUT is not allowed."})
#
#         try:
#             instance = Game.objects.get(pk=pk)
#         except:
#             Response({"error": "Object does not exists."})
#
#         serializer = GameSerializer(data=request.data, instance=instance)
#         serializer.is_valid(raise_exception=True)
#         serializer.save()
#         return Response({"game": serializer.data})
#
#     def delete(self, request, *args, **kwargs):
#         pk = kwargs.get("pk", None)
#         if not pk:
#             return Response({"error": "Method DELETE is not allowed."})
#
#         try:
#             record = Game.objects.get(pk=pk)
#             record.delete()
#         except:
#             return Response({"error": "Object does not exists"})
#
#         return Response({"game": "delete game " + str(pk)})
