from flask import Flask, render_template, request
import random
import string
import pymongo
from zxcvbn import zxcvbn

app = Flask(__name__, static_url_path='/static')

# connect to MongoDB
client = pymongo.MongoClient('mongodb://mongo:sIKmH0MdBU7f3O8aouSa@containers-us-west-167.railway.app:5684')
db = client['passwords']
collection = db['generated_passwords']

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
    while True:
        password = ''.join(random.choice(password_chars) for i in range(length))
        if collection.find_one({'password': password}) is None:
            break
    collection.insert_one({'password': password})

    result = zxcvbn(password)
    strength = result['score']
    
    return render_template('index.html', password=password, strength=strength)

if __name__ == '__main__':
    app.run(debug=True)
