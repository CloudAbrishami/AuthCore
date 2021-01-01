from abc import ABC

from django.contrib.auth import get_user_model
from django_grpc_framework import proto_serializers
from rest_framework import serializers

from microservices_Auth_pb2 import AccessRespose


class UserLoginSerializer(serializers.Serializer):
    username = serializers.CharField(required=True)
    password = serializers.CharField(required=True)


class UserSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True)

    def create(self, validated_data):
        user = get_user_model().objects.create(
            username=validated_data['username'],
            role=validated_data['role']
        )
        user.set_password(validated_data['password'])
        user.save()
        return user

    class Meta:
        model = get_user_model()
        fields = ['id', 'username', 'password', 'created_at', 'updated_at', 'role']

class AccessProtoSerializer(proto_serializers.BaseProtoSerializer):
    retrieve = serializers.BooleanField()
    list = serializers.BooleanField()
    create = serializers.BooleanField()
    update = serializers.BooleanField()
    delete = serializers.BooleanField()
    user_id = serializers.IntegerField()

    class Meta:
        proto_class = AccessRespose
        fields = ['retrieve', 'list', 'create', 'update', 'delete', 'user_id']
