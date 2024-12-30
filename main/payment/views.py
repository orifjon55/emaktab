from django.shortcuts import render
from . import serializers as ser
from main import models as md
from rest_framework.generics import ListAPIView
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import filters
from rest_framework.pagination import PageNumberPagination


class CustomPaginator(PageNumberPagination):
    page_size = 2
    page_size_query_param = 'page_size'
    max_page_size = 5
# ===============================================
class PaymentView(ListAPIView):
    queryset = md.EMaktabPayment.objects.all().order_by('id')
    serializer_class = ser.PaymentSer
    pagination_clas = CustomPaginator
    filter_backends = [filters.SearchFilter,DjangoFilterBackend]
    search_fields = ['fullname']
    filterset_fields = ['school','student']