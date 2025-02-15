from django.core.mail import send_mail
from celery import shared_task
from .models import Mailing, Subscriber


@shared_task
def send_mailing(mailing_id):
    mailing = Mailing.objects.get(id=mailing_id)
    subscribers = Subscriber.objects.all()

    for subscriber in subscribers:
        message = mailing.template.replace("{{ first_name }}", subscriber.first_name)
        send_mail(
            mailing.subject,
            message,
            'from@example.com',
            [subscriber.email],
            fail_silently=False,
        )
    mailing.is_sent = True
    mailing.save()