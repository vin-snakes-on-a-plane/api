from rest_framework import serializers
from flights.models import Flight

class FlightSerializer(serializers.ModelSerializer):

    class Meta:
        fields = ('name', 'airborne', )
        model = Flight
