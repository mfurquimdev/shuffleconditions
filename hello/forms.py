from django import forms

CHOICES=[('1','1'), ('2','2'), ('3','3'), ('4','4'), ('5','5'), ('6','6'), ('7','7'), ('8','8'), ('9','9')] 

class NumberForm(forms.Form):
    numberchoices = forms.ChoiceField(choices=CHOICES, widget=forms.RadioSelect())
