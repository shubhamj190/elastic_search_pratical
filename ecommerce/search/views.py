from django.shortcuts import render
from ecommerce.inventory.models import *
from rest_framework.views import APIView
from rest_framework.pagination import LimitOffsetPagination
from ecommerce.drf.serializer import *
from .documents import ProductInventoryDocument
from elasticsearch_dsl import Q
from rest_framework.response import Response
from django.http import HttpResponse
# Create your views here.


class SearchProductInventory(APIView, LimitOffsetPagination):

    productinventory_serializer=ProductInventorySearchSerializer
    search_document= ProductInventoryDocument

    def get(self, request, query=None):
        try:
            q=Q(
                "multi_match",
                query=query,
                fields=["product.name","product.web_id","brand.name"],
                fuzziness="auto"
            )& Q(
                should =[
                    Q("match", is_default=True)
                ],
                minimum_should_match=1
            )
            search = self.search_document.search().query(q)
            response=search.execute()
            results=self.paginate_queryset(response, request, view=self)
            serializer=self.productinventory_serializer(results, many=True)
            return self.get_paginated_response(serializer.data)
        except Exception as e:
            HttpResponse(str(e), status=500)

        
