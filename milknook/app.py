from flask import Flask, render_template, request
from pymongo import MongoClient

app = Flask(__name__)

# First you can Install mongo db in ur local mechine  and mongodb studio
client = MongoClient('mongodb://localhost:27017/')
db = client['test_db']
collection = db['test_collection']

@app.route('/')
def index():
    return render_template('index.html')

#=========Products page================

@app.route('/product')
def product():
    return render_template('product.html')

@app.route('/open', methods=('GET', 'POST'))
def login():
    return render_template('login.html')

@app.route('/add', methods=['POST'])
def add():
    username = request.form['username']
    #email = request.form['email']
    password = request.form['password']
    
    existing_user = collection.find_one({'username': username})
    
    if existing_user:
        return 'User already exists!'
    else:
     
        collection.insert_one({'username': username, 'password': password})
        return render_template('login.html')



if __name__ == '__main__':
    app.run(debug=True)