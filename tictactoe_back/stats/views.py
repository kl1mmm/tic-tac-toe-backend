from rest_framework import generics
from .models import PlayerStatistic
from .serializers import StatsSerializer
from rest_framework.response import Response
from rest_framework.views import APIView


# Create your views here.
class StatsViewSet(generics.ListCreateAPIView):
    queryset = PlayerStatistic.objects.all()
    serializer_class = StatsSerializer

# class StatsViewSetCustom(APIView):
#     def get(self, request, *args, **kwargs):
#         p = PlayerStatistic.objects.all()
#         return Response({"stats": StatsSerializer(p, many=True).data})
#
#     def post(self, request, *args, **kwargs):
#         serializer = StatsSerializer(data=request.data)
#         serializer.is_valid(raise_exception=True)
#         serializer.save()
#         return Response({"statistic": serializer.data})
#
#     def put(self, request, *args, **kwargs):
#         pk = kwargs.get("pk", None)
#         if not pk:
#             return Response({"error": "Method PUT is not allowed."})
#
#         try:
#             instance = PlayerStatistic.objects.get(pk=pk)
#         except:
#             Response({"error": "Object does not exists."})
#
#         serializer = StatsSerializer(data=request.data, instance=instance)
#         serializer.is_valid(raise_exception=True)
#         serializer.save()
#         return Response({"statistic": serializer.data})
#
#     def delete(self, request, *args, **kwargs):
#         pk = kwargs.get("pk", None)
#         if not pk:
#             return Response({"error": "Method DELETE is not allowed."})
#
#         try:
#             record = PlayerStatistic.objects.get(pk=pk)
#             record.delete()
#         except:
#             return Response({"error": "Object does not exists"})
#
#         return Response({"post": "delete statistic of " + str(pk)})
