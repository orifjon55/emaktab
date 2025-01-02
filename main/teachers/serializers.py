from rest_framework.serializers import ModelSerializer, SlugRelatedField
from main import models as md



class TeachersSer(ModelSerializer):
    class Meta:
        depth = 2
        model = md.Teacher
        fields = '__all__'