import functools
from flask import (
    Blueprint, flash, g, redirect, render_template, request, session, url_for
)
from werkzeug.security import check_password_hash, generate_password_hash

from iq.db import get_db

bp = Blueprint('product', __name__, url_prefix='/product')


@bp.route('/search', methods=('GET', 'POST'))
def search():
    if request.method == 'POST':
        find = request.form['find']
        error = None
        db= get_db()

        LP = db.execute(
                "SELECT * FROM product WHERE id = '%s'" % find).fetchone()
        #print(LP['stock'])
    
        #LP = db.execute(
                #"SELECT * FROM product WHERE name = " + find).fetchone()
       

        if LP  is None:
            error = "INVALID NAME"
        
        flash(error)

        return render_template('product/result.html', LP= LP)

    return render_template('product/search.html')


@bp.route('/insert', methods=('GET', 'POST'))
def insert():
    error = None
    if error is None:
        db = get_db()
        sql = 'INSERT INTO product (id, name , price , stock) VALUES (? , ? , ? , ?)'
        val = [
                (1 , 'pen drive' , 200 , 7),

                (2 , 'pc' , 500 , 9),
                (3 , 'laptop' , 400 , 1),
                (4 , 'ssd' , 100 , 7),
                (5 , 'mouse' , 900 , 6),
                (6 , 'monitor' , 600 , 4)
                ]
        db.executemany(sql , val)
        db.commit()
        return redirect(url_for('product.search'))

    return render_template('product/insert.html')

