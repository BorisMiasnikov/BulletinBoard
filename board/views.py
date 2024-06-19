from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.models import User
from django.shortcuts import render
from django.views.generic import ListView, DetailView, CreateView
from django.urls import reverse_lazy

from .forms import BulletinForm, FeedbackForm
from .models import Bulletin, Feedback


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


class Profile(DetailView):
    model = User
    template_name = 'profile.html'


    def get_context_data(self, **kwargs):
        pk_user = self.kwargs.get('pk')
        context = super().get_context_data(**kwargs)
        context['bulletins'] = Bulletin.objects.filter(author = pk_user)
        return context


class FeedbackCreate(LoginRequiredMixin, CreateView):
    form_class = FeedbackForm
    model = Feedback
    template_name = 'feedback_cteate.html'
    success_url = reverse_lazy('Bulletin_list')

    def form_valid(self, form):
        print(form.POST)

        bull_pk = form.path.split('/')[-2]
        print(bull_pk)

        post = form.save(commit=False)
        post.author = self.request.user.author
        post.bulletin = bull_pk
        post.save()
        return super().form_valid(form)


