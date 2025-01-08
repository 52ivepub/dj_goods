from django.http import Http404, HttpResponse, HttpResponseNotFound, HttpResponseRedirect
from django.shortcuts import redirect, render
from django.urls import reverse
from django.template.loader import render_to_string

menu= ['О сайте', "Добавить статью", "Обратная связь", "Войти"]

class MyClass:
    def __init__(self, a, b):
        self.a = a
        self.b = b


def index(request):
    # t = render_to_string('women/index.html')
    # return HttpResponse(t)
    posts = [{'id':1, 'name': 'sunday'},
            {'id':2, 'name': 'friday'},
            {'id':3, 'name': 'monday'}]
    data = []
    return render(request, 'women/index.html', context=posts)

def about(request):
    return render(request, 'women/about.html', {'title': 'О сайте',})

def show_post(request, post_id):
    return HttpResponse(f'Отображение статьи с id = {post_id}')

def page_not_found(request, exception):
    return HttpResponseNotFound("<h1>Страница не найдена</h1>")