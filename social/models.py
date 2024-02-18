from django.db import models


class PredictionPauvrete(models.Model):
    result = models.FloatField()
    created_at = models.DateField(auto_now_add=True)
