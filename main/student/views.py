from django.shortcuts import render
from rest_framework.generics import ListAPIView
from main import models as md
from .import serializers as ser
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import filters
from rest_framework.pagination import PageNumberPagination
from rest_framework.viewsets import ModelViewSet

class CustomPagination(PageNumberPagination):
    page_size = 2
    page_size_query_param = 'page_size'
    max_page_size = 5
# ===============================================
class StudentViewSet(ModelViewSet):
    queryset = md.Student.objects.all().order_by('id')
    serializer_class = ser.StudentSer
    pagination_class = CustomPagination
    filter_backends = [filters.SearchFilter,DjangoFilterBackend]
    search_fields = ['fullname']
    filterset_fields = ['grade','school','diary','tasktable']