from django.urls import path
from .views import BulletinList, BulletinDetail, BulletinCreate

urlpatterns = [
    path('bulletins/', BulletinList.as_view(), name='Bulletin_list'),
    path('bulletins/<int:pk>/', BulletinDetail.as_view(), name='Bulletin_detail'),
    path('bulletins/create/', BulletinCreate.as_view(), name='Bulletin_create'),

]
