from app_bone import celery
from app_bone import create_app
from app_bone.celery_conf import init_celery
app = create_app()
init_celery(celery, app)
