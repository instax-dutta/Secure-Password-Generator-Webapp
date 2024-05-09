from flask import Flask, render_template, request, g
import random
import string
import sqlite3
from zxcvbn import zxcvbn

app = Flask(__name__, static_url_path='/static')
app.config['DATABASE'] = 'passwords.db'

def get_db():
    db = getattr(g, '_database', None)
    if db is None:
        db = g._database = sqlite3.connect(app.config['DATABASE'])
    return db

@app.teardown_appcontext
def close_connection(exception):
    db = getattr(g, '_database', None)
    if db is not None:
        db.close()

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/generate', methods=['POST'])
def generate():
    length = int(request.form['length'])
    include_uppercase = 'upper' in request.form
    include_numbers = 'nums' in request.form
    include_special_characters = 'spec' in request.form

    password_chars = string.ascii_lowercase

    if include_uppercase:
        password_chars += string.ascii_uppercase
    if include_numbers:
        password_chars += string.digits
    if include_special_characters:
        password_chars += string.punctuation

    db = get_db()
    cursor = db.cursor()

    while True:
        password = ''.join(random.choice(password_chars) for i in range(length))
        cursor.execute("SELECT * FROM generated_passwords WHERE password=?", (password,))
        if cursor.fetchone() is None:
            break

    cursor.execute("INSERT INTO generated_passwords (password) VALUES (?)", (password,))
    db.commit()

    result = zxcvbn(password)
    strength = result['score']
    
    return render_template('index.html', password=password, strength=strength)

if __name__ == '__main__':
    app.run(debug=True)
