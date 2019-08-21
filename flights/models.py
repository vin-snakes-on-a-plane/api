from django.db import models

# Create your models here.
class Flight(models.Model):
    name = models.CharField(max_length=256)
    airborne = models.BooleanField()

    def __str__(self):
        return f'name:[{self.name}] airborne:[{self.airborne}]'

class CarryOn(models.Model):
    name = models.CharField(max_length=256)
    attack = models.IntegerField(default=100)

    def __str__(self):
        return f'{self.name} - {self.attack}'

class Passenger(models.Model):
    name = models.CharField(max_length=256)
    personal_item = models.ForeignKey(CarryOn, on_delete=models.SET_DEFAULT, default=None, related_name='personal_item')
    carry_on = models.ForeignKey(CarryOn, on_delete=models.SET_DEFAULT, default=None, related_name='carry_on')

    # @TODO
    # class Meta:
    #     abstract = True

    def __str__(self):
        return self.name

class Seat(models.Model):
    name = models.CharField(max_length=256)
    flight = models.ForeignKey(Flight, on_delete=models.CASCADE)
    passenger = models.OneToOneField(Passenger, on_delete=models.CASCADE, default=None)

    def __str__(self):
        return f'name:[{self.name}] flight:[{self.flight}] passenger:[{self.passenger}]'

class ThreeGs(Passenger):
    accessories = models.CharField(max_length=256)

    def sanitizer_spray(self, snake):
        snake.health -= 10
        print("Ew gross!")
