"""
URL configuration for tictactoe_back project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from users.views import UserViewSet, UserViewUpdate, UserViewDetail
from stats.views import StatsViewSet, StatsViewUpdate, StatsViewDetail
from games.views import GamesViewSet, GamesViewUpdate, GamesViewDetail

urlpatterns = [
    path("admin/", admin.site.urls),
    path("api/v1/users_list/", UserViewSet.as_view()),
    path("api/v1/users_list/<int:pk>/", UserViewUpdate.as_view()),
    path("api/v1/users_detail/<int:pk>/", UserViewDetail.as_view()),
    path("api/v1/statistic_list/", StatsViewSet.as_view()),
    path("api/v1/statistic_list/<int:pk>/", StatsViewUpdate.as_view()),
    path("api/v1/statistic_detail/<int:pk>/", StatsViewDetail.as_view()),
    path("api/v1/games_list/", GamesViewSet.as_view()),
    path("api/v1/games_list/<int:pk>/", GamesViewUpdate.as_view()),
    path("api/v1/games_detail/<int:pk>/", GamesViewDetail.as_view())
]
