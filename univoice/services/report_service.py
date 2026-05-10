from database.models import Issue
from sqlalchemy import func
from database.db import db


def get_trending_issues():
    return Issue.query.order_by(Issue.priority_score.desc()).limit(10).all()


def get_cluster_summary():
    data = db.session.query(
        Issue.cluster_id,
        func.count(Issue.id)
    ).group_by(Issue.cluster_id).all()

    return data