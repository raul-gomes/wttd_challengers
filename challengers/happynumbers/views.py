from django.http import HttpResponseRedirect
from django.contrib import messages
from django.shortcuts import render

from challengers.happynumbers.form import HappyOrSad
from challengers.happynumbers.model.happynumbersCode import happy_numbers


def happynumbers(request):
    if request.method == 'POST':
        return create(request)
    else:
        return new(request)


def create(request):

    happy_or_sad = HappyOrSad(request.POST)

    if not happy_or_sad.is_valid():
        messages.success(request, 'Numero invalido')
        return HttpResponseRedirect('/happynumbers/')
    result = happy_numbers(happy_or_sad.cleaned_data['happy_or_sad'])

    messages.success(request, result)

    return HttpResponseRedirect('/happynumbers/')


def new(request):
    return render(request, 'happynumbers.html')