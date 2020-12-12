import functools
from flask import (
    Blueprint, flash, g, redirect, render_template, request, session, url_for
)
from werkzeug.security import check_password_hash, generate_password_hash

from iq.db import get_db

bp = Blueprint('patient', __name__, url_prefix='/patient')




@bp.route('/home', methods=('GET', 'POST'))
def home():
    return render_template('patient/home.html')







@bp.route('/register', methods=('GET', 'POST'))
def register():
    if request.method == 'POST':
        name = request.form['name']
        
        dob= request.form['dob']

        sex =  request.form['sex']
        address  = request.form['address']
        
        
        from datetime import date
        today = date.today()

        # dd/mm/YY
        date_admit = today.strftime("%d/%m/%Y")
        #print("d1 =", d1)
        
        error = None
        if error is None:
            db = get_db()

            db.execute('INSERT INTO Patient (Name , DOB , Sex , Address ,   Date_admit) VALUES (? ,  ? , ? , ? , ?)',
                    (name , dob , sex , address ,   date_admit)
                    )
            db.commit()
            return redirect(url_for('patient.home'))


    return render_template('patient/register.html')





