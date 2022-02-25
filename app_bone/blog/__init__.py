from flask import Blueprint
from .time_context_prossessor import time_context

blog = Blueprint('blog', __name__, template_folder='../../templates')
# blog.app_context_processor(time_context)
