import random
from string import hexdigits

from django.contrib.auth.models import User
from django.core.mail import send_mail
from django.shortcuts import redirect, render
from django.views.generic.edit import CreateView

from BulletinBoard import settings
from .models import BaseRegisterForm, OneTimeCode


class BaseRegisterView(CreateView):
    model = User
    form_class = BaseRegisterForm
    template_name = 'signup.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['form'] = BaseRegisterForm()
        return context

    def post(self, request, *args, **kwargs):
        form = self.form_class(request.POST)
        if form.is_valid():
            user = form.save(commit=False)  # забираем объект не сохраненной формы
            user.is_activ = False  # делаем юзера не активным и сохраняем
            user.save()
        return redirect('code', request.POST['username'])


class GetCode(CreateView):
    template_name = 'code.html'

    def get_context_data(self, **kwargs):
        name_user = self.kwargs.get('user')
        print(name_user)
        if not OneTimeCode.objects.filter(user=name_user).exists():
            code = ''.join(random.sample(hexdigits, 5))
            OneTimeCode.objects.create(user=name_user, code=code)
            user = OneTimeCode.objects.get(username=name_user)
            send_mail(
                subject=f'Код активации',
                message=f'Код активации аккаунта: {code}',
                from_email=settings.DEFAULT_FROM_EMAIL,
                recipient_list=[user.email],
            )

    def post(self, request, *args, **kwargs):
        if 'code' in request.POST:  # означает что code.html делает POST запрос
            print(request)
            user = request.path.split('/')[-1]
            if OneTimeCode.objects.filter(code=request.POST['code'], user=user).exists():
                User.objects.filter(username=user).update(is_active=True)
                OneTimeCode.objects.filter(code=request.POST['code'], user=user).delete()
            else:
                return render(self.request, 'invalid_code.html')
        return redirect('login')


class GetCode(CreateView):
    template_name = 'code.html'

    def get_context_data(self, **kwargs):
        name_user = self.kwargs.get('user')
        if not OneTimeCode.objects.filter(user=name_user).exists():
            code = ''.join(random.sample(hexdigits, 6))
            OneTimeCode.objects.create(user=name_user, code=code)
            user = User.objects.get(user=name_user)
            send_mail(
                subject=f'Код активации',
                message=f'',
                from_email=settings.DEFAULT_FROM_EMAIL,
                recipient_list=[user.email]
            )

    def post(self, request, *args, **kwargs):
        print(request.POST)
        if 'code' in request.POST:
            user = request.path.split('/')[-1]
            if OneTimeCode.objects.filter(code=request.POST['code'], user=user).exists():
                User.objects.filter(username=user).update(is_active=True)
                OneTimeCode.objects.filter(code=request.POST['code'], user=user).delete()
            else:
                return (render(self.request, 'invalid_code.html'))
        return redirect('login')
