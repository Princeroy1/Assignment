from rest_framework import serializers
from .models import Location, Ad,DailyVisitor

class LocationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Location
        fields = '__all__'

class AdSerializer(serializers.ModelSerializer):
    class Meta:
        model = Ad
        fields = '__all__'
        # exclude = ['id']
        
class VisitorCountSerializer(serializers.ModelSerializer):
    class Meta:
        model = DailyVisitor
        fields = '__all__'