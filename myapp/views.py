from django.shortcuts import render
from django.http import HttpResponse
from myapp.models import Person

# Create your views here.


def index(request):
    # return HttpResponse('OMG')
    all_person = Person.objects.all()
    # all_person = Person.objects.filter(age=25)
    return render(request, 'index.html', {"all_person": all_person})


def about(request):
    return render(request, 'about.html')


def form(request):
    return render(request, 'form.html')
