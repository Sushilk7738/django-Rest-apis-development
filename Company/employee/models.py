from django.db import models


class Company(models.Model):
    name = models.CharField(max_length=100)
    industry = models.CharField(max_length=100)

    def __str__(self):
        return self.name

class Employee(models.Model):
    company = models.ForeignKey(Company, on_delete=models.CASCADE, related_name='employees')
    employee = models.CharField(max_length=100)

    def __str__(self):
        return self.employee