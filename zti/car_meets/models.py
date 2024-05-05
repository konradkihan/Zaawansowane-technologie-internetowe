from django.db import models


# Create your models here.
class CarMeet(models.Model):
    name = models.CharField(max_length=100)
    start_date = models.DateField()
    meet_host = models.CharField(max_length=100)
    address = models.CharField(max_length=100)
    description = models.TextField(max_length=1000)

    def __str__(self):
        return self.name


class Car(models.Model):
    brand = models.CharField(max_length=100)
    model = models.CharField(max_length=100)
    year = models.IntegerField()
    license_plate = models.CharField(max_length=10)
    description = models.TextField(max_length=1000)
    image = models.ImageField(upload_to='car_images/', null=True, blank=True)

    def __str__(self):
        return f"{self.brand} {self.model} from {self.year}"
