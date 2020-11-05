from django import forms


class NumberForm(forms.Form):
    number = forms.IntegerField(label='Informe o Numero: ')