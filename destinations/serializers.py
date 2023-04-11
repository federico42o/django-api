from rest_framework import serializers
from .models import Location, Destination

class LocationDTO(serializers.ModelSerializer):
    class Meta:
        model = Location
        fields = '__all__'

class DestinationDTO(serializers.ModelSerializer):
    class Meta:
        model = Destination
        fields = '__all__'