from django.urls import include, path
from rest_framework import routers
from .views import GamesViewSet

router = routers.DefaultRouter()
router.register(r'games', GamesViewSet)

urlpatterns = [
    path('', include(router.urls)),
]
