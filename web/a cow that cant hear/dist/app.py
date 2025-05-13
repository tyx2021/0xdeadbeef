from flask import Flask, request, render_template, redirect, session
import sqlite3
import os

app = Flask(__name__)
app.secret_key = 'dev-key'  # required for session
DB_PATH = 'db.sqlite3'

@app.route('/', methods=['GET', 'POST'])
def login():
    message = ''
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']

        query = f"SELECT * FROM users WHERE username = '{username}' AND password = '{password}'"
        print(f"[DEBUG] SQL: {query}")

        conn = sqlite3.connect(DB_PATH)
        cursor = conn.cursor()
        try:
            cursor.execute(query)
            user = cursor.fetchone()
        except Exception as e:
            user = None
            message = f"SQL Error: {e}"

        if user:
            session['user'] = user[0]
            return redirect('/dashboard')
        else:
            message = "Login failed."

    return render_template('login.html', message=message)

@app.route('/dashboard')
def dashboard():
    if 'user' not in session:
        return redirect('/')

    product_id = request.args.get('product_id', '')
    results = ''
    if product_id:
        query = f"SELECT * FROM products WHERE id = {product_id}"
        print(f"[DEBUG] SQL: {query}")
        try:
            conn = sqlite3.connect(DB_PATH)
            c = conn.cursor()
            c.execute(query)
            rows = c.fetchall()
            results = "<br>".join([f"ID: {r[0]}, Name: {r[1]}, Price: ${r[2]}" for r in rows])
        except Exception as e:
            results = f"Error: {e}"

    return render_template('dashboard.html', user=session['user'], results=results)

if __name__ == '__main__':
    app.run(debug=True)
