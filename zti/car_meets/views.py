from django.shortcuts import render, HttpResponse
from .forms import NewMeetForm, MeetHostForm, CarMeetForm
from .models import MeetHost, CarMeet, Car
from datetime import date


# Create your views here.
def index(request):
    return render(request, "landing_page.html")


def register_meet(request):
    return render(request,
                  "new_meet.html",
                  {
                      "form": NewMeetForm
                  })


def browse_meetings(request):
    today = date.today()
    meets = CarMeet.objects.filter(start_date__gte=today).order_by('start_date')
    return render(request,
                  "browse_meets.html",
                  {"meets": meets})


def register_user(request):
    return HttpResponse("Hello, world. You're at the registration form.")


def add_new_car(request):
    return HttpResponse("Hello, world. You're at the add new car form.")
