from django.http import HttpResponse
from django.shortcuts import render


def index(request):
    return HttpResponse('<h1> Привет мир </h1>')

def categories(request):
    return HttpResponse('<h3> Категории </h3>')

