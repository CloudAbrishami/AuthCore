import jwt
from django.conf import settings
from django.contrib.auth import get_user_model
from rest_framework import exceptions, permissions
from rest_framework.authentication import BaseAuthentication
from rest_framework.permissions import SAFE_METHODS


class SafeJWTAuthentication(BaseAuthentication):

    def authenticate(self, request):

        User = get_user_model()
        authorization_heaader = request.headers.get('Authorization')

        if not authorization_heaader:
            return None
        try:
            # header = 'Token xxxxxxxxxxxxxxxxxxxxxxxx'
            access_token = authorization_heaader.split(' ')[1]
            payload = jwt.decode(
                access_token, settings.JWT_SECRET, algorithms=['HS256'])

        except jwt.ExpiredSignatureError:
            raise exceptions.AuthenticationFailed('access_token expired')
        except IndexError:
            raise exceptions.AuthenticationFailed('Token prefix missing')

        user = User.objects.filter(id=payload['user_id']).first()
        if user is None:
            raise exceptions.AuthenticationFailed('User not found')

        return (user, payload)


class ApiAuthentication(permissions.BasePermission):

    def has_permission(self, request, view):
        if request.method in SAFE_METHODS:
            return True

        if request.auth is None:
            return False
        # todo add control for change access level just for admin
        return False

    def has_object_permission(self, request, view, obj):
        if request.method in SAFE_METHODS:
            return True
        # check owner object
        return obj.user == request.user


class OwnProfilePermission(permissions.IsAuthenticated):
    """
    Object-level permission to only allow updating his own profile
    """

    def has_object_permission(self, request, view, obj):
        # Read permissions are allowed to any request,
        # so we'll always allow GET, HEAD or OPTIONS requests.
        if request.method in permissions.SAFE_METHODS:
            return True

        # obj here is a UserProfile instance
        return obj == request.user
