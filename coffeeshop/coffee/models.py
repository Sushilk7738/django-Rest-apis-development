from django.db import models


class Coffee(models.Model):
    name = models.CharField(max_length=100)
    price = models.IntegerField()
    description = models.TextField()
    stock = models.IntegerField()