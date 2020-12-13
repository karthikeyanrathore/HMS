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





@bp.route('/id', methods=('GET', 'POST'))
def id():

    db = get_db()
    #count = 1
    count = db.execute("SELECT COUNT(*) FROM Doctor").fetchone()[0]
    print(count)
    
    return render_template('doctor/id.html' , (count) = (count))






@bp.route('/show', methods=('GET', 'POST'))
def show():

    db = get_db()
    SHOW = db.execute("SELECT * FROM Doctor").fetchall()
    
    
    return render_template('doctor/show.html' , (SHOW) = (SHOW))





@bp.route('/register', methods=('GET', 'POST'))
def register():
    if request.method == 'POST':
        name = request.form['name']
        
        dob= request.form['dob']

        sex =  request.form['sex']
        address  = request.form['address']
        salary  = request.form['salary']

        Dept_ID = request.form['Dept_ID']
        
     
        
        error = None
        if error is None:
            db = get_db()

            db.execute('INSERT INTO Doctor (Name , DOB , Sex , Address ,   Salary , Dept_ID) VALUES (? ,  ? , ? , ? , ? , ?)',
                    (name , dob , sex , address ,   salary , Dept_ID)
                    )
            db.commit()
            return redirect(url_for('doctor.id'))


    return render_template('doctor/register.html')





