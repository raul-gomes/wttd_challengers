from django import forms

OPTIONS = [('1', 'jo'), ('2', 'ken'), ('3', 'po')]


class JokenpoForm(forms.Form):

    option = forms.ChoiceField(choices=OPTIONS, widget=forms.RadioSelect)

