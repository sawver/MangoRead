from rest_framework import serializers
from rest_framework.exceptions import ValidationError
from users.models import User


class UserAuthenticationSerializer(serializers.ModelSerializer):
    username = serializers.CharField(required=True)
    password = serializers.CharField(required=True)

    class Meta:
        model = User
        fields = ["username", "password"]


class UserRegistrationSerializer(serializers.ModelSerializer):
    username = serializers.CharField(required=True)
    nickname = serializers.CharField(required=True)
    password = serializers.CharField(
        style={"input_type": "password"}, help_text="min length 4", min_length=4, required=True
    )

    class Meta:
        model = User
        fields = 'username nickname password'.split()

    """ Validating User """

    def validate_username(self, username):
        try:
            User.objects.get(username=username)
        except User.DoesNotExist:
            return username
        raise ValidationError('Такой пользователь уже существует!')
