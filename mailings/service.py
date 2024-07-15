import smtplib
from datetime import datetime

import pytz
from apscheduler.schedulers.background import BackgroundScheduler
from django.core.mail import send_mail

from config import settings
from mailings.models import Mailings, Messages, Сhance


def start():
    scheduler = BackgroundScheduler()
    scheduler.add_job(send_mailing, 'interval', days=30)
    scheduler.start()


def send_mailing():
    zone = pytz.timezone(settings.TIME_ZONE)
    current_datetime = datetime.now(zone)

    # проверка статуса активных рассылок  и если дата завершения прошла меняем статус на завершенную
    for mailing in Mailings.objects.all():
        if mailing.date - current_datetime < mailing.date_end:
            mailing.status = [('завершено', 'Завершено')]
            mailing.save()
    # создание объекта с применением фильтра
    mailings = Mailings.objects.filter(date__lte=current_datetime).filter(
        status__in=[('начато', 'Начато')])

    messages = Messages.objects.all()
    for mailing in mailings:
        recipient_list = [client.email for client in mailing.clients.all()]
        server_response = ''
        status = False
        try:
            send_mail(
                subject=messages.theme,
                message=messages.body,
                from_email=settings.EMAIL_HOST_USER,
                recipient_list=recipient_list
            )
            server_response = 'Рассылка выполнена'
            status = True
        except smtplib.SMTPException as e:
            server_response = 'Произошла ошибка'
            status = False
        finally:
            chance = Сhance(status=status, response=server_response, date=current_datetime, mailing=mailing)
            chance.save()
