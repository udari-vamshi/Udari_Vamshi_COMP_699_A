from flask import Blueprint, render_template, request, redirect, url_for, flash
from database.db import db
from database.models import User
from utils.auth import login_user, logout_user

auth_bp = Blueprint('auth', __name__)


@auth_bp.route('/')
def home():
    return redirect(url_for('auth.login'))


@auth_bp.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        email = request.form['email']
        password = request.form['password']
        confirm_password = request.form['confirm_password']

        # check password match
        if password != confirm_password:
            flash("Passwords do not match", "error")
            return redirect(url_for('auth.register'))

        # check if user exists
        existing_user = User.query.filter_by(email=email).first()
        if existing_user:
            flash("Email already registered", "error")
            return redirect(url_for('auth.register'))

        # create new user
        new_user = User(email=email, password=password)
        db.session.add(new_user)
        db.session.commit()

        flash("Registration successful. Please login.", "success")
        return redirect(url_for('auth.login'))

    return render_template('register.html')


@auth_bp.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        email = request.form['email']
        password = request.form['password']

        user = User.query.filter_by(email=email, password=password).first()

        if not user:
            flash("Invalid email or password", "error")
            return redirect(url_for('auth.login'))

        login_user(user)

        if user.role == 'admin':
            return redirect('/admin/dashboard')
        else:
            return redirect('/student/dashboard')

    return render_template('login.html')


@auth_bp.route('/logout')
def logout():
    logout_user()
    flash("Logged out successfully", "success")
    return redirect(url_for('auth.login'))