from flask import Blueprint

bp = Blueprint('blog', __name__)

@bp.route('/')
def index():
    return "Hello World"
