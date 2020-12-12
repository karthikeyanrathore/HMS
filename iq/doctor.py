import functools
from flask import (
    Blueprint, flash, g, redirect, render_template, request, session, url_for
)
from werkzeug.security import check_password_hash, generate_password_hash

from iq.db import get_db

bp = Blueprint('doctor', __name__, url_prefix='/doctor')




@bp.route('/home', methods=('GET', 'POST'))
def home():
    return render_template('doctor/home.html')







@bp.route('/register', methods=('GET', 'POST'))
def register():
    if request.method == 'POST':
        name = request.form['name']
        
        dob= request.form['dob']

        sex =  request.form['sex']
        address  = request.form['address']
        salary  = request.form['salary']
        
     
        
        error = None
        if error is None:
            db = get_db()

            db.execute('INSERT INTO Doctor (Name , DOB , Sex , Address ,   Salary) VALUES (? ,  ? , ? , ? , ?)',
                    (name , dob , sex , address ,   salary)
                    )
            db.commit()
            return redirect(url_for('doctor.home'))


    return render_template('doctor/register.html')





