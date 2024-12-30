from main import models
from rest_framework.serializers import ModelSerializer


class PrincipalSer(ModelSerializer):
    class Meta:
        depth = 2
        model = models.Principal
        fields = '__all__'
