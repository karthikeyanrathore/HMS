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



@bp.route('/id', methods=('GET', 'POST'))
def id():

    db = get_db()
    #count = 1
    count = db.execute("SELECT COUNT(*) FROM Patient").fetchone()[0]
    print(count)
    
    return render_template('patient/id.html' , (count) = (count))




@bp.route('/show', methods=('GET', 'POST'))
def show():

    db = get_db()
    SHOW = db.execute("SELECT * FROM Patient").fetchall()
    
    
    return render_template('patient/show.html' , (SHOW) = (SHOW))




@bp.route('/register', methods=('GET', 'POST'))
def register():
    if request.method == 'POST':
        name = request.form['name']
        
        dob= request.form['dob']

        sex =  request.form['sex']
        address  = request.form['address']
        Ward_ID  = request.form['Ward_ID']
        D_ID = request.form['D_ID']
        
        #from datetime import date
        #today = date.today()

        # dd/mm/YY
        #date_admit = today.strftime("%d/%m/%Y")
        #print("d1 =", d1)
        
        error = None
        if error is None:
            db = get_db()

            db.execute('INSERT INTO Patient (Name , DOB , Sex , Address ,    Ward_ID , D_ID) VALUES (? ,   ? , ? , ? , ? , ?)',
                    (name , dob , sex , address ,     Ward_ID , D_ID)
                    )
            db.commit()
    
            return redirect(url_for('patient.id'))


    return render_template('patient/register.html')





