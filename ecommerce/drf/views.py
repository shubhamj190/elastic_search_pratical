from django.db import models
from rest_framework.views import APIView
from ecommerce.inventory.models import Category, Product, ProductInventory
from rest_framework.response import Response
from .serializer import AllCategorySerializer, ProductSerializer, ProductInventorySerializer
# Create your models here.

class CategoryList(APIView):
    """
    Return list of all categories
    """

    def get(self, request):
        queryset = Category.objects.all()
        serializer = AllCategorySerializer(queryset, many=True)
        return Response(serializer.data)

class ProductList(APIView):

    def get(self, request, query=None):
        queryset = Product.objects.filter(category__slug=query)
        serializer = ProductSerializer(queryset, many=True)
        return Response(serializer.data)

class ProductInventoryByWebId(APIView):

    def get(self, request, query=None):
        queryset=ProductInventory.objects.filter(product__web_id=query)
        serializer=ProductInventorySerializer(queryset, many=True)
        return Response(serializer.data)
        