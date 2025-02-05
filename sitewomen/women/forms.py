
from unittest.util import _MAX_LENGTH
from django import forms
from django.core.validators import BaseValidator, MaxLengthValidator, MinLengthValidator
from django.utils.deconstruct import deconstructible
from django.core.exceptions import ValidationError
from .models import Category, Husband


@deconstructible
class RussianValidator:
    ALLOWED_CHARS = "АБВГДЕЁЖЗИЙКЛМНОПРСТУФХЦЧШЩЬЫЪЭЮЯабвгдеёжзийклмнопрстуфхцчшщъыьэюя1234567890- "
    code = 'russian'

    def __init__(self, message=None):
        self.message = message if message else "Должны присутсвовать только русские символы, дефис, пробел"
    
    def __call__(self, value, *args, **kwds):
        if not (set(value) <= set(self.ALLOWED_CHARS)):
            raise forms.ValidationError(self.message, code=self.code)



class AddPostForm(forms.Form):
    title = forms.CharField(max_length=255, min_length=7, label='Заголовок', 
                            widget=forms.TextInput(attrs={'class': 'form-input'}),
                            validators=[RussianValidator()],
                            error_messages={
                                'min_length': 'слишком короткий заголовок',
                                'required': 'Без заголовка никак'}
                            )
    slug = forms.SlugField(max_length=255, label='URL', 
                           validators=[
                               MinLengthValidator(5),
                               MaxLengthValidator(100)
                           ])
    content = forms.CharField(widget=forms.Textarea(attrs={'cols':50, 'rows':5}), required=False, label='Содержание')
    is_published = forms.BooleanField(required=False, label='Статус')
    cat = forms.ModelChoiceField(queryset=Category.objects.all(), label='Категория', empty_label="Категория не выбрана")
    husband = forms.ModelChoiceField(queryset=Husband.objects.all(), required=False, label='Муж', empty_label="не замужем")

    def clean_title(self):
        title = self.cleaned_data['title']
        ALLOWED_CHARS = "АБВГДЕЁЖЗИЙКЛМНОПРСТУФХЦЧШЩЬЫЪЭЮЯабвгдеёжзийклмнопрстуфхцчшщъыьэюя1234567890- "
        if not (set(title) <= set(ALLOWED_CHARS)):
            raise forms.ValidationError("Должны присутсвовать только русские символы, дефис, пробел") 

