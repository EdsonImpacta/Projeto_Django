from django.shortcuts import render
from django.http import HttpResponse


def OlaMundo(request):
    return HttpResponse("Ola Mundo!")
# Create your views here.
