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
    
    
    return render_template('department/show.html' , (SHOW) = (SHOW))





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





