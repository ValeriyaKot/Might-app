from django.db import models
from django.contrib.auth.models import User


class EmployeeInfo(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=250)
    family_name = models.CharField(max_length=250)
    role = models.CharField(max_length=250)
    position = models.CharField(max_length=250)
