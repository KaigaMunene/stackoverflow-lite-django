from rest_framework import serializers, status, validators

from apps.questions.serializers import QuestionSerializer
from apps.users.serializers import UserSerializer

from .models import Answer


class AnswerSerializer(serializers.ModelSerializer):
    question = QuestionSerializer(read_only=True)
    user = UserSerializer(read_only=True)
    answer = serializers.CharField()

    class Meta:
        model = Answer
        fields = ["id", "question", "answer", "user"]

    def create(self, validated_data):
        user = None
        request = self.context.get("request")
        if request and hasattr(request, "user"):
            user = request.user

        validated_data["user"] = user
        validated_data["question"] = self.context.get("question")
        return Answer.objects.create(**validated_data)

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
        instance.answer = validated_data.get("answer", instance.answer)

        return instance
