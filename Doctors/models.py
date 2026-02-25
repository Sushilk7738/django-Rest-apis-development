from django.db import models


class Doctors(models.Model):
    name = models.CharField(max_length=100)
    speciality = models.CharField(max_length=100)
    qualification = models.CharField(max_length=100)
    created_At = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'{self.name} - {self.speciality}'

        
