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





@bp.route('/update', methods=('GET', 'POST'))
def update():
    return render_template('patient/update.html')


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
   
    SHOW = db.execute("SELECT * FROM Patient  ").fetchall()
    FF = db.execute("SELECT * FROM Patient_Contact  ").fetchall()
    
    
    return render_template('patient/show.html' , (SHOW) = (SHOW) , FF = FF)
   



@bp.route('/register', methods=('GET', 'POST'))
def register():
    if request.method == 'POST':
        name = request.form['name']
        
        dob= request.form['dob']

        sex =  request.form['sex']
        address  = request.form['address']
        Ward_ID  = request.form['Ward_ID']
        D_ID = request.form['D_ID']

        Contact = request.form['Contact']

        
        #from datetime import date
        #today = date.today()

        # dd/mm/YY
        #date_admit = today.strftime("%d/%m/%Y")
        #print("d1 =", d1)
        
        error = None
        if error is None:
            db = get_db()

            count = db.execute("SELECT COUNT(*) FROM Patient").fetchone()[0]
            count += 1
            print(count)
            db.execute("INSERT INTO Patient_Contact(P_ID , Contact) VALUES(? , ?)",
            (count , Contact)

            )

            db.execute('INSERT INTO Patient (Name , DOB , Sex , Address ,    Ward_ID , D_ID) VALUES (? ,   ? , ? , ? , ? , ?)',
                    (name , dob , sex , address ,     Ward_ID , D_ID)
                    )
           

    
            db.commit()

            return redirect(url_for('patient.id'))


    return render_template('patient/register.html')





@bp.route('/update_discharge', methods=('GET', 'POST'))
def update_discharge():
    if request.method == 'POST':
        id = request.form['id']
        discharge = request.form['discharge']



        db = get_db()
        db.execute(
            'UPDATE Patient SET Date_Discharged = ?'
            ' WHERE P_ID = ?',
            (discharge, id)
        )
        db.commit()
        return redirect(url_for('patient.home'))

    return render_template('patient/discharge.html')




@bp.route('/update_dID', methods=('GET', 'POST'))
def update_dID():
    if request.method == 'POST':
        id = request.form['id']
        D_ID = request.form['D_ID']



        db = get_db()
        db.execute(
            'UPDATE Patient SET D_ID = ?'
            ' WHERE P_ID = ?',
            (D_ID, id)
        )
        db.commit()
        return redirect(url_for('patient.home'))

    return render_template('patient/dID.html')




@bp.route('/bill', methods=('GET', 'POST'))
def bill():
    if request.method == 'POST':
        id = request.form['id']
        #count_treatment = int(request.form['count_treatment'])
        T_ID = request.form['T_ID']
        db = get_db()
        db.execute("INSERT INTO Bill (P_ID , T_ID) VALUES (? , ?)",
        (id , T_ID )
        )
        db.commit()
        
        return redirect(url_for('patient.bill'))
    
    return render_template('patient/bill.html')



@bp.route('/cost', methods=('GET', 'POST'))
def cost():
    if request.method == 'POST':
        id = request.form['id']
        db = get_db()
        sum = db.execute("select SUM(Cost)  from Treatment where T_ID in (select T_ID from Bill where P_ID = ?)",
        (id , )
        ).fetchone()[0]

        FF = db.execute('SELECT Cost , Name  from Treatment where T_ID in (select T_ID from Bill where P_ID = ?)' , 
         (id , )
        ).fetchall()

        #db.commit()
        #Select SUM(cost)  from treatment where tid in (select tid from bill where pid = ?)

        
        return render_template('patient/result.html' , (sum) = (sum) , FF = FF)
    
    return render_template('patient/cost.html')



@bp.route('/insert', methods=('GET', 'POST'))
def insert():
    if request.method == 'POST':
        id = request.form['id']
        Contact = request.form['Contact']
        db = get_db()
        db.execute("INSERT INTO Patient_Contact(P_ID , Contact) VALUES(? , ?)",
            (id , Contact)

            )

        db.commit()
        #Select SUM(cost)  from treatment where tid in (select tid from bill where pid = ?)

        
        return redirect(url_for('patient.home'))
    
    return render_template('patient/insert.html')
