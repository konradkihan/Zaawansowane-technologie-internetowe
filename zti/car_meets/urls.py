from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('new-meet/', views.register_meet, name='new-meet'),
    path('browse/', views.browse_meetings, name='browse-meets'),
    path('cars/', views.browse_cars, name='browse-cars'),
    path('new-car/', views.add_new_car, name='new-car'),
]
