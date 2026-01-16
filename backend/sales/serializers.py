from rest_framework import serializers
from .models import Plot

class PlotSerializer(serializers.ModelSerializer):
    class Meta:
        model = Plot
        fields = '__all__'
        read_only_fields = ['booked_for', 'booked_by']
    
    def validate(self, data):
        data["owner"] = data.get("owner") or "Avihs Builders"
        data["booked_for"] = data.get("booked_for") or "Not Booked"
        return data

    def validate_price(self, value):
        if value < 0:
            raise serializers.ValidationError("Price must be a positive value.")
        return value
    
class PlotBookingSerializer(serializers.Serializer):
    booked_for = serializers.CharField(required=True)