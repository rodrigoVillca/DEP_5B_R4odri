from flask import (
    Blueprint, flash, g, redirect, render_template, request, url_for
)
from werkzeug.exceptions import abort

from tracks.db import get_db

bp = Blueprint('valores', __name__, url_prefix="/valores")

@bp.route('/')
def index():
    db = get_db()
    valores = db.execute('SELECT value FROM sensor_values').fetchall()
    return render_template('valores/index.html', valores=valores)
