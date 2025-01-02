from rest_framework.serializers import ModelSerializer
from main import models as md

class WorkSer(ModelSerializer):
    class Meta:
        depth = 2
        model = md.Assignment
        fields = '__all__'

