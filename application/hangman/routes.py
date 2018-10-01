from flask import render_template
from application.hangman import hangman


@hangman.route('/hangman')
def index():
    return render_template('hangman.html', title='hangman')
