from django.contrib.auth.models import User
from django.core.mail import send_mail
from django.db.models.signals import m2m_changed, post_save
from django.dispatch import receiver

from BulletinBoard import settings
from board.models import Feedback, Bulletin

'''Не забыть импортировать сигналы в apps и расширить в настройки проекта 
board.apps.BoardConfig'''


@receiver(post_save, sender=Feedback)
def notify_about_new_feedback( instance, created, **kwargs):
        # в инстанс находится объект Feedback
    if created:
        email = instance.bulletin.author.email
        send_mail(
            subject=f'Вам письмо',
            message=f'Ваше объяевление {instance.bulletin.title} получило отклик',
            from_email=settings.DEFAULT_FROM_EMAIL,
            recipient_list=[email],
        )
