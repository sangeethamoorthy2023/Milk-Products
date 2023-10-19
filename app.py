from flask import Flask, render_template, request
from pymongo import MongoClient

app = Flask(__name__)

# First you can Install mongo db in ur local mechine  and mongodb studio
client = MongoClient('mongodb://localhost:27017/')
db = client['test_db']
collection = db['test_collection']

#==========Home===============
@app.route('/')
def index():
    return render_template('index.html')

#=========Products page================

@app.route('/product')
def product():
    return render_template('product.html')

#=========About us=====================

@app.route('/about')
def about():
    return render_template('About.html')

#=========contact us====================
@app.route('/contact')
def contact():
    return render_template('contact.html')

#==========Oreder now==================
@app.route('/order')
def order():
    return render_template('order.html')

#==========Login page======================
@app.route('/open', methods=('GET', 'POST'))
def login():
    return render_template('login.html')
@app.route('/loginopen', methods=['POST'])
def loginopen():
    email = request.form['email']
    password = request.form['password']

    user = collection.find_one({'email': email, 'password': password})

    if user:
        # Login successful
        return  render_template('index.html')
    else:
        # Login failed
        return "Invalid credentials. Please try again."


#===========Sign up=======================
@app.route('/signup')
def sign():
    return render_template('signup.html')


@app.route('/signupadd', methods=['POST'])
def signupadd():
    name = request.form['name']
    email = request.form['email']
    password = request.form['password']

    # Insert data into MongoDB
    user_data = {
        'name': name,
        'email': email,
        'password': password
    }

    collection.insert_one(user_data)

    # You can add further logic or redirect the user to another page after successful submission
    return render_template('login.html')

if __name__ == '__main__':
    app.run(host='0.0.0.0' )
    #port=5000