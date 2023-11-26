# app/routes.py

from flask import render_template, redirect, url_for, request, session
from app import app, db
from app.models import User
import bcrypt


@app.route('/', methods=["GET"])
def index():
    return render_template('login.html', email="matu@gmail.com", password="password")


@app.route('/dashboard', methods=["GET"])
def dashboard():
    return render_template('dashboard.html')


@app.route('/login', methods=["POST"])
def login():
    email = request.form['email']
    password = request.form['password']

    # Query the database to find the user by username
    user = User.query.filter_by(email=email).first()

    if user:
        # If the user exists, verify the password
        if bcrypt.checkpw(password.encode('utf-8'), user.password_hash.encode('utf-8')):
            # Password is correct - set user session and redirect to a dashboard or profile page
            session['user_id'] = user.id  # Store the user's ID in the session
            return redirect(url_for('dashboard'))  # Redirect to a dashboard page upon successful login

    # If username or password is incorrect, show an error message or redirect to the login page
    return render_template('login.html', error='Invalid username or password')


@app.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        username = request.form['username']
        email = request.form['email']
        password = request.form['password']  # Note: Password hashing should be implemented for security

        # Hash the password before storing it
        hashed_password = bcrypt.hashpw(password.encode('utf-8'), bcrypt.gensalt())

        # Create a new user instance
        new_user = User(username=username, email=email, password_hash=hashed_password)

        # Add the user to the session and commit to the database
        db.session.add(new_user)
        db.session.commit()

        return redirect(url_for('index'))  # Redirect to the home page after successful registration

    return render_template('register.html', username="matu", email="matu@gmail.com", password="password")  # Render the registration form
