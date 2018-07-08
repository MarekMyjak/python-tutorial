from flask import Blueprint

animals = Blueprint('animals', __name__, template_folder='templates')

from application.animals import routes
