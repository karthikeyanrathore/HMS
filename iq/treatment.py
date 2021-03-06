import functools
from flask import (
    Blueprint, flash, g, redirect, render_template, request, session, url_for
)
from werkzeug.security import check_password_hash, generate_password_hash
from iq.db import get_db
bp = Blueprint('treatment', __name__, url_prefix='/treatment')

@bp.route('/home', methods=('GET', 'POST'))
def home():
    return render_template('treatment/home.html')


@bp.route('/show', methods=('GET', 'POST'))
def show():
    db = get_db()
    SHOW = db.execute("SELECT * FROM Treatment").fetchall()
    return render_template('treatment/show.html' , SHOW = SHOW)

@bp.route('/register', methods=('GET', 'POST'))
def register():
    if request.method == 'POST':
        name = request.form['name']
        cost = request.form['cost']
        
        error = None
        if error is None:
            db = get_db()
            db.execute('INSERT INTO Treatment (Name , Cost) VALUES (?, ?)',
                    (name, cost)
                    )
            db.commit()
            return redirect(url_for('treatment.home'))

    return render_template('treatment/register.html')

@bp.route('/delete', methods=('GET', 'POST'))
def delete():
    if request.method == 'POST':
        T_ID = request.form['T_ID']
        db = get_db()

        error = None
        TP = db.execute(
            'SELECT * FROM Treatment WHERE T_ID = ?', (T_ID,)
        ).fetchone()
        if TP is None:
            error = "Treatment  ID : {} is not registered".format(T_ID)
        flash(error)
        if error is None:
            db.execute('DELETE FROM Treatment WHERE T_ID = ?', (T_ID,))
            db.commit()
            return redirect(url_for('treatment.home'))

    return render_template('treatment/delete.html')


