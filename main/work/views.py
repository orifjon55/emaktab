from rest_framework.views import APIView
from rest_framework.generics import ListAPIView
from rest_framework.response import Response
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import filters
from rest_framework.pagination import PageNumberPagination
from .import serializers as ser
from main import models as md
from rest_framework.viewsets import ModelViewSet

class CustomPagination(PageNumberPagination):
    page_size = 2
    page_size_query_param = 'page_size'
    max_page_size = 5
# ===============================================

# ===============================================    
class WorkViewSet(ModelViewSet):
    queryset = md.AssignmentStatus.objects.all().order_by('-id')
    serializer_class = ser.WorkSer
    filter_backends = [filters.SearchFilter, DjangoFilterBackend]
    filterset_fields = ['student', 'assignment','completed']
    
