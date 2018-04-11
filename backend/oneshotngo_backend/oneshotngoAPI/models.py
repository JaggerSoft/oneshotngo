from django.db import models
from django.contrib.auth.models import User

ESTABLISHMENT_CHOICES = (
    ('bar', 'Bar'),
    ('pub', 'Pub'),
    ('spb', 'Sports Bar'),
    ('tav', 'Taverna')
)


# Create your models here.
class Client(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    points = models.IntegerField(default=0)
    birth_date = models.DateField
    date_joined = models.DateField(auto_now=True)


class Establishment(models.Model):
    name = models.CharField(max_length=20)
    latitude = models.FloatField
    longitude = models.FloatField
    type = models.CharField(choices=ESTABLISHMENT_CHOICES, max_length=3)


class Admin(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    establishment = models.OneToOneField(Establishment, on_delete=models.CASCADE)


class Menu(models.Model):
    establishment = models.OneToOneField(Establishment, on_delete=models.CASCADE)


class Product(models.Model):
    menu = models.ForeignKey("Menu", on_delete=models.CASCADE)
    name = models.CharField(max_length=20)
    price = models.IntegerField


class Reward(models.Model):
    establishment = models.ForeignKey('Establishment', on_delete=models.CASCADE)
    product = models.OneToOneField(Product, on_delete=models.CASCADE)
    cost = models.IntegerField


class Event(models.Model):
    establishment = models.ForeignKey('Establishment', on_delete=models.CASCADE)
    date = models.DateField
    price = models.IntegerField


class Reservation(models.Model):
    client = models.ForeignKey('Client', on_delete=models.CASCADE)
    event = models.ForeignKey('Event', on_delete=models.CASCADE)


class Review(models.Model):
    client = models.ForeignKey('Client', on_delete=models.CASCADE)
    establishment = models.ForeignKey('Establishment', on_delete=models.CASCADE)
    rating = models.IntegerField
    text = models.CharField(max_length=200)
