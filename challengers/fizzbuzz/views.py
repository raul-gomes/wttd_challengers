from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render
from django.contrib import messages

from challengers.fizzbuzz.form import NumberForm

from challengers.fizzbuzz.model._fizzbuzz import sayFizzBuzz


def fizzbuzz(request):

    numberForm = NumberForm(request.POST)

    say = sayFizzBuzz(numberForm.cleaned_data)

    messages.success(request, say)

    return HttpResponseRedirect('/fizzbuzz/')