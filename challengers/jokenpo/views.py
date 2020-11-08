from django.contrib import messages
from django.http import HttpResponseRedirect
from django.shortcuts import render

from challengers.jokenpo.form import JokenpoForm


def jokenpo(request):

    if request == 'POST':
        move = JokenpoForm(request.POST)
        if move.is_valid():
            play = move.cleaned_data
        print(play)
        return HttpResponseRedirect('/jokenpo/')
    else:
        return render(request, 'jokenpo.html')
