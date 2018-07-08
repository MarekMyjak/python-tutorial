from flask import Blueprint

new_module = Blueprint('new_module', __name__, template_folder='templates')

from application.new_module import routes
