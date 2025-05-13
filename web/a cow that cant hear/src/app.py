from flask import Flask, request, render_template, redirect, session
import sqlite3
import os

app = Flask(__name__)
app.secret_key = 'dev-key'  # required for session
DB_PATH = 'db.sqlite3'

def init_db():
    if os.path.exists(DB_PATH):
      os.remove(DB_PATH)
    
    conn = sqlite3.connect(DB_PATH)
    c = conn.cursor()
    c.execute('CREATE TABLE IF NOT EXISTS users (username TEXT, password TEXT)')
    c.execute('CREATE TABLE IF NOT EXISTS products (id INTEGER, name TEXT, price INTEGER)')
    c.execute('CREATE TABLE IF NOT EXISTS S3CR3t_t4BL3 (id TEXT, content TEXT)')
    c.execute("INSERT INTO users VALUES ('deafbeef', 'n8m4bnc8byxhb3jdc77rjbfviuc7c6t')")
    c.execute("INSERT INTO products VALUES (1, 'Apple', 5)")
    c.execute("INSERT INTO products VALUES (2, 'Banana', 10)")
    c.execute("INSERT INTO products VALUES (3, 'Cherry', 15)")
    c.execute("INSERT INTO S3CR3t_t4BL3 VALUES ('do you see the flag?', 'deafbeef{th3_b33F_1s_n0w_bl1nd}')")
    conn.commit()
    conn.close()

init_db()

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
