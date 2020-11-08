from django import forms


class HappyOrSad(forms.Form):
    happy_or_sad = forms.IntegerField(label='Informe o numero: ')