from django.contrib import admin
from .models import Car, CarMeet, MeetHost

# Register your models here.
admin.site.register(Car)
admin.site.register(CarMeet)
admin.site.register(MeetHost)
