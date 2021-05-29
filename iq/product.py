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
    name = request.form['name']
    error = None
    db = get_db()

    # correct way
    #LP = db.execute("SELECT * FROM product WHERE id = ? AND name = ?" ,( find , name))

    # wrong way (SQL-injection-attack)
    #LP = db.execute("SELECT * FROM product")
    LP = db.execute(f"SELECT * FROM product WHERE id = '{find}' AND name = '{name}'")
    
    if LP  is None:
      error = "INVALID NAME"
    return render_template('product/result.html', LP= LP)

  if request.method == "GET":
    return render_template('product/search.html')

@bp.route('/insert', methods=('GET', 'POST'))
def insert():
  error = None
  if request.method == "POST":
    if error is None:
      db = get_db()
      sql = 'INSERT INTO product (id, name , price , stock) VALUES (? , ? , ? , ?)'
      val = [
          (1 , 'pendrive' , 200 , 7),
          (2 , 'scale' , 500 , 9),
          (3 , 'laptop' , 400 , 1),
          (4 , 'ssd' , 100 , 7),
          (5 , 'mouse' , 900 , 6),
          (6 , 'monitor' , 600 , 4)
          ]
      db.executemany(sql , val)
      db.commit()
      return redirect(url_for('product.search'))
  
  if request.method == "GET":
    return render_template('product/insert.html')

