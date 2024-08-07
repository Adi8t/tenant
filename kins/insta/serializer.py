# insta/serializers.py
from rest_framework import serializers
from django.contrib.auth.models import User
from .models import UserProfile, Client
from tenant_app.serializers import HotelSerializer

class Userserializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'username', 'email']

class ClientSerializer(serializers.ModelSerializer):
    hotels = HotelSerializer(many=True, read_only=True)

    class Meta:
        model = Client
        fields = ['id', 'name', 'hotels']

class Userprofileserializer(serializers.ModelSerializer):
    user = Userserializer()
    tenant = ClientSerializer()

    class Meta:
        model = UserProfile
        fields = ['id', 'user', 'tenant']
