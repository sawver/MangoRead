from django.contrib.auth.base_user import BaseUserManager
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin
from django.db import models


class CustomUserManager(BaseUserManager):
    def create_user(self, username, password, **extra_fields):
        if not username:
            raise ValueError('username not found')

        user = self.model(
            username=username,
            **extra_fields
        )
        user.set_password(password)
        user.save()
        return user

    def create_superuser(self, username, password, **extra_fields):
        extra_fields.setdefault("is_staff", True)
        extra_fields.setdefault("is_superuser", True)

        if extra_fields.get("is_staff") is not True:
            raise ValueError('Superuser has to have is_staff being True')

        if extra_fields.get('is_superuser') is not True:
            raise ValueError('Superuser has to have superuser being True')

        return self.create_user(username=username, password=password, **extra_fields)


class User(AbstractBaseUser, PermissionsMixin):
    photo = models.ImageField(blank=True, upload_to="media")
    username = models.CharField(max_length=20, unique=True)
    nickname = models.CharField(max_length=20)
    password = models.CharField(max_length=20)
    is_staff = models.BooleanField(default=False)
    is_superuser = models.BooleanField(default=False)

    objects = CustomUserManager()

    USERNAME_FIELD = 'username'
    REQUIRED_FIELDS = ['password']

    def __str__(self):
        return self.username
