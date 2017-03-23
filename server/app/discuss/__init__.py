from flask import Blueprint

discuss = Blueprint('discuss',__name__)

from . import views,errors
