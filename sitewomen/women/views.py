from django.http import Http404, HttpResponse, HttpResponseNotFound, HttpResponseRedirect
from django.shortcuts import redirect, render
from django.urls import reverse
from django.template.loader import render_to_string

menu= [{'title': 'О сайте', 'url_name': 'about'},
        {'title': "Добавить статью", 'url_name': 'addpage'},
        {'title': "Обратная связь", 'url_name': 'contact'},
        {'title': "Войти", 'url_name': 'login'},]

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
    data = {
        'title': 'главная ',
          'menu': menu,
          'float': 28.56,
          'lst': [1, 2, 'abc', True],
          'set': {1, 2, 3, 4, 5, 7},
          'posts': posts,
          'obj': MyClass(10,20),
          }
   
    return render(request, 'women/index.html', context=data)

def about(request):
    return render(request, 'women/about.html', {'title': 'О сайте', 'menu': menu})

def show_post(request, post_id):
    return HttpResponse(f'Отображение статьи с id = {post_id}')

def page_not_found(request, exception):
    return HttpResponseNotFound("<h1>Страница не найдена</h1>")

def addpage(request):
    return HttpResponse("ДОбавление статьи")

def contact(request):
    return HttpResponse("Обратная связь")

def login(request):
    return HttpResponse("Авторизация")