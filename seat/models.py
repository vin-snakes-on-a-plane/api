from django.db import models

class Seat(models.Model):
    name = models.CharField(max_length=256)
    flight = models.ForeignKey(Flight, on_delete=models.CASCADE)
    passenger = models.ForeignKey(Passenger, on_delete=models.CASCADE)

    def __str__(self):
        return f'name:[{self.name}] flight:[{self.flight}] passenger:[{self.passenger}]'
