from rest_framework import serializers
from .models import User


class NormalUserSerializer(serializers.ModelSerializer):

    class Meta:
        model = User
        # fields = ("username", "superhost")
        fields = (
            "username",
            "first_name",
            "last_name",
            "email",
            )


class ReadUserSerializer(serializers.ModelSerializer):

    class Meta:
        model = User
        exclude = (
            "groups",
            "user_permissions",
            "password",
            "last_login",
            "is_active",
            "date_joined",
            )


class UserSerializer(serializers.ModelSerializer):

    password = serializers.CharField(write_only=True)

    class Meta:
        model = User
        fields = ("id", "username", "first_name", "last_name", "email", "password")
        read_only_fields = ["id"]

    def create(self, validated_data):
        password = validated_data.get("password")
        user = super().create(validated_data)
        user.set_password(password)
        user.save()
        return user
