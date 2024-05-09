from rest_framework.generics import RetrieveUpdateAPIView
from rest_framework.permissions import IsAuthenticated, IsAdminUser, AllowAny
from rest_framework.authtoken.serializers import AuthTokenSerializer
from .serializers import UserProfileSerializer
from core.response import MyResponse

from knox.views import LoginView as KnoxLoginView, LogoutView as KnoxLogoutView, LogoutAllView as KnoxLogoutAllView
from authentication.core import CookieTokenAuthentication as TokenAuthentication
from django.contrib.auth import login


class LoginView(KnoxLoginView):
    """
    Custom Login View extending the Knox LoginView
    """
    permission_classes = (AllowAny,)
    authentication_classes = []

    def post(self, request, format=None):
        serializer = AuthTokenSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = serializer.validated_data['user']
        login(request, user)
        response = super().post(request, format=None)
        token = response.data["token"]
        expiry = response.data["expiry"]
        del response.data['token']

        response.set_cookie('auth_token', token,
                            httponly=True, samesite='strict', expires=expiry)
        return response


class LogoutView(KnoxLogoutView):
    """
    Custom Logout View extending the Knox LogoutView, using the CookieTokenAuthentication
    """
    authentication_classes = (TokenAuthentication,)


class LogoutAllView(KnoxLogoutAllView):
    """
    Custom LogoutAll View extending the Knox LogoutAllView, using the CookieTokenAuthentication
    """
    authentication_classes = (TokenAuthentication,)


class ProfileDetailView(RetrieveUpdateAPIView):
    """
    Profile Detail View
    """
    authentication_classes = [TokenAuthentication, ]
    permission_classes = [IsAuthenticated, IsAdminUser]

    def get(self, request, format=None):
        serializer = UserProfileSerializer(request.user)
        return MyResponse.success(data=serializer.data, message="Successfully fetched!")
