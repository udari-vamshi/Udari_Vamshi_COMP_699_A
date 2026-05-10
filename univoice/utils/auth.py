from flask import session, redirect, url_for

def login_user(user):
    session['user_id'] = user.id
    session['role'] = user.role

def logout_user():
    session.clear()

def current_user():
    return session.get('user_id')

def is_admin():
    return session.get('role') == 'admin'