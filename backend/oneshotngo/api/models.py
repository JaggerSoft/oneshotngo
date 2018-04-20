from django.db import models
from django.contrib.auth.models import User


# Create your models here.class Client(models.Model):
class Client(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)

    points = models.IntegerField(default=0)
    first_name = models.CharField(max_length=20)
    last_name = models.CharField(max_length=20)
    email = models.EmailField()
    birth_date = models.DateField(null=True, blank=True)


class Establishment(models.Model):
    name = models.CharField(max_length=20)
    longitude = models.FloatField()
    latitude = models.FloatField()


class Admin(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    establishment = models.OneToOneField(Establishment, on_delete=models.CASCADE)

    name = models.CharField(max_length=20, default='Admin')


