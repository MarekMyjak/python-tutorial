from flask import render_template
from application.new_module import new_module


@new_module.route('/new_module')
def index():
    return render_template('new_module.html', title='New_module')
