from rest_framework import serializers
from flights.models import Flight, Seat, Passenger


class FlightSerializer(serializers.ModelSerializer):

    class Meta:
        fields = ('name', 'airborne', )
        model = Flight

class SeatSerializer(serializers.ModelSerializer):

    class Meta:
        fields = ('name', 'flight', 'passenger', )
        model = Seat

class PassengerSerializer(serializers.ModelSerializer):

    class Meta:
        fields = ('name', 'personal_item', 'carry_on', )
        model = Passenger

