from django.shortcuts import render
from main.models import Product
from main import serializers
from rest_framework import viewsets

# Create your views here.

class ProductViewset(viewsets.ModelViewSet):
    queryset = Product.objects.all()
    serializer_class = serializers.ProductSerializer
