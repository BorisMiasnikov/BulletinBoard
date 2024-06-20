from django_filters import FilterSet
from django import forms

from .models import Bulletin

class BulletinFilter(FilterSet):
    class Meta:
        model = Bulletin
        fields = {
            'title': ['icontains'],
            'author': ['exact'],
        }