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

#===========Sign up=======================
@app.route('/signup')
def sign():
    return render_template('signup.html')

@app.route('/signupadd', methods=['POST'])
def add():
    username = request.form['username']
    email = request.form['email']
    password = request.form['password']
    
    existing_user = collection.find_one({'username': username})
    
    if existing_user:
        return 'User already exists!'
    else:
     
        collection.insert_one({'username': username, 'password': password,'email':email})
        return render_template('login.html')



if __name__ == '__main__':
    app.run(debug=True)