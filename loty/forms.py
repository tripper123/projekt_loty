from .models import Loty, Kraje, Linie
from django import forms
from django.forms import DateInput

class LotyForm(forms.ModelForm):
    lotnisko_wylot= forms.CharField(max_length=32)
    lotnisko_przylot = forms.CharField(max_length=32)
    data_lotu = forms.DateField(widget=DateInput(
                format=('%d/%m/%Y'),
                attrs={
                    'class': 'form-control',
                    'placeholder': 'Select a date',
                    'type': 'date',}
    ))

    def __init__(self, *args, **kwargs):
        super(LotyForm,self).__init__(*args, **kwargs)
        self.fields['linia'] = forms.ModelChoiceField(queryset=Linie.objects.all())
        self.fields['kraj'] = forms.ModelChoiceField(queryset=Kraje.objects.all())

    class Meta:
        model = Loty
        fields = ('lotnisko_wylot', 'lotnisko_przylot', 'data_lotu', 'kraj' , 'linia' )
