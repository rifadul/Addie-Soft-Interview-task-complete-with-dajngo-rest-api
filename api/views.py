from django.shortcuts import render
from .serializers import SalesSerializer,ProductSerializer,SalesDetailsSerializer
from rest_framework import viewsets
from .models import Sales,Product,SalesDetails,Album,Track

# Create your views here.

class SalesViewSet(viewsets.ModelViewSet):
    queryset = Sales.objects.all()
    serializer_class = SalesSerializer

class ProductViewSet(viewsets.ModelViewSet):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer

class SalesDetailsViewSet(viewsets.ModelViewSet):
    queryset = SalesDetails.objects.all()
    serializer_class = SalesDetailsSerializer
