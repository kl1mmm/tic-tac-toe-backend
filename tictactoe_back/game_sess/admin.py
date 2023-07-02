from django.contrib import admin

# Register your models here.
from .models import Session, Chat


@admin.register(Session)
class SessionAdmin(admin.ModelAdmin):
    """Сессии"""
    list_display = ("player1", "player2", "date")

    def invited_user(self, obj):
        return "\n".join([user.username for user in obj.invited.all()])


@admin.register(Chat)
class ChatAdmin(admin.ModelAdmin):
    """Диалоги"""
    list_display = ("room", "user", "text", "date")
