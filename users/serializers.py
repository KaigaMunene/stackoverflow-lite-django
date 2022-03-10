from django.contrib.auth.models import User
from rest_framework import serializers, validators


class RegisterSerializer(serializers.ModelSerializer):
    username = serializers.CharField(
        validators=[
            validators.UniqueValidator(
                User.objects.all(), message="Username not available"
            ),
        ]
    )

    email = serializers.EmailField(
        validators=[
            validators.UniqueValidator(
                User.objects.all(),
                message="A user with that Email already exists",
            ),
        ]
    )

    password = serializers.CharField(
        min_length=8, max_length=32, validators=[]
    )

    first_name = serializers.CharField()
    last_name = serializers.CharField()

    class Meta:
        model = User
        fields = ("username", "password", "email", "first_name", "last_name")

    def create(self, validated_data):
        user = User.objects.create(**validated_data)

        return user
