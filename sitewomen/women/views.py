from django.http import Http404, HttpResponse, HttpResponseNotFound, HttpResponseRedirect
from django.shortcuts import redirect, render
from django.urls import reverse


def index(request):
    return HttpResponse('<h1> Привет мир </h1>')

def categories(request, cat_id):
    return HttpResponse(f'<h3> Категории </h3><p>id: {cat_id}</p>')

def categories_by_slug(request, cat_slug):
    return HttpResponse(f'<h2> Категории </h2><p>slug: {cat_slug}</p>')

def archive(request, year):
    if year > 2023:
        uri = reverse('cats', args=('music', ))
        return HttpResponseRedirect('/')
    return HttpResponse(f'<h2> Архив по годам </h2><p>{year}</p>')

def page_not_found(request, exception):
    return HttpResponseNotFound("<h1>Страница не найдена</h1>")