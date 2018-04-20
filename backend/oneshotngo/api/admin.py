from django.contrib import admin
from .models import Client, Establishment, Admin

# Register your models here.
admin.site.register(Client)
admin.site.register(Establishment)
admin.site.register(Admin)
