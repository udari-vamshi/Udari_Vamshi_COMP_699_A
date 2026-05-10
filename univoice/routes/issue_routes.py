from flask import Blueprint, redirect, url_for, render_template
from utils.auth import current_user
from database.models import Issue
from services.vote_service import add_vote, remove_vote

issue_bp = Blueprint('issue', __name__)


@issue_bp.route('/vote/<int:issue_id>')
def vote(issue_id):
    user_id = current_user()
    if user_id:
        add_vote(user_id, issue_id)

    return redirect(url_for('student.dashboard'))


@issue_bp.route('/remove_vote/<int:issue_id>')
def remove_vote_route(issue_id):
    user_id = current_user()
    if user_id:
        remove_vote(user_id, issue_id)

    return redirect(url_for('student.dashboard'))


@issue_bp.route('/issue/<int:id>')
def issue_detail(id):
    issue = Issue.query.get(id)
    return render_template('issue_detail.html', issue=issue)