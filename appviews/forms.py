from appdata.models import Details
from appdata.models import UrgentBlood
from django import forms

class DetailsForm(forms.ModelForm):
    pic = forms.FileField(required=False)
    class Meta:
        model = Details
        fields = ('username', 'email', 'firstname', 'lastname', 'bloodgroup', 'gender', 'day', 'month', 'year', 'state', 'city', 'mobile', 'pic')

class UrgentForm(forms.ModelForm):
    class Meta:
        model = UrgentBlood
        fields = ('username', 'bloodgroup', 'name', 'mobile', 'location', 'state', 'city', 'message')

