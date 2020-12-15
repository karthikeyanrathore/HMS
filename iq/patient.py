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
    count = db.execute("SELECT COUNT(*) FROM Patient").fetchone()[0]
    return render_template('patient/id.html' , count = count)


@bp.route('/show', methods=('GET', 'POST'))
def show():
    db = get_db()
    SHOW = db.execute("SELECT * FROM Patient  ").fetchall()
    FF = db.execute("SELECT * FROM Patient_Contact  ").fetchall()
    GG = db.execute("SELECT *  FROM Doctor").fetchall()
    KK = db.execute("SELECT *  FROM Wards").fetchall()
    return render_template('patient/show.html' , SHOW = SHOW , FF = FF , GG = GG , KK = KK)


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
        
        db = get_db()
        error = None
        if len(str(Contact)) != 10:
            error = "Contact No. Should be 10 Digit Number"

        flash(error)
        ward = db.execute(
            'SELECT * FROM Wards WHERE Ward_ID = ?', (Ward_ID,)
        ).fetchone()

        if ward is None:
            error = "Ward  ID : {} is not registered".format(Ward_ID)

        flash(error)
        doctor = db.execute(
            'SELECT * FROM Doctor WHERE D_ID = ?', (D_ID,)
        ).fetchone()

        if doctor is None:
            error = "Doctor  ID : {} is not registered".format(D_ID)

        flash(error)

        if error is None:
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
        error = None
        name = db.execute(
            'SELECT * FROM Patient WHERE P_ID = ?', (id,)
        ).fetchone()

        if name is None:
            error = "Patient id :{} is not registered".format(id)

        flash(error)

        if error is None:
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
        
        error = None
        name = db.execute(
            'SELECT * FROM Patient WHERE P_ID = ?', (id,)
        ).fetchone()

        if name is None:
            error = "Patient id :{} is not registered".format(id)

        flash(error)

        if error is None:
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
        T_ID = request.form['T_ID']
        db = get_db()

        error = None
        name = db.execute(
            'SELECT * FROM Patient WHERE P_ID = ?', (id,)
        ).fetchone()

        if name is None:
            error = "Patient id :{} is not registered".format(id)

        flash(error)

        if error is None:
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

        error = None
        name = db.execute(
            'SELECT * FROM Patient WHERE P_ID = ?', (id,)
        ).fetchone()

        if name is None:
            error = "Patient id :{} is not registered".format(id)

        flash(error)

        if error is None:
            sum = db.execute("select SUM(Cost)  from Treatment where T_ID in (select T_ID from Bill where P_ID = ?)",
            (id , )
            ).fetchone()[0]

            FF = db.execute('SELECT Cost , Name  from Treatment where T_ID in (select T_ID from Bill where P_ID = ?)' , 
            (id , )
            ).fetchall()
            
            return render_template('patient/result.html' , sum = sum , FF = FF)
        
    return render_template('patient/cost.html')



@bp.route('/insert', methods=('GET', 'POST'))
def insert():
    if request.method == 'POST':
        id = request.form['id']
        Contact = request.form['Contact']
        db = get_db()

        error = None
        name = db.execute(
            'SELECT * FROM Patient WHERE P_ID = ?', (id,)
        ).fetchone()

        if name is None:
            error = "Patient id :{} is not registered".format(id)

        flash(error)

        if error is None:
            db.execute("INSERT INTO Patient_Contact(P_ID , Contact) VALUES(? , ?)",
                (id , Contact)

                )

            db.commit()
            return redirect(url_for('patient.home'))
    
    return render_template('patient/insert.html')
