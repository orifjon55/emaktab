from django.shortcuts import render
from rest_framework.generics import ListAPIView
from rest_framework.response import Response
from .import serializers as ser
from main import models as md
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import filters
from rest_framework.pagination import PageNumberPagination

class CustomPagination(PageNumberPagination):
    page_size = 2
    page_size_query_param = 'page_size'
    max_page_size = 5
# ===============================================
class Family(ListAPIView):
    queryset = md.Family.objects.all().order_by('id')
    serializer_class = ser.FamilySer
    pagination_class = CustomPagination
    search_fields = ['fullname']
    filterset_fields = '__all__'