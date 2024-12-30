from django.urls import path
from .import views

urlpatterns = [
    path('',views.TeachersView.as_view(), name='teachers_url')
]