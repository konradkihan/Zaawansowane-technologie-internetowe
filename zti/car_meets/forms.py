from datetime import datetime

from django import forms


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

    def clean(self):
        cleaned_data = super().clean()

        name = cleaned_data.get("name")
        start_date = cleaned_data.get("start_date")
        meet_host = cleaned_data.get("meet_host")
        address = cleaned_data.get("address")
        description = cleaned_data.get("description")

        if 3 > len(name) > 100:
            self.add_error("name", "Nazwa powinna mieć od 3 do 100 znaków.")

        try:
            datetime.strptime(str(start_date), "%d-%m-%Y")
        except ValueError:
            self.add_error("start_date", "Podaj jakąś datę wydarzenia")

        if start_date < datetime.today().date():
            self.add_error("start_date", "Event nie może zacząć się wcześniej niż dzisiaj.")

        if 3 > len(meet_host) > 100:
            self.add_error("meet_host", "Nazwa hosta powinna mieć od 3 do 100 znaków.")

        if 1 > len(address) > 100:
            self.add_error("address", "Podaj właściwy adres")

        if len(description) > 1000:
            self.add_error("description", "Opis jest zbyt długi!")

        return cleaned_data


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

    def clean(self):
        cleaned_data = super().clean()

        brand = cleaned_data.get("brand")
        model = cleaned_data.get("model")
        year = cleaned_data.get("year")
        license_plate = cleaned_data.get("license_plate")
        description = cleaned_data.get("description")

        if len(brand) > 100 or len(brand) == 0:
            self.add_error("brand", "Uzupełnij markę samochodu od 1 do 100 znaków.")

        if len(model) > 100 or len(model) == 0:
            self.add_error("model", "Uzupełnij model pojazdu od 1 do 100 znaków.")

        if (
                brand.lower() == "toyota" and model.lower() == "prius"
        ) or (
                brand.lower() == "nissan" and model.lower() == "altima"
        ) or (
                brand.lower() == "fiat" and model.lower() == "multipla"
        ):
            self.add_error("model", "Nie. Po prostu nie.")

        if year > datetime.today().year or year < 1885:
            self.add_error("year", "A ty co? Podróżnik w czasie?")

        if len(license_plate) > 10:
            self.add_error("license_plate", "Niepoprawny numer rejestracyjny pojazdu.")

        if len(description) > 1000:
            self.add_error("description", "Opis jest zbyt długi!")
