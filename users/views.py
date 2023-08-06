from django.contrib.auth import authenticate, login, logout
from rest_framework import viewsets, response, status, views, permissions
from users import models, serializers
from rest_framework.authtoken.models import Token


class UserRegistrationViewSet(viewsets.GenericViewSet):
    serializer_class = serializers.UserRegistrationSerializer

    def post(self, request, *args, **kwargs):
        serializer = self.serializer_class(data=request.data)
        serializer.is_valid(raise_exception=True)
        """ Receiving User """
        photo = request.data.get('photo')
        username = request.data.get('username')
        nickname = request.data.get('nickname')
        password = request.data.get('password')
        """ Create User """
        user = models.User.objects.create_user(photo=photo, username=username, nickname=nickname, password=password)
        return response.Response(data={'user_id': user.id})

    def list(self, request):
        return response.Response(status=status.HTTP_200_OK)


class UserAuthenticationViewSet(viewsets.GenericViewSet):
    serializer_class = serializers.UserAuthenticationSerializer

    def post(self, request, *args, **kwargs):
        serializer = self.serializer_class(data=request.data)
        serializer.is_valid(raise_exception=True)
        """ Authenticate User """
        user = authenticate(**serializer.validated_data)
        if user:
            """ Authorize User """
            token, created = Token.objects.get_or_create(user=user)
            login(request, user)
            return response.Response(data={'key': token.key})
        """ Unauthorizing Error """
        return response.Response(status=status.HTTP_401_UNAUTHORIZED)

    def list(self, request):
        return response.Response(status=status.HTTP_200_OK)


class UserLogoutAPIViewSet(viewsets.GenericViewSet):
    permission_classes = [permissions.IsAuthenticated]

    def list(self, request):
        logout(request)
        return response.Response({"detail": "Вы успешно вышли из системы."})
