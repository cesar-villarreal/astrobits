from django import forms

class julianDateForm(forms.Form):
	julian_form = forms.DateTimeField(label = 'Date and time to Julian Date converter:',
                                      widget = forms.DateTimeInput(attrs={'type': 'datetime-local'}))
class dateJulianForm(forms.Form):
	date_form = forms.FloatField(label = 'Julian Date to Date converter:',
                                 widget = forms.NumberInput(attrs={'step': "0.000000001"}))
