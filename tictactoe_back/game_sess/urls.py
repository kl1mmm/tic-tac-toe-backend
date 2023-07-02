from django.urls import path
from .views import *

urlpatterns = [
    path('sessions/', Sessions.as_view()),
    path('dialog/', Dialog.as_view()),
    path('users/', AddUsersRoom.as_view()),
]
