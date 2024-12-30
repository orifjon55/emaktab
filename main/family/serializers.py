from rest_framework.serializers import ModelSerializer
from main import models

class FamilySer(ModelSerializer):
    class Meta:
        depth = 2
        model = models.Family
        fields = '__all__'