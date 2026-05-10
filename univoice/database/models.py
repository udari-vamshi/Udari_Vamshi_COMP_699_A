from datetime import datetime
from .db import db

# ---------------- USER ----------------
class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(120), unique=True, nullable=False)
    password = db.Column(db.String(200), nullable=False)
    role = db.Column(db.String(20), default='student')  # student / admin

# ---------------- CATEGORY ----------------
class Category(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100))

# ---------------- ISSUE ----------------
class Issue(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    description = db.Column(db.Text, nullable=False)
    image = db.Column(db.String(200))
    
    status = db.Column(db.String(50), default="New")
    priority_score = db.Column(db.Float, default=0.0)
    tone = db.Column(db.String(50))
    cluster_id = db.Column(db.Integer)

    created_at = db.Column(db.DateTime, default=datetime.utcnow)

    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))
    category_id = db.Column(db.Integer, db.ForeignKey('category.id'))

# ---------------- VOTE ----------------
class Vote(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    issue_id = db.Column(db.Integer, db.ForeignKey('issue.id'))
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))
    created_at = db.Column(db.DateTime, default=datetime.utcnow)

# ---------------- FOLLOW ----------------
class Follow(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    issue_id = db.Column(db.Integer, db.ForeignKey('issue.id'))
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))

# ---------------- REPORT ----------------
class Report(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    generated_date = db.Column(db.DateTime, default=datetime.utcnow)