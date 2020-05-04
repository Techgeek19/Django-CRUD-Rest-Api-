from django.contrib import admin
from django.urls import path, include
from rest_framework import routers
from main import views
from rest_framework_jwt.views import obtain_jwt_token

router = routers.DefaultRouter()
router.register(r'product', views.ProductViewset)

urlpatterns = [
    path('api/', include(router.urls)),
    path(r'api-token-auth/', obtain_jwt_token),
]
