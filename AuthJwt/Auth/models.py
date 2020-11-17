from django.contrib.auth.models import AbstractUser
from django.db import models


class UserRole(models.IntegerChoices):
    Customer = 0
    Seller = 1


class User(AbstractUser):
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    role = models.IntegerField(
        choices=UserRole.choices,
        default=UserRole.Customer,
    )


# bite meaning: Delete-Update-Create-List-Retrieve
class AccessLevel(models.IntegerChoices):
    NotAllowed = int("00000", 2)
    Delete = int("10000", 2)
    Update = int("01000", 2)
    Create = int("00100", 2)
    List = int("00010", 2)
    Retrieve = int("00001", 2)
    Delete_Update = int("11000", 2)
    Delete_Create = int("10100", 2)
    Delete_List = int("10010", 2)
    Delete_Retrieve = int("10001", 2)
    Update_Create = int("01100", 2)
    Update_List = int("01010", 2)
    Update_Retrieve = int("01001", 2)
    Create_List = int("00110", 2)
    Create_Retrieve = int("00101", 2)
    List_Retrieve = int("00011", 2)
    Delete_Update_Create = int("11100", 2)
    Delete_Update_List = int("11010", 2)
    Delete_Update_Retrieve = int("11001", 2)
    Delete_Create_List = int("10110", 2)
    Delete_Create_Retrieve = int("10101", 2)
    Delete_List_Retrieve = int("10011", 2)
    Update_Create_List = int("01110", 2)
    Update_Create_Retrieve = int("01101", 2)
    Update_List_Retrieve = int("01011", 2)
    Create_List_Retrieve = int("00111", 2)
    Delete_Update_Create_List = int("11110", 2)
    Delete_Update_Create_Retrieve = int("11101", 2)
    Delete_Update_List_Retrieve = int("11011", 2)
    Delete_Create_List_Retrieve = int("10111", 2)
    Update_Create_List_Retrieve = int("01111", 2)
    Delete_Update_Create_List_Retrieve = int("11111", 2)


class AccessControl(models.Model):
    role = models.IntegerField(
        choices=UserRole.choices,
        default=UserRole.Customer,
    )
    targetEndpoint = models.CharField(max_length=120)
    microServiceName = models.CharField(max_length=120)
    access = models.IntegerField(
        choices=AccessLevel.choices,
        default=AccessLevel.NotAllowed,
    )
