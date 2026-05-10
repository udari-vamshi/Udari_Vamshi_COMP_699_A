from flask import Flask
from config import Config
from database.db import db
from database.models import Category, User

# import routes
from routes.auth_routes import auth_bp
from routes.student_routes import student_bp
from routes.admin_routes import admin_bp
from routes.issue_routes import issue_bp


# -------- CATEGORY SEED FUNCTION --------
def seed_categories():
    categories = [
        "Academics",
        "Facilities",
        "Safety",
        "Campus Life"
    ]

    for c in categories:
        exists = Category.query.filter_by(name=c).first()
        if not exists:
            db.session.add(Category(name=c))

    db.session.commit()


# -------- DEFAULT ADMIN SEED FUNCTION --------
def seed_admin():
    admin_email = "vamshudari1@gmail.com"
    admin_password = "vamshi123"

    existing_admin = User.query.filter_by(email=admin_email).first()

    if not existing_admin:
        admin = User(
            email=admin_email,
            password=admin_password,
            role="admin"
        )
        db.session.add(admin)
        db.session.commit()
        print("Default admin created")


# -------- APP FACTORY --------
def create_app():
    app = Flask(__name__)
    app.config.from_object(Config)

    db.init_app(app)

    # register routes
    app.register_blueprint(auth_bp)
    app.register_blueprint(student_bp)
    app.register_blueprint(admin_bp)
    app.register_blueprint(issue_bp)

    # create tables + seed data
    with app.app_context():
        db.create_all()
        seed_categories()
        seed_admin()

    return app


# -------- RUN APP --------
app = create_app()

if __name__ == "__main__":
    app.run(debug=True)