from django.db import models


class Subscriber(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    email = models.EmailField(unique=True)
    birth_date = models.DateField(null=True, blank=True)

    def __str__(self):
        return self.email

class Mailing(models.Model):
    subject = models.CharField(max_length=200)
    template = models.TextField()
    send_time = models.DateTimeField()
    is_sent = models.BooleanField(default=False)

    def __str__(self):
        return self.subject

class EmailOpenTracking(models.Model):
    mailing = models.ForeignKey(Mailing, on_delete=models.CASCADE)
    subscriber = models.ForeignKey(Subscriber, on_delete=models.CASCADE)
    opened_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return '{} - {}'.format(self.subscriber.email, self.mailing.subject)
