from django.contrib.auth.models import User
from django.core.mail import send_mail
from django.db.models.signals import m2m_changed, post_save
from django.dispatch import receiver

from BulletinBoard import settings
from board.models import Feedback, Bulletin

'''Не забыть импортировать сигналы в apps и расширить в настройки проекта 
board.apps.BoardConfig'''


@receiver(post_save, sender=Feedback)
def notifY_about_new_feedback(sender, instance, **kwargs):
    # в инстанс находится объект Feedback
    feedback = instance.id
    bulletin_id = Feedback.objects.get(id=feedback).bulletin_id
    author_id = Bulletin.objects.get(pk=bulletin_id).author_id
    email = User.objects.get(id=author_id).email

    send_mail(
        subject=f'Вам письмо',
        message=f'Ваше объяевление {Bulletin.objects.get(pk=bulletin_id).title} получило отклик',
        from_email=settings.DEFAULT_FROM_EMAIL,
        recipient_list=[email],
    )
