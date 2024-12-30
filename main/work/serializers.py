from rest_framework.serializers import ModelSerializer
from main import models as md

class WorkSer(ModelSerializer):
    class Meta:
        model = md.Assignment
        fields = '__all__'

class WorkStatusSer(ModelSerializer):
    class Meta:
        model = md.AssignmentStatus
        fields = '__all__'