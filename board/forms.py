from django import forms
from .models import Bulletin, Feedback


class BulletinForm(forms.ModelForm):
    class Meta:
        model = Bulletin
        fields = [
            'title',
            'text',
            'category',
            'author',
        ]
        labels = {
            'title':'Заголовок',
            'text':"Содержание",
            'category':"Категория",
            'author':"Автор", #пока не настроил автоматическое добавление авторов - оставить
        }
        widgets = {
            'title': forms.Textarea(attrs={'class': 'form-text', 'cols': 70, 'rows': 3}),
            'text': forms.Textarea(attrs={'class': 'form-text', 'cols': 70, 'rows': 10}),
        }


class FeedbackCreateForm(forms.ModelForm):
    class Meta:
        model = Feedback
        fields = [
            'text',
        ]
        labels = {
            'text':"Содержание",
        }
        widgets = {
            'title': forms.Textarea(attrs={'class': 'form-text', 'cols': 70, 'rows': 3}),
            'text': forms.Textarea(attrs={'class': 'form-text', 'cols': 70, 'rows': 10}),
        }