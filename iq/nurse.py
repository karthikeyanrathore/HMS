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
    
    return render_template('nurse/id.html' , count = count)




@bp.route('/update', methods=('GET', 'POST'))
def update():
    return render_template('nurse/update.html')


@bp.route('/show', methods=('GET', 'POST'))
def show():

    db = get_db()
    SHOW = db.execute("SELECT * FROM Nurse").fetchall()
    FF = db.execute("SELECT * FROM Nurse_Contact  ").fetchall()
    GG = db.execute("SELECT * FROM Wards  ").fetchall()
    
    
    return render_template('nurse/show.html' , SHOW = SHOW , FF = FF , GG = GG)



@bp.route('/register', methods=('GET', 'POST'))
def register():
    if request.method == 'POST':
        name = request.form['name']
        
        dob= request.form['dob']

        sex =  request.form['sex']
        address  = request.form['address']
        salary  = request.form['salary']

        Ward_ID  = request.form['Ward_ID']

        Contact = request.form['Contact']
      

        
        error = None
        if error is None:
            db = get_db()
            count = db.execute("SELECT COUNT(*) FROM Nurse").fetchone()[0]
            count += 1
            print(count)

            db.execute("INSERT INTO Nurse_Contact(N_ID , Contact , Ward_ID) VALUES(? , ? , ?)",
                (count , Contact , Ward_ID)

                )



            #db = get_db()

            db.execute('INSERT INTO Nurse (Name , DOB , Sex , Address ,   Salary , Ward_ID , N_ID) VALUES (? ,  ? , ? , ? , ? , ? , ?)',
                    (name , dob , sex , address ,   salary , Ward_ID , count)
                    )
            db.commit()
            return redirect(url_for('nurse.id'))


    return render_template('nurse/register.html')






@bp.route('/insert', methods=('GET', 'POST'))
def insert():
    if request.method == 'POST':
        id = request.form['id']
        Contact = request.form['Contact']
        Ward_ID  = request.form['Ward_ID']

        db = get_db()
        db.execute("INSERT INTO Nurse_Contact(N_ID , Contact , Ward_ID) VALUES(? , ? , ?)",
            (id , Contact , Ward_ID)

            )

        db.commit()
        #Select SUM(cost)  from treatment where tid in (select tid from bill where pid = ?)

        
        return redirect(url_for('nurse.home'))
    
    return render_template('nurse/insert.html')