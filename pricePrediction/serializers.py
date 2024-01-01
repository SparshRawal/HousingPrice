from rest_framework import serializers
from .models import HouseFeatures

class HouseSerializers(serializers.ModelSerializer):
    class Meta:
        model = HouseFeatures
        fields = '__all__'
