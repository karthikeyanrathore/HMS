import functools
from flask import (
    Blueprint, flash, g, redirect, render_template, request, session, url_for
)
from werkzeug.security import check_password_hash, generate_password_hash

from iq.db import get_db

bp = Blueprint('wards', __name__, url_prefix='/wards')




@bp.route('/home', methods=('GET', 'POST'))
def home():
    return render_template('wards/home.html')







@bp.route('/register', methods=('GET', 'POST'))
def register():
    if request.method == 'POST':
        room_type = request.form['room_type']
        
        error = None
        if error is None:
            db = get_db()

            db.execute('INSERT INTO Wards (Room_type) VALUES (?)',
                    (room_type ,)
                    )
            db.commit()
            return redirect(url_for('wards.home'))


    return render_template('wards/register.html')





