from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render
from django.contrib import messages

from challengers.fizzbuzz.form import NumberForm

from challengers.fizzbuzz.model.fizzbuzzCode import sayFizzBuzz


def fizzbuzz(request):

    if request.method == 'POST':
        return create(request)
    else:
        return render(request, 'fizzbuzz.html')


def create(request):

    numberForm = NumberForm(request.POST)

    if not numberForm.is_valid():
        return render(request, 'index.html')

    say = sayFizzBuzz(numberForm.cleaned_data['number'])

    messages.success(request, f'{say}')

    return HttpResponseRedirect('/fizzbuzz/')
