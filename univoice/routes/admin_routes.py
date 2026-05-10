from flask import Blueprint, render_template, redirect
from database.models import Issue
from database.db import db

admin_bp = Blueprint('admin', __name__)

@admin_bp.route('/admin/dashboard')
def admin_dashboard():
    issues = Issue.query.order_by(Issue.priority_score.desc()).all()
    return render_template('admin_dashboard.html', issues=issues)


@admin_bp.route('/admin/update/<int:id>/<status>')
def update_status(id, status):
    issue = Issue.query.get(id)
    issue.status = status
    db.session.commit()

    return redirect('/admin/dashboard')