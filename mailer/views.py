from django.contrib import messages
from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt
from django.utils import timezone
from .models import EmailOpenTracking, Mailing, Subscriber
from .tasks import send_mailing
from .forms import MailingForm


def create_mailing(request):
    if request.method == 'POST':
        form = MailingForm(request.POST)
        if form.is_valid():
            mailing = form.save()
            send_time = mailing.send_time
            now = timezone.now()
            if send_time > now:
                send_mailing.apply_async((mailing.id,), eta=send_time)
            else:
                send_mailing.delay(mailing.id)
            messages.success(request, 'Mailing list created!')
            return redirect('mailing_list')
        else:
            messages.error(request, 'Error when creating a mailing list!')

    else:
        form = MailingForm()
    return render(request, 'mailer/mailing_form.html', {'form': form})

@csrf_exempt
def track_open(request, mailing_id, subscriber_id):
    mailing = get_object_or_404(Mailing, id=mailing_id)
    subscriber = get_object_or_404(Subscriber, id=subscriber_id)
    EmailOpenTracking.track_open(mailing, subscriber)
    return HttpResponse(status=200)

def mailing_list(request):
    mailings = Mailing.objects.all()
    return render(request, 'mailer/mailing_list.html', {'mailings': mailings})