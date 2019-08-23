from rest_framework import generics
from django.http import JsonResponse
from flights.models import Flight, Seat, Passenger
from .serializers import FlightSerializer, SeatSerializer, PassengerSerializer

class FlightList(generics.ListCreateAPIView):
    queryset = Flight.objects.all()
    serializer_class = FlightSerializer

class FlightDetail(generics.RetrieveUpdateAPIView):
    queryset = Flight.objects.all()
    serializer_class = FlightSerializer

class SeatList(generics.ListCreateAPIView):
    queryset = Seat.objects.all()
    serializer_class = SeatSerializer

class SeatDetail(generics.RetrieveUpdateAPIView):
    queryset = Seat.objects.all()
    serializer_class = SeatSerializer

class PassengerList(generics.ListCreateAPIView):
    queryset = Passenger.objects.all()
    serializer_class = PassengerSerializer

class PassengerDetail(generics.RetrieveUpdateAPIView):
    queryset = Passenger.objects.all()
    serializer_class = PassengerSerializer

def get_gameboard(request):
    data = '{"backgrounds":[{"cell_type":"entrance","movement_cost":1,"y_pos":0,"x_pos":0},{"cell_type":"aisle","movement_cost":1,"y_pos":0,"x_pos":1},{"cell_type":"aisle","movement_cost":1,"y_pos":0,"x_pos":2},{"cell_type":"aisle","movement_cost":1,"y_pos":0,"x_pos":3},{"cell_type":"aisle","movement_cost":1,"y_pos":0,"x_pos":4},{"cell_type":"equipment","movement_cost":0,"y_pos":0,"x_pos":5},{"cell_type":"equipment","movement_cost":0,"y_pos":0,"x_pos":6},{"cell_type":"wall","movement_cost":0,"y_pos":0,"x_pos":7}]}'
    data = data.replace("\n", "")
    data = data.replace('\\\"', '"')
    # while data.find('  ') > 0:
    #     data = data.replace("  ", " ")
    return JsonResponse(data, safe=False)