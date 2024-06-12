from django.shortcuts import render
from django.views.generic import ListView
from .models import Bulletin



class BulletinList(ListView):
    model = Bulletin
    # ordering = '-date'
    template_name = 'bulletins.html'
    context_object_name = 'bulletins'
    paginate_by = 10




