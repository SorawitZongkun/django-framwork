from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.


def index(request):
    # return HttpResponse('OMG')
    name = 'Hanni'
    age = 17
    return render(request, 'index.html', {"name": name, "age": age})


def about(request):
    return render(request, 'about.html')


def form(request):
    return render(request, 'form.html')
