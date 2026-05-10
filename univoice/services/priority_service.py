from database.models import Issue, Vote
from database.db import db


def calculate_priority(issue_id):
    issue = Issue.query.get(issue_id)

    vote_count = Vote.query.filter_by(issue_id=issue_id).count()

    cluster_count = Issue.query.filter_by(cluster_id=issue.cluster_id).count()

    urgent = 1 if issue.tone == "urgent" else 0

    score = (vote_count * 0.4) + (cluster_count * 0.4) + (urgent * 0.2)

    issue.priority_score = round(score, 2)

    db.session.commit()


def update_all_priorities():
    issues = Issue.query.all()

    for issue in issues:
        calculate_priority(issue.id)