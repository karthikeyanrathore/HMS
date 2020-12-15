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


@bp.route('/update', methods=('GET', 'POST'))
def update():
    return render_template('doctor/update.html')



@bp.route('/id', methods=('GET', 'POST'))
def id():

    db = get_db()
    #count = 1
    count = db.execute("SELECT COUNT(*) FROM Doctor").fetchone()[0]
    print(count)
    
    
    return render_template('doctor/id.html' , count = count)






@bp.route('/show', methods=('GET', 'POST'))
def show():

    db = get_db()
    SHOW = db.execute("SELECT * FROM Doctor").fetchall()
    FF = db.execute("SELECT * FROM Doctor_Contact  ").fetchall()

    GG = db.execute("SELECT * FROM Department  ").fetchall()
    
    
    return render_template('doctor/show.html' , SHOW = SHOW  , FF = FF , GG = GG)





@bp.route('/register', methods=('GET', 'POST'))
def register():
    if request.method == 'POST':
        name = request.form['name']
        
        dob= request.form['dob']

        sex =  request.form['sex']
        address  = request.form['address']
        salary  = request.form['salary']

        Dept_ID = request.form['Dept_ID']
        Contact = request.form['Contact']
        
        db = get_db()
        error = None
        if len(str(Contact)) != 10:
            error = "Contact No. Should be 10 Digit Number"

        flash(error)
       
        department = db.execute(
            'SELECT * FROM Department WHERE Dept_ID = ?', (Dept_ID,)
        ).fetchone()

        if department is None:
            error = "Department  ID : {} is not registered".format(Dept_ID)

        flash(error)

        if error is None:

            count = db.execute("SELECT COUNT(*) FROM Doctor").fetchone()[0]
            count += 1
            print(count)
            db.execute("INSERT INTO Doctor_Contact(D_ID , Contact) VALUES(? , ?)",
            (count , Contact)

            )

            db.execute('INSERT INTO Doctor (Name , DOB , Sex , Address ,   Salary , Dept_ID) VALUES (? ,  ? , ? , ? , ? , ?)',
                    (name , dob , sex , address ,   salary , Dept_ID)
                    )
            db.commit()
            return redirect(url_for('doctor.id'))


    return render_template('doctor/register.html')






@bp.route('/insert', methods=('GET', 'POST'))
def insert():
    if request.method == 'POST':
        id = request.form['id']
        Contact = request.form['Contact']
        db = get_db()

        error = None
        name = db.execute(
            'SELECT * FROM Doctor WHERE D_ID = ?', (id,)
        ).fetchone()

        if name is None:
            error = "Doctor id :{} is not registered".format(id)

        flash(error)

        if error is None:
            db.execute("INSERT INTO Doctor_Contact(D_ID , Contact) VALUES(? , ?)",
                (id , Contact)

                )

            db.commit()
            #Select SUM(cost)  from treatment where tid in (select tid from bill where pid = ?)

            
            return redirect(url_for('doctor.home'))
    
    return render_template('doctor/insert.html')
