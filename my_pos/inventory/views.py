from django.shortcuts import render

# Create your views here.
from rest_framework import generics, permissions
from .models import Product
from .serializers import ProductSerializer 

class ProductList(generics.ListAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer 
    permission_classes = [permissions.AllowAny]  # Adjust permissions later if needed
