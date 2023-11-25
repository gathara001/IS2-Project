from flask import Blueprint, render_template
# from flask import  render_template, url_for, redirect, flash
# from flask_classification.forms import RegistrationForm, LoginForm
# from flask_classification.models import User, Post

main_blueprint = Blueprint('main', __name__)

@main_blueprint.route("/")
def hello():
    return render_template('home.html', posts=[])


@main_blueprint.route("/about")
def about():
    return render_template('about.html', title='About')

# urls_blueprint.route("/")
# def index():
#     return 'index page'


# @app.route("/home")
# def home():
#     return render_template('home.html', posts=[])
#
#
# def allowed_file(filename):
#     return '.' in filename and \
#            filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS
#
# @app.route('/', methods=['GET', 'POST'])
# def upload_file():
#     if request.method == 'POST':
#         if 'file' not in request.files:
#             flash('No file part')
#             return redirect(request.url)
#         file = request.files['file']
#         if file.filename == '':
#             flash('No selected file')
#             return redirect(request.url)
#         if file and allowed_file(file.filename):
#             filename = secure_filename(file.filename)
#             file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
#             return redirect(url_for('download_file', name=filename))
#
# @app.route("/about")
# def about():
#     return render_template('about.html', title='About')
#
# @app.route("/register", methods=['GET', 'POST'])
# def register():
#     form = RegistrationForm()
#     if form.validate_on_submit():
#         flash(f'Account created for {form.username.data}!', 'success')
#         return redirect(url_for('home'))
#     return render_template('register.html', title='Register', form=form)
#
#
# @app.route("/login", methods=['GET', 'POST'])
# def login():
#     form = LoginForm()
#     if form.validate_on_submit():
#         if form.email.data == 'admin@blog.com' and form.password.data == 'password':
#             flash('You have been logged in!', 'success')
#             return redirect(url_for('home'))
#         else:
#             flash('Login Unsuccessful. Please check username and password', 'danger')
#     return render_template('login.html', title='Login', form=form)