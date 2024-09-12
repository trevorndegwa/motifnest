from flask import render_template, url_for, flash, redirect
from motifnest import app
from motifnest.forms import RegistrationForm, LoginForm
from motifnest.models import User, Post


posts = [
    {
        'author': 'Trevor Ndegwa',
        'title': 'Post 1',
        'content': 'First post content',
        'date_posted': 'September 4th, 2024'
    },
    {
        'author': 'Corey Schafer',
        'title': 'Post 2',
        'content': 'Second post content',
        'date_posted': 'April 20th, 2024'
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
                        flash(f'You have been logged in!', 'success')
                        return redirect(url_for('home'))
                else:
                        flash(f'Login unsuccessful. Please check username and password', 'danger')
        return render_template('login.html', title='Login', form=form)
