from django.contrib import messages
from django.http import HttpResponseRedirect
from django.shortcuts import render

from challengers.fizzbuzz.form import NumberForm
from challengers.fizzbuzz.model.fizzbuzzCode import sayFizzBuzz


def fizzbuzz(request):
    if request.method == 'POST':
        return create(request)
    else:
        return new(request)


def create(request):

    numberForm = NumberForm(request.POST)

    if not numberForm.is_valid():
        messages.success(request, 'Informe um numero valido')
        return HttpResponseRedirect('/fizzbuzz/')

    say = sayFizzBuzz(numberForm.cleaned_data['number'])

    messages.success(request, f'{say}')

    return HttpResponseRedirect('/fizzbuzz/')


def new(request):
    return render(request, 'fizzbuzz.html')