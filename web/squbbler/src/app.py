from flask import Flask, request, render_template, redirect, session
import sqlite3
import os
import re

app = Flask(__name__)
app.secret_key = 'harharharharharharharharharhar'  # required for session
DB_PATH = 'db.sqlite3'

def init_db():
    if os.path.exists(DB_PATH):
      os.remove(DB_PATH)
    
    conn = sqlite3.connect(DB_PATH)
    c = conn.cursor()
    c.execute('CREATE TABLE IF NOT EXISTS users (username TEXT, password TEXT)')
    c.execute("INSERT INTO users VALUES ('admin', 'deadbeef{r34l_t1m3_4t74ck}')")
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
        if not ("insert" in query.lower() or "drop" in query.lower() or "delete" in query.lower()):    
            conn = sqlite3.connect(DB_PATH)
            conn.execute(query)
            conn.close()

    return render_template('login.html', message=message)

if __name__ == '__main__':
    app.run(host='0.0.0.0',port='3957')
