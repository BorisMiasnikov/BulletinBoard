from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render
from django.views.generic import ListView, DetailView, CreateView
from django.urls import reverse_lazy

from .forms import BulletinForm
from .models import Bulletin


# Нужно показывать объявления, создавать объявления, оставлять отклики, принимать или не принимать отклики автором объявления
# не авторизованные пользователи могут только просматривать объявления



class BulletinList(ListView):
    model = Bulletin
    ordering = '-date_in'
    template_name = 'bulletins.html'
    context_object_name = 'bulletins'
    paginate_by = 10


class BulletinDetail(DetailView):
    model = Bulletin
    template_name = 'bulletin.html'
    context_object_name = 'bulletin'


#создание постов нужно делать через формы, это связано с методом POST
class BulletinCreate(LoginRequiredMixin, CreateView):
    form_class = BulletinForm
    model = Bulletin
    template_name = 'bulletin_cteate.html'
    success_url = reverse_lazy('Bulletin_list')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        print(context)
        return context





