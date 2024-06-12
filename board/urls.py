from django.urls import path
from .views import BulletinList

urlpatterns = [
    path('bulletins/', BulletinList.as_view(), name='Bulletin_list')
]