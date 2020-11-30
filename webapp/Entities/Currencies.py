from django.db import models

# Create your models here.
class Currencies(models.Model):
    name = models.CharField(max_length=254)
    user_id = models.CharField(max_length=254)
    shortname = models.CharField(max_length=10)
    is_active = models.CharField(max_length=200)
    updated_at = models.CharField(max_length=200)
    created_at = models.CharField(max_length=200)