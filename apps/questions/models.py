from django.contrib.auth import get_user_model
from django.db import models

from apps.abstract import TimeStampModel

User = get_user_model()


class Question(TimeStampModel):
    user = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
    title = models.CharField(verbose_name="title", max_length=250)
    question = models.TextField(verbose_name="question")
    views = models.PositiveIntegerField(verbose_name="viewers", default=0)

    def __str__(self) -> str:
        return self.title
