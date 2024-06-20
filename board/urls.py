from django.urls import path
from .views import BulletinList, BulletinDetail, BulletinCreate, Profile, FeedbackCreate, FeedbackList

urlpatterns = [
    path('bulletins/', BulletinList.as_view(), name='Bulletin_list'),
    path('bulletins/<int:pk>/', BulletinDetail.as_view(), name='Bulletin_detail'),
    path('bulletins/create/', BulletinCreate.as_view(), name='Bulletin_create'),
    path('profile/', Profile.as_view(), name='Profile'),
    path('bulletins/<int:pk>/feedback', FeedbackCreate.as_view(), name='Feedback_create'),
    path('bulletins/<int:pk>/feedbacks', FeedbackList.as_view(), name='Feedback_list'),

]
