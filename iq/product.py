import functools
from flask import (
    Blueprint, flash, g, redirect, render_template, request, session, url_for
)
from werkzeug.security import check_password_hash, generate_password_hash
from iq.db import get_db
bp = Blueprint('product', __name__, url_prefix='/product')

@bp.route('/home', methods=('GET', 'POST'))
def home():
  return render_template('product/home.html')

@bp.route('/search', methods=('GET', 'POST'))
def search():
  if request.method == 'POST':
    find = request.form['find']
    name = request.form['name']
    query = request.form['options']
    error = None
    db = get_db()
    
    if(int(query) == 1):
      # correct way
      LP = db.execute("SELECT * FROM product WHERE id = ? AND name = ?" ,( find , name))
     # print(LP.fetchone()[0])
    else:
      # wrong way (SQL-injection-attack)
      #LP = db.execute("SELECT * FROM product")
      LP = db.execute(f"SELECT * FROM product WHERE id = '{find}' AND name = '{name}'")
    return render_template('product/result.html', LP= LP)

  if request.method == "GET":
    return render_template('product/search.html')

@bp.route('/insert', methods=('GET', 'POST'))
def insert():
  error = None
  db = get_db()
  if request.method == "POST":
    if error is None:
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
    rows = db.execute("SELECT count(*) from product")
    rows = rows.fetchone()[0]
    return render_template('product/insert.html' , rows=rows)

@bp.route('/delete', methods=('GET', 'POST'))
def delete():
  error = None
  db = get_db()
  if request.method == "POST":
      db.execute('DELETE FROM product')
      db.commit()
      return redirect(url_for('product.search'))
  
  if request.method == "GET":
    rows = db.execute("SELECT count(*) from product")
    rows = rows.fetchone()[0]
    return render_template('product/delete.html' , rows=rows)

