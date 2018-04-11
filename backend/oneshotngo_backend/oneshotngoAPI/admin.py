from django.contrib import admin
from . import models

# Register your models here.
admin.site.register(models.Client)
admin.site.register(models.Establishment)
admin.site.register(models.Admin)
admin.site.register(models.Product)
admin.site.register(models.Reward)
admin.site.register(models.Event)
admin.site.register(models.Reservation)
admin.site.register(models.Review)