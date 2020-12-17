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

@bp.route('/show', methods=('GET', 'POST'))
def show():
    db = get_db()
    SHOW = db.execute("SELECT * FROM Wards").fetchall()
    return render_template('wards/show.html' , SHOW = SHOW)

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

@bp.route('/delete', methods=('GET', 'POST'))
def delete():
    if request.method == 'POST':
        Ward_ID = request.form['Ward_ID']
        db = get_db()

        error = None
        WARDS = db.execute(
            'SELECT * FROM Wards WHERE Ward_ID = ?', (Ward_ID,)
        ).fetchone()
        if WARDS is None:
            error = "WARD  ID : {} is not registered".format(Ward_ID)
        flash(error)
        if error is None:
            db.execute('DELETE FROM Wards WHERE Ward_ID = ?', (Ward_ID,))
            db.commit()
            return redirect(url_for('wards.home'))

    return render_template('wards/delete.html')

