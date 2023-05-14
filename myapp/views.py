from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def index(request):
    return HttpResponse('Hype Boy')

def about(request):
    return HttpResponse('OMG')

def form(request):
    return HttpResponse('Ditto')