from django.shortcuts import render
from rest_framework.generics import ListAPIView
from rest_framework.response import Response
from .import serializers as ser
from main import models as md
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import filters
from rest_framework.pagination import PageNumberPagination
from rest_framework.viewsets import ModelViewSet
from rest_framework.filters import SearchFilter

class CustomPagination(PageNumberPagination):
    page_size = 2
    page_size_query_param = 'page_size'
    max_page_size = 5
# ===============================================
class FamilyViewSet(ModelViewSet):
    queryset = md.Family.objects.all()
    serializer_class = ser.FamilySer
    filter_backends = [DjangoFilterBackend, SearchFilter]
    search_fields = ['fullname']
    filterset_fields = ['teacher']
