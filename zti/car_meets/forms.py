from django import forms
from django.core.exceptions import ValidationError
from django.utils.translation import gettext_lazy as _


class NewMeetForm(forms.Form):
    name = forms.CharField(label='Nazwa spotkania',
                           max_length=100,
                           widget=forms.TextInput(attrs={"placeholder": "Super Car Meet",
                                                         "class": "mb-4 form-control"}))
    start_date = forms.DateField(label='Kiedy?',
                                 widget=forms.DateInput(
                                     attrs={"class": "mb-4 form-control",
                                            "type": "date"}))
    address = forms.CharField(label='Gdzie?',
                              max_length=100,
                              widget=forms.TextInput(
                                  attrs={"placeholder": "Warszawska 70, 99-120 Poznań",
                                         "class": "mb-4 form-control"}))
    meet_host = forms.CharField(label="Kto?",
                                max_length=100,
                                widget=forms.TextInput(
                                    attrs={"placeholder": "TOYO Group",
                                           "class": "mb-4 form-control"}))
    description = forms.CharField(label='Jak?',
                                  max_length=1000,
                                  widget=forms.Textarea(
                                      attrs={"placeholder": "Zapraszamy na nasz niezwykły meet\n"
                                                            "Będą food trucki ze zbyt drogimi frytkami\n"
                                                            "(wszyscy wiemy że nie da się im oprzeć)",
                                             "class": "mb-4 form-control"}))


class CarMeetForm(forms.Form):
    brand = forms.CharField(label='Marka', max_length=100,
                            widget=forms.TextInput(
                                attrs={"placeholder": "Toyota",
                                       "class": "mb-4 form-control"}
                            ))
    model = forms.CharField(label='Model', max_length=100,
                            widget=forms.TextInput(
                                attrs={"placeholder": "Prius",
                                       "class": "mb-4 form-control"}
                            ))
    year = forms.IntegerField(label='Rok Produkcji',
                              widget=forms.NumberInput(
                                  attrs={
                                      "placeholder": "2024",
                                      "class": "mb-4 form-control",
                                      "type": "number",
                                      "min": 1885}))

    license_plate = forms.CharField(label='Numer rejestracyjny',
                                    max_length=10,
                                    widget=forms.TextInput(
                                        attrs={
                                            "placeholder": "GD 000XD",
                                            "class": "mb-4 form-control",
                                        }
                                    ))

    description = forms.CharField(label='Opis samochodu*:',
                                  max_length=1000,
                                  required=False,
                                  widget=forms.Textarea(
                                      attrs={"placeholder": "Powiedz nam jak cudowny jest twój samochód",
                                             "class": "mb-4 form-control"}))

    image = forms.ImageField(label='Zdjęcie samochodu*', required=False,
                             widget=forms.FileInput(attrs={"class": "mb-4 form-control"}))
