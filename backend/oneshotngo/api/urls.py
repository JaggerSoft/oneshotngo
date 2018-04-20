from django.urls import path, include
from . import views
from rest_framework import routers

router = routers.DefaultRouter()
router.register('clients', views.ClientsView)
router.register('establishments', views.EstablishmentView)
router.register('admins', views.AdminView)

urlpatterns =[
    path('', include(router.urls))
]