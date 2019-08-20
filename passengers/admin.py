from django.contrib import admin
from .models import CarryOn
from .models import Flight
from .models import Seat

# Register your models here.
admin.site.register(CarryOn)
admin.site.register(Flight)
admin.site.register(Seat)
