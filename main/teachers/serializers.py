from rest_framework.serializers import ModelSerializer
from main import models as md

class TeachersSer(ModelSerializer):
    class Meta:
        model = md.Teacher
        fields = '__all__'