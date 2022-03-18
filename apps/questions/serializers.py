from rest_framework import serializers, status, validators

from ..users.serializers import UserSerializer
from .models import Question


class QuestionSerializer(serializers.ModelSerializer):
    user = UserSerializer(read_only=True)
    title = serializers.CharField(
        max_length=150,
        validators=[
            validators.UniqueValidator(
                Question.objects.all(),
                message="a question with that title already exists",
            )
        ],
    )
    question = serializers.CharField(
        validators=[
            validators.UniqueValidator(
                Question.objects.all(), message="question already exists"
            )
        ],
    )

    class Meta:
        model = Question
        fields = [
            "id",
            "title",
            "question",
            "created_at",
            "updated_at",
            "views",
            "user",
        ]

    def create(self, validated_data):
        user = None
        request = self.context.get("request")
        if request and hasattr(request, "user"):
            user = request.user

        validated_data["user"] = user

        return Question.objects.create(**validated_data)

    def update(self, instance, validated_data):
        user = None
        request = self.context.get("request")
        if request and hasattr(request, "user"):
            user = request.user

        if instance.user != user:
            err = serializers.ValidationError(
                {
                    "message": "You do not have permissions to edit this resource"
                }
            )
            err.status_code = status.HTTP_401_UNAUTHORIZED
            raise err

        instance.title = validated_data.get("title", instance.title)
        instance.question = validated_data.get("question", instance.question)
        instance.views = validated_data.get("viewers", instance.views)

        instance.save()
        return instance
