from flask import Flask
from extensions import db, migrate
from dotenv import load_dotenv
import os

# load vars from .env into os.environ
load_dotenv()

def create_app():
    app = Flask(__name__)

    user = os.getenv("DB_USER")
    pw = os.getenv("DB_PASS")
    host = os.getenv("DB_HOST")
    db_name = os.getenv("DB_NAME")

    # ➊ point SQLAlchemy at your Postgres database
    app.config["SQLALCHEMY_DATABASE_URI"] = (
        f"postgresql://{user}:{pw}@{host}:5432/{db_name}"
    )
    app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False  # silence warnings

    db.init_app(app)
    migrate.init_app(app, db)

    # register Blueprints
    from routes.items import items_bp
    from routes.users import users_bp

    app.register_blueprint(items_bp, url_prefix="/api/items")
    app.register_blueprint(users_bp, url_prefix="/api/users")

    return app


app = create_app()

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)
