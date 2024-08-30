# myapp/serializers.py
from rest_framework import serializers
from .models import *

class detailserializer(serializers.ModelSerializer):
    class Meta:
        model = detail
        fields = '__all__'
        read_only_fields = ['__all__']

class exerciseserializers(serializers.ModelSerializer):
    class Meta:
        model = exercises
        fields = '__all__'
        read_only_fields = ['__all__']

