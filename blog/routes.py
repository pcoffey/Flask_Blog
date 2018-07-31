from flask import render_template, url_for, flash, redirect
from blog import app
from blog.forms import RegistrationForm, LoginForm
from blog.models import User, Post

posts = [
    {
        'author': 'Jack Bauer',
        'title': 'Blog Post 1',
        'content': 'POSTY content 1',
        'date_posted': 'June 20, 2018'
    },
    {
        'author': 'Shelly Bauer',
        'title': 'Blog Post 20',
        'content': 'POSTY Mc Post content 5',
        'date_posted': 'May 20, 2018'
    }
]


@app.route('/')
@app.route('/home')
def home():
    return render_template('index.html', posts=posts)


@app.route('/about')
def about():
    return render_template('about.html', title='About')


@app.route('/register', methods=['GET', 'POST'])
def register():
    form = RegistrationForm()
    if form.validate_on_submit():
        flash(f'Account created for {form.username.data}!', 'success')
        return redirect(url_for('home'))
    return render_template('register.html', title='Register', form=form)


@app.route('/login', methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        if form.email.data == 'admin@blog.com' and form.password.data == 'password':
            flash('You have been logged in!', 'success')
            return redirect(url_for('home'))
        else:
            flash('Login unsuccessful. Please check username and password', 'danger')
    return render_template('login.html', title='Login', form=form)

