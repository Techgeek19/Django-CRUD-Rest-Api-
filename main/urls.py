from django.contrib import admin
from django.urls import path, include
from rest_framework import routers
from main import views

router = routers.DefaultRouter()
router.register(r'product', views.ProductViewset)

urlpatterns = [
    path('api/', include(router.urls)),
]
