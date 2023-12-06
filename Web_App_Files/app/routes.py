from flask import render_template, Blueprint, request
from .forms import TrigForm
from .utils import find_domain_and_range, find_asymptotes
from .visualizer import plot_function, plot_inverse_function

bp = Blueprint('main', __name__)

@bp.route('/', methods=['GET', 'POST'])
def index():
    form = TrigForm()
    plot_url = None
    domain_range = None
    asymptotes = None

    if form.validate_on_submit():
        function_name = form.function_name.data
        action = form.action.data

        if action == 'plot':
            plot_url = plot_function(function_name)
        elif action == 'inverse':
            plot_url = plot_inverse_function(function_name)
        elif action == 'domain_range':
            domain_range = find_domain_and_range(function_name)
        elif action == 'asymptotes':
            asymptotes = find_asymptotes(function_name)

    return render_template('index.html', form=form, plot_url=plot_url, domain_range=domain_range, asymptotes=asymptotes)
