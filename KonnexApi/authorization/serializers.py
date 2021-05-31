from .models import Register
from rest_framework import serializers


class RegisterSerializer(serializers.ModelSerializer):
    class Meta:
        fields = '__all__'
