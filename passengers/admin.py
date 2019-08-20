from django.contrib import admin
from .models import CarryOn
from flight.models import Flight

# Register your models here.
admin.site.register(CarryOn)
admin.site.register(Flight)
