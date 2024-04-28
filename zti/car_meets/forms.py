from django import forms


class NewMeetForm(forms.Form):
    name = forms.CharField(label='Name',
                           max_length=100,
                           widget=forms.TextInput(attrs={"placeholder": "Super Car Meet"}))
    start_date = forms.DateField(label='Start Date')
    end_date = forms.DateField(label='End Date')
    address = forms.CharField(label='Address', widget=forms.TextInput(attrs={"placeholder": "Address"}))
    meet_host = forms.CharField(label="Meet Host", widget=forms.TextInput(attrs={"placeholder": "Meet Host"}))


class MeetHostForm(forms.Form):
    name = forms.CharField(label='Name', max_length=100)
    surname = forms.CharField(label='Surname', max_length=100)
    phone = forms.CharField(label='Phone Number', max_length=12)
    email = forms.EmailField(label='Email Address', max_length=50)


class CarMeetForm(forms.Form):
    brand = forms.CharField(label='Brand', max_length=100)
    model = forms.CharField(label='Model', max_length=100)
    year = forms.IntegerField(label='Year')
    license_plate = forms.CharField(label='License Plate', max_length=10)
