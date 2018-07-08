from flask import Blueprint

main = Blueprint('index', __name__, template_folder='templates')

from application.index import routes
