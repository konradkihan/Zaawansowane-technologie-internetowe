from django.shortcuts import render, HttpResponse, redirect
from .forms import NewMeetForm, CarMeetForm
from .models import CarMeet, Car
from datetime import date


# Create your views here.
def index(request):
    return render(request, "landing_page.html")


def register_meet(request):
    if request.method == "POST":
        form = NewMeetForm(request.POST)
        if form.is_valid():
            new_car_meet = CarMeet(
                name=form["name"].data,
                start_date=form["start_date"].data,
                meet_host=form["meet_host"].data,
                address=form["address"].data,
                description=form["description"].data
            )
            new_car_meet.save()
            return redirect("browse-meets")
    return render(request,
                  "new_meet.html",
                  {
                      "form": NewMeetForm
                  })


def browse_meetings(request):
    today = date.today()
    meets = list(CarMeet.objects.filter(start_date__gte=today).order_by('start_date').values())

    return render(request,
                  "browse_meets.html",
                  {"meets": meets})


def browse_cars(request):
    cars = list(Car.objects.order_by('brand').values())
    return render(request,
                  "browse_cars.html",
                  {"cars": cars})


def add_new_car(request):
    if request.method == "POST":
        form = CarMeetForm(request.POST)
        if form.is_valid():
            image = request.FILES.get("image")
            new_car = Car(
                brand=form["brand"].data,
                model=form["model"].data,
                year=form["year"].data,
                license_plate=form["license_plate"].data,
                description=form["description"].data,
                image=image
            )
            new_car.save()
            return redirect("browse-cars")

    return render(request,
                  "new_car.html",
                  {"form": CarMeetForm})
