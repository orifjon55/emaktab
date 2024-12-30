from main import models
from rest_framework.serializers import ModelSerializer


class PaymentSer(ModelSerializer):
    class Meta:
        depth = 2
        model = models.EMaktabPayment
        fields = '__all__'