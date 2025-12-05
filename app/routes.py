from flask import Blueprint, render_template, request
from flask_babel import gettext
from .services.calculator_service import is_leap_year

main_bp = Blueprint('main', __name__)


@main_bp.route('/', methods=['GET', 'POST'])
def index():
    result = None
    error = None
    year_input = ''
    if request.method == 'POST':
        year_input = request.form.get('year', '').strip()
        try:
            year = int(year_input)
            leap = is_leap_year(year)
            result = gettext('Yes') if leap else gettext('No')
        except ValueError:
            error = gettext('Invalid year. Enter a year 1 or greater')

    return render_template('index.html', title=gettext('Find out if your year is a leap year?'), result=result, error=error, year=year_input)
