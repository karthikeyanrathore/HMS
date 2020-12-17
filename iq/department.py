import functools
from flask import (
    Blueprint, flash, g, redirect, render_template, request, session, url_for
)
from werkzeug.security import check_password_hash, generate_password_hash
from iq.db import get_db
bp = Blueprint('department', __name__, url_prefix='/department')

@bp.route('/home', methods=('GET', 'POST'))
def home():
    return render_template('department/home.html')

@bp.route('/show', methods=('GET', 'POST'))
def show():
    db = get_db()
    SHOW = db.execute("SELECT * FROM Department").fetchall()
    return render_template('department/show.html' , SHOW = SHOW)

@bp.route('/register', methods=('GET', 'POST'))
def register():
    if request.method == 'POST':
        name = request.form['name']
        error = None
        if error is None:
            db = get_db()
            db.execute('INSERT INTO Department (Name) VALUES (?)',
                    (name, )
                    )
            db.commit()
            return redirect(url_for('department.home'))

    return render_template('department/register.html')

@bp.route('/display', methods=('GET', 'POST'))
def display():
    if request.method == 'POST':
        Dept_ID = request.form['Dept_ID']
        db = get_db()
        error = None
        dep = db.execute(
            'SELECT * FROM Department WHERE Dept_ID = ?', (Dept_ID,)
        ).fetchone()
        if dep is None:
            error = "Department  ID : {} is not registered".format(Dept_ID)
        flash(error)

        if error is None:
            FF = db.execute('SELECT * FROM Doctor WHERE Dept_ID = ?' , (Dept_ID , )).fetchall()
            return render_template('department/all.html' , FF = FF)

        
    return render_template('department/display.html' )

@bp.route('/delete', methods=('GET', 'POST'))
def delete():
    if request.method == 'POST':
        Dept_ID = request.form['Dept_ID']
        db = get_db()

        error = None
        dep = db.execute(
            'SELECT * FROM Department WHERE Dept_ID = ?', (Dept_ID,)
        ).fetchone()
        if dep is None:
            error = "Department  ID : {} is not registered".format(Dept_ID)
        flash(error)
        if error is None:
            db.execute('DELETE FROM Department WHERE Dept_ID = ?', (Dept_ID,))
            db.commit()
            return redirect(url_for('department.home'))

    return render_template('department/delete.html')



