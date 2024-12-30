from rest_framework.serializers import ModelSerializer
from main import models as md

class StudentSer(ModelSerializer):
    class Meta:
        depth = 2
        model = md.Student 
        fields = '__all__'  
        