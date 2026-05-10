from flask import Blueprint, render_template, request, redirect
from database.db import db
from database.models import Issue, Category
from utils.auth import current_user

from services.ml_engine import process_new_issue
from services.priority_service import calculate_priority

student_bp = Blueprint('student', __name__)


@student_bp.route('/student/dashboard')
def dashboard():
    issues = Issue.query.order_by(Issue.priority_score.desc()).all()
    return render_template('dashboard.html', issues=issues)


@student_bp.route('/submit_issue', methods=['GET', 'POST'])
def submit_issue():
    if request.method == 'POST':
        description = request.form['description']
        category_id = request.form['category']

        issue = Issue(
            description=description,
            category_id=category_id,
            user_id=current_user()
        )

        db.session.add(issue)
        db.session.commit()

        process_new_issue(issue)
        calculate_priority(issue.id)

        return redirect('/student/dashboard')

    categories = Category.query.all()
    return render_template('submit_issue.html', categories=categories)