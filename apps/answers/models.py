from django.contrib.auth import get_user_model
from django.db import models

from ..questions.models import Question

User = get_user_model()


class Answer(models.Model):
    user = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    answer = models.TextField(verbose_name="answer", max_length=1500)
    votes = models.PositiveBigIntegerField(verbose_name="votes", default=0)

    def __str__(self) -> str:
        return self.answer
