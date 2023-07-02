# from channels.auth import AuthMiddlewareStack
# from rest_framework.authtoken.models import Token
# from django.contrib.auth.models import AnonymousUser
# from django.db import close_old_connections
#
#
# class TokenAuthMiddleware:
#     """Token authorization"""
#
#     def __init__(self, inner):
#         self.inner = inner
#
#     def __call__(self, scope):
#         headers = dict(scope['headers'])
#         if b'authorization' in headers:
#             try:
#                 token_name, token_key = headers[b'authorization'].decode().split()
#                 if token_name == 'Token':
#                     token = Token.objects.get(key=token_key)
#                     scope['user'] = token.user
#                     close_old_connections()
#             except Token.DoesNotExist:
#                 scope['user'] = AnonymousUser()
#         return self.inner(scope)

from urllib.parse import parse_qs

from channels.auth import AuthMiddleware
from channels.db import database_sync_to_async
from channels.sessions import CookieMiddleware, SessionMiddleware

from rest_framework.authtoken.models import Token
from django.contrib.auth.models import AnonymousUser


@database_sync_to_async
def get_user(scope):
    query_string = parse_qs(scope['query_string'].decode())
    token = query_string.get('token')
    if not token:
        return AnonymousUser()
    try:
        user = Token.objects.get(key=token[0]).user

    except Exception as exception:
        return AnonymousUser()
    if not user.is_active:
        return AnonymousUser()
    return user


class TokenAuthMiddleware(AuthMiddleware):
    async def resolve_scope(self, scope):
        scope['user']._wrapped = await get_user(scope)


def TokenAuthMiddlewareStack(inner):
    return CookieMiddleware(SessionMiddleware(TokenAuthMiddleware(inner)))
