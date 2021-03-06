from django.contrib.auth import get_user_model
from rest_framework import serializers, validators

User = get_user_model()


class UserSerializer(serializers.ModelSerializer):
    username = serializers.CharField(
        min_length=6,
        max_length=12,
        validators=[
            validators.UniqueValidator(
                User.objects.all(),
                message="A user with that username already exists",
            )
        ],
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
        min_length=8,
        max_length=32,
        write_only=True,
    )

    first_name = serializers.CharField(max_length=20)
    last_name = serializers.CharField(max_length=20)

    class Meta:
        model = User
        fields = ("username", "password", "email", "first_name", "last_name")

    def create(self, validated_data):
        user = User.objects.create_user(**validated_data)

        return user
