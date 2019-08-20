from django.db import models

class Flight(models.Model):
    name = models.CharField(max_length=256)
    airborne = models.BooleanField

    def __str__(self):
        return f'name:[{self.name}] airborne:[{self.airborne}]'

