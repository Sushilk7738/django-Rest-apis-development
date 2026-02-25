from django.db import models


class Players(models.Model):
    name = models.CharField(max_length=100)
    role = models.CharField(max_length=100)
    achievements = models.CharField()
    created_At = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.name} - {self.achievements}"