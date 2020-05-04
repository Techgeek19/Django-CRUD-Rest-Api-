from django.shortcuts import render
from main.models import Product
from main import serializers
from rest_framework import viewsets

# Create your views here.

class ProductViewset(viewsets.ModelViewSet):
    queryset = Product.objects.all()
    serializer_class = serializers.ProductSerializer
    # Searching in Name 
    def get_queryset(self):
        pname= self.request.GET.get("pname")
        if pname== None:
            pname= ""
        return Product.objects.filter(name__icontains= pname)

