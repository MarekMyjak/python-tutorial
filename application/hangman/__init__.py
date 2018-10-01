from flask import Blueprint

hangman = Blueprint('hangman', __name__, template_folder='templates')

from application.hangman import routes
