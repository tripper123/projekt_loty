from .models import Loty, Kraje, Linie
from django import forms

class LotyForm(forms.ModelForm):
    lotnisko_wylot= forms.CharField(max_length=32)
    lotnisko_przylot = forms.CharField(max_length=32)
    data_lotu = forms.CharField(max_length=34)

    class Meta:
        model = Loty
        fields = ('lotnisko_wylot', 'lotnisko_przylot', 'data_lotu',)


    def __init__(self, *args, **kwargs):
        super(LotyForm,self).__init__(*args, **kwargs)

        self.fields['linia'] = forms.ModelChoiceField(queryset=Linie.objects.all())
        self.fields['kraj'] = forms.ModelChoiceField(queryset=Kraje.objects.all())