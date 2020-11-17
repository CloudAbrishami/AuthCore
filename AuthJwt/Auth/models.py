from django.contrib.auth.models import AbstractUser
from django.db import models


# Create your models here.


class User(AbstractUser):
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class UserType(models.IntegerChoices):
        Customer = 0
        Seller = 1

    role = models.IntegerField(
        choices=UserType.choices,
        default=UserType.Customer,
    )
