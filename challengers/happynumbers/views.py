from django.shortcuts import render


def happynumbers(request):
    return render(request, 'happynumbers.html')