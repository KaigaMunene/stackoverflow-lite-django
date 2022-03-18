from email import message

from django.utils import timezone
from rest_framework import serializers, validators

from .models import Question


class QuestionSerializer(serializers.ModelSerializer):
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
        max_length=1000,
        validators=[
            validators.UniqueValidator(
                Question.objects.all(), message="question already exists"
            )
        ],
    )

    class Meta:
        model = Question
        fields = ["id", "title", "question"]

    def create(self, validated_data):
        return Question.objects.create(**validated_data, user=self.context)

    def update(self, instance, validated_data):
        instance.title = validated_data.get("title", instance.title)
        instance.question = validated_data.get("question", instance.question)
        instance.views = validated_data.get("created_at", instance.views)
        return instance
