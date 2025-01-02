from django.urls import path
from .import views
from rest_framework.routers import SimpleRouter

router = SimpleRouter()

router.register('', views.StudentViewSet, basename='student')

urlpatterns = router.urls