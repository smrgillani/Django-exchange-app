from django.db import models

class Conversions(models.Model):
    user_id = models.CharField(max_length=10)
    from_id = models.CharField(max_length=10)
    to_id = models.CharField(max_length=10)
    rate = models.CharField(max_length=50)