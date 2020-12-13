import functools
from flask import (
    Blueprint, flash, g, redirect, render_template, request, session, url_for
)
from werkzeug.security import check_password_hash, generate_password_hash

from iq.db import get_db

bp = Blueprint('nurse', __name__, url_prefix='/nurse')




@bp.route('/home', methods=('GET', 'POST'))
def home():
    return render_template('nurse/home.html')


@bp.route('/id', methods=('GET', 'POST'))
def id():

    db = get_db()
    #count = 1
    count = db.execute("SELECT COUNT(*) FROM Nurse").fetchone()[0]
    print(count)
    
    return render_template('nurse/id.html' , (count) = (count))





@bp.route('/show', methods=('GET', 'POST'))
def show():

    db = get_db()
    SHOW = db.execute("SELECT * FROM Nurse").fetchall()
    
    
    return render_template('nurse/show.html' , (SHOW) = (SHOW))



@bp.route('/register', methods=('GET', 'POST'))
def register():
    if request.method == 'POST':
        name = request.form['name']
        
        dob= request.form['dob']

        sex =  request.form['sex']
        address  = request.form['address']
        salary  = request.form['salary']

        Ward_ID  = request.form['Ward_ID']
        
        db = get_db()
        count = db.execute("SELECT COUNT(*) FROM Nurse").fetchone()[0]
        count += 1
        print(count)

        
        error = None
        if error is None:
            db = get_db()

            db.execute('INSERT INTO Nurse (Name , DOB , Sex , Address ,   Salary , Ward_ID , N_ID) VALUES (? ,  ? , ? , ? , ? , ? , ?)',
                    (name , dob , sex , address ,   salary , Ward_ID , count)
                    )
            db.commit()
            return redirect(url_for('nurse.id'))


    return render_template('nurse/register.html')





