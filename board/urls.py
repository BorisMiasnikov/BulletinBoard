from django.urls import path
from .views import BulletinList, BulletinDetail, BulletinCreate, Profile, FeedbackCreate, FeedbackList, accept, refuze

urlpatterns = [
    path('', BulletinList.as_view(), name='Bulletin_list'),
    path('/<int:pk>/', BulletinDetail.as_view(), name='Bulletin_detail'),
    path('/create/', BulletinCreate.as_view(), name='Bulletin_create'),
    path('profile/', Profile.as_view(), name='Profile'),
    path('/<int:pk>/feedback', FeedbackCreate.as_view(), name='Feedback_create'),
    path('/<int:pk>/feedbacks', FeedbackList.as_view(), name='Feedback_list'),
    path('feedback/<int:pk>/accept', accept, name='Accept'),
    path('feedback/<int:pk>/refuze', refuze, name='Refuze'),

]
