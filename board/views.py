from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.models import User
from django.shortcuts import render
from django.views.generic import ListView, DetailView, CreateView
from django.urls import reverse_lazy

from .filters import BulletinFilter
from .forms import BulletinForm, FeedbackCreateForm
from .models import Bulletin, Feedback


# Нужно показывать объявления, создавать объявления, оставлять отклики, принимать или не принимать отклики автором объявления
# не авторизованные пользователи могут только просматривать объявления

''' В джанго реализованы методы доступа к авторизованному пользователю из коробки 
{{ iser.id }} - идентификатор пользователя из шаблона
request.user.id - доступ к id пользователя в представлениях-функциях
self.request.user.id - доступ к id пользователя в представлениях-классах'''



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


class Profile(LoginRequiredMixin, ListView):
    model = User
    template_name = 'profile.html'

    def get_queryset(self):
        queryset = super().get_queryset()
        self.user = User.objects
        # self.category = get_object_or_404(Category, id = self.kwargs['pk'])
        # queryset = Post.objects.filter(category=self.category).order_by('-data_in')
        print(queryset)
        print(self.request.user)
        return queryset

    def get_context_data(self, **kwargs):
        print(self.request.user.id)
        print(kwargs)
        pk_user = self.request.user.id
        context = super().get_context_data(**kwargs)
        context['bulletins'] = Bulletin.objects.filter(author = pk_user)
        print(context)
        return context


class FeedbackCreate(LoginRequiredMixin, CreateView):
    form_class = FeedbackCreateForm
    model = Feedback
    template_name = 'feedback_cteate.html'
    success_url = reverse_lazy('Bulletin_list')

    def form_valid(self, form):
        # bulletin_pk = self.request.path.split('/')[-2] #Это один из способов получения из адресной строки
        bulletin_pk = self.kwargs.get('pk') #Это другой способ получения ид, без адресной строки, но как?...
        post = form.save(commit=False)
        post.author = self.request.user
        post.bulletin_id = bulletin_pk
        post.save()
        return super().form_valid(form)



class FeedbackList(LoginRequiredMixin, ListView):
    model = Feedback
    template_name = 'feedbacks.html'
    context_object_name = 'feedbacks'

    def get_queryset(self,**kwargs):
        # Получаем обычный queryser список объектов модели
        queryset = super().get_queryset()
        return queryset.filter(bulletin_id= self.request.path.split('/')[-2])

# @login_required
# def accept(request, pk):
#     user = request.user
#     category = Category.objects.get(id=pk)
#     category.subscriber.add(user)
#
#     massage = 'Вы подтвердили отклик'
#     return render(request, 'subscriber.html', {'category':category, 'massage':massage})
#
#
# @login_required
# def refuze(request, pk):
#     user = request.user
#     category = Category.objects.get(id=pk)
#     category.subscriber.add(user)
#
#     massage = 'Это успешная подписка на'
#     return render(request, 'subscriber.html', {'category':category, 'massage':massage})
#
