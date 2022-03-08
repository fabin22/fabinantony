from rest_framework import serializers

from app1.models import student


class StudentSerializer(serializers.ModelSerializer):
    class Meta:
        model = student
        fields = '__all__'
