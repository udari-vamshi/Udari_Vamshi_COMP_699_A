from database.models import Vote
from database.db import db
from services.priority_service import calculate_priority


def add_vote(user_id, issue_id):
    existing = Vote.query.filter_by(user_id=user_id, issue_id=issue_id).first()

    if not existing:
        vote = Vote(user_id=user_id, issue_id=issue_id)
        db.session.add(vote)
        db.session.commit()

        calculate_priority(issue_id)


def remove_vote(user_id, issue_id):
    vote = Vote.query.filter_by(user_id=user_id, issue_id=issue_id).first()

    if vote:
        db.session.delete(vote)
        db.session.commit()

        calculate_priority(issue_id)