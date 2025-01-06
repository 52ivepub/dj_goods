from django.http import HttpResponse
from django.shortcuts import render


def index(request):
    return HttpResponse('<h1> Привет мир </h1>')

def categories(request, cat_id):
    return HttpResponse(f'<h3> Категории </h3><p>id: {cat_id}</p>')

def categories_by_slug(request, cat_slug):
    return HttpResponse(f'<h2> Категории </h2><p>slug: {cat_slug}</p>')

def archive(request, year):
    return HttpResponse(f'<h2> Архив по годам </h2><p>{year}</p>')