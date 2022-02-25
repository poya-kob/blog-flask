from flask import current_app
from app_bone import mail, celery
from flask_mail import Message


@celery.task
def my_mail():
    msg = Message("Ping!",
                  sender='django.code.decoders@gmail.com',
                  recipients=['poya_kob@live.com'])
    msg.body = "hello poya"
    mail.send(msg)


def send_mail(sender, **kwargs):
    if type(sender) != type(current_app._get_current_object()):
        my_mail.delay()
