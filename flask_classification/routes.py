from flask import  render_template, url_for, redirect, flash
from flask_classification.forms import RegistrationForm, LoginForm
from flask_classification.models import User, Post

posts = [
    {
        'image': 'Place your image here',
        'classification': 'Your classification',
        'date_posted': 'November 10 2023'
    },
        {
        'image': 'Place your image here',
        'classification': 'Your classification',
        'date_posted': 'November 07 2023'
    }

]


@app.route("/")
@app.route("/home")
def home():
    return render_template('home.html', posts=posts)


@app.route("/about")
def about():
    return render_template('about.html', title='About')

@app.route("/register", methods=['GET', 'POST'])
def register():
    form = RegistrationForm()
    if form.validate_on_submit():
        flash(f'Account created for {form.username.data}!', 'success')
        return redirect(url_for('home'))
    return render_template('register.html', title='Register', form=form)


@app.route("/login", methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        if form.email.data == 'admin@blog.com' and form.password.data == 'password':
            flash('You have been logged in!', 'success')
            return redirect(url_for('home'))
        else:
            flash('Login Unsuccessful. Please check username and password', 'danger')
    return render_template('login.html', title='Login', form=form)

