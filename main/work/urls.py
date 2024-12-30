from django.urls import path
from .import views

urlpatterns = [
    path('',views.WorkView.as_view(), name='work_url'),
    path('status/',views.WorkStatus.as_view(), name='work_status_url'),
]