class Config():
    SQLALCHEMY_DATABASE_URI = 'sqlite:///blog.sqlite'
    SQLALCHEMY_TRACK_MODIFICATIONS = True
    SECRET_KEY = b'\x1f\xb4!\xce\xe0\xbaZ\xa5|r:!l\xd42\xfd\x16\xa5\xb6\xa7O\xac\xba\x97'
    MAIL_SERVER = 'smtp.gmail.com'
    MAIL_PORT = 587
    MAIL_USE_TLS = True
    MAIL_USERNAME = 'django.code.decoders@gmail.com'
    MAIL_PASSWORD = 'D8ttEA9GDaQda4B'
    CELERY_BROKER_URL = 'redis://localhost:6379/0'
    CELERY_RESULT_BACKEND = 'redis://localhost:6379/0'

    # STATIC_FOLDER = '../static'
