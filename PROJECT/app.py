from flask import Flask, render_template, request, redirect, url_for, session,flash
import boto3
from boto3.dynamodb.conditions import Key,Attr
import uuid
from datetime import datetime,timedelta
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from bcrypt import hashpw,gensalt,checkpw
import os
import random

app = Flask(__name__)
app.secret_key = os.urandom(24)
 
@app.context_processor
def inject_now():
    return{'now':datetime.now}

# AWS Configuration
s3_bucket = 'your-s3-bucket-name'
region_name = 'your-region'

# AWS Clients
s3 = boto3.client('s3')
dynamodb = boto3.resource('dynamodb', region_name=region_name)
user_table = dynamodb.Table('Users')
orders_table = dynamodb.Table('Orders')




EMAIL_ADDRESS = 'your_email@gmail.com'
EMAIL_PASSWORD = 'your_gmail_app_password'


app = Flask(__name__)
app.secret_key = 'your_secret_key_here'  # Replace with a strong secret key

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/veg_pickles')
def veg_pickles():
    return render_template('veg_pickles.html')

@app.route('/non_veg_pickles')
def non_veg_pickles():
    return render_template('non_veg_pickles.html')

@app.route('/snacks')
def snacks():
    return render_template('snacks.html')
@app.route('/add_to_cart/<product_id>', methods=['POST'])
def add_to_cart(product_id):
    # Example product data (you’d usually get this from your DB)
    products = {
        'mango': {'name': 'Mango Pickle', 'price': 130},
        'tomato':{'name': 'Tomato Pickle', 'price': 120},
        'gongura':{'name':'Gongura Pickle', 'price':150},
        'lemon':{'name':'Lemon Pickle', 'price': 140},
        'chicken': {'name': 'Chicken Pickle', 'price': 250},
        'prawn': {'name': 'Prawn Pickle', 'price': 300},
        'mutton':{'name':'Mutton Pickle', 'price':300},
        'fish': {'name': 'Fish Pickle', 'price': 260},
        'murukulu': {'name': 'Murukulu', 'price': 50},
        'boondi': {'name': 'Boondi', 'price': 80},
        'chekkalu': {'name': 'Chekkalu', 'price': 90},
        'mixture': {'name': 'Mixture', 'price': 90}
    }

    if 'cart' not in session:
        session['cart'] = []

    product = products.get(product_id)
    if product:
        found = False
        for item in session['cart']:
            if item['name'] == product['name']:
                item['quantity'] += 1
                found = True
                break

        if not found:
            product_with_qty = product.copy()
            product_with_qty['quantity'] = 1
            session['cart'].append(product_with_qty)

        session.modified = True

    return redirect(url_for('cart'))
@app.route('/cart')
def cart():
    cart_items = session.get('cart', [])
    return render_template('cart.html', cart_items=cart_items)

@app.route('/checkout', methods=['GET', 'POST'])
def checkout():
    cart_items = session.get('cart', [])
    return render_template('checkout.html', cart_items=cart_items)

@app.route('/success')
def success():
    return render_template('success.html')

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form.get('username')
        password = request.form.get('password')
        # Add login logic here
        return redirect(url_for('index'))
    return render_template('login.html')

@app.route('/signup', methods=['GET', 'POST'])
def signup():
    if request.method == 'POST':
        username = request.form.get('username')
        password = request.form.get('password')
        # Add signup logic here
        return redirect(url_for('login'))
    return render_template('signup.html')

@app.route('/about')
def about():
    return render_template('about.html')

@app.route('/contact')
def contact_us():
    return render_template('contact us.html')

if __name__ == '__main__':
    app.run(debug=True)
