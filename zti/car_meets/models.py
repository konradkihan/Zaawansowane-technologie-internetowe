from django.db import models


# Create your models here.
class CarMeet(models.Model):
    name = models.CharField(max_length=100)
    start_date = models.DateField()
    meet_host = models.CharField(max_length=100)
    address = models.CharField(max_length=100)

    def __str__(self):
        return self.name


class MeetHost(models.Model):
    name = models.CharField(max_length=100)
    surname = models.CharField(max_length=100)
    phone = models.CharField(max_length=12)
    email = models.CharField(max_length=50)

    def __str__(self):
        return f"{self.name} {self.surname}"


class Car(models.Model):
    brand = models.CharField(max_length=100)
    model = models.CharField(max_length=100)
    year = models.IntegerField()
    license_plate = models.CharField(max_length=10)

    def __str__(self):
        return f"{self.brand} {self.model} from {self.year}"
