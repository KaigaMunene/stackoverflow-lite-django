from django.db import models


class TimeStampModel(models.Model):
    created_at = models.DateTimeField(verbose_name="Asked", auto_now_add=True)
    updated_at = models.DateTimeField(verbose_name="Modified", auto_now=True)

    class Meta:
        abstract = True
