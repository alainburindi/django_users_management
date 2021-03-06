from django.contrib.auth.base_user import BaseUserManager
from django.contrib.auth.models import (AbstractBaseUser, PermissionsMixin)
from django.db import models


class UserManager(BaseUserManager):
    def create_user(self, **kwargs):
        """
        Creates and saves a User with the given credentials.
        """
        email = kwargs.pop("email")
        password = kwargs.pop("password")

        user = self.model.objects.filter(email=email).first()

        if user:
            raise ValueError("User with given email already exists")

        user = self.model(email=self.normalize_email(email), **kwargs)
        user.set_password(password)
        user.save()
        return user

    def create_superuser(self, **kwargs):
        super_user_args = {
            "is_active": True,
            "is_admin": True,
            "is_staff": True,
            "role": "admin"
        }
        user = self.create_user(**kwargs, **super_user_args)
        return user


class User(AbstractBaseUser, PermissionsMixin):
    email = models.EmailField(max_length=100, unique=True)
    password = models.CharField(max_length=100)
    name = models.CharField(max_length=100)
    role = models.CharField(max_length=100)
    username = models.CharField(max_length=100, null=True, blank=True)
    is_staff = models.BooleanField(default=False)
    is_admin = models.BooleanField(default=False)
    is_active = models.BooleanField(default=False)

    USERNAME_FIELD = "email"

    objects = UserManager()

    def __str__(self):
        return self.email

    class Meta:
        db_table = "users"
