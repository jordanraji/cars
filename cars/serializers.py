from rest_framework import serializers
from .models import Car, Brand


class BrandSerializer(serializers.ModelSerializer):
    class Meta:
        model = Brand
        fields = ['id', 'name']


class CarSerializer(serializers.ModelSerializer):
    id = serializers.IntegerField(read_only=False)
    class Meta:
        model = Car
        fields = ['id', 'model', 'brand', 'color', 'value', 'production_cost', 'transportation_cost']

