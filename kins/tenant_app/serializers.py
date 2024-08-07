from rest_framework import serializers
from .models import Hotel
from insta.models import Client

class HotelSerializer(serializers.ModelSerializer):
    class Meta:
        model = Hotel
        fields = ['id', 'name', 'location', 'rating']

