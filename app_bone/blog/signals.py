from flask import current_app
from app_bone import mail


# from flask_mail import Message
#
#
def send_mail(sender, **kwargs):
    if type(sender) != type(current_app._get_current_object()):
        pass
#         my_mail.delay()
#
#
# @app_celery.task
# def my_mail():
#     msg = Message("Ping!",
#                   sender="admin.ping",
#                   recipients=['poya_kob@live.com'])
#     msg.body = "hello poya"
#     mail.send(msg)
