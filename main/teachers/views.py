from main import models as md
from .import serializers as ser
from rest_framework.viewsets import ModelViewSet
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.pagination import PageNumberPagination
from rest_framework.permissions import IsAuthenticated
from rest_framework.filters import SearchFilter

class CustomPagination(PageNumberPagination): #paginatsiya
    page_size = 2
    page_size_query_param = 'page_size'
    max_page_size = 100

class TeacherViewSet(ModelViewSet):
    queryset = md.Teacher.objects.all()
    serializer_class = ser.TeachersSer
    permission_classes = [IsAuthenticated]
    pagination_class = CustomPagination
    filter_backends = [DjangoFilterBackend, SearchFilter]
    filterset_fields = ['grade', 'tasktable']
    search_fields = ['fullname']




