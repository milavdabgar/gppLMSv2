from flask import Flask
from config import LocalDevelopmentConfig
from .extensions import db, migrate, security, bootstrap, mail, ma, babel, cors
from .api import api_bp
from .api_calls import api_call_bp
from .routes_librarian import librarian_bp
from .routes_member import member_bp
from .utilities.utils import initialize_db
from .utilities.generate_dummy_data import generate_dummy_data
# import flask_excel as excel
# from flask_sse import sse
from .views import setup_admin
from .models import user_datastore


def create_app():
    app = Flask(__name__)
    app.config.from_object(LocalDevelopmentConfig)
    db.init_app(app)
    ma.init_app(app)
    migrate.init_app(app, db)

    app.app_context().push()
    

    mail.init_app(app)
    bootstrap.init_app(app)
    security.init_app(app, user_datastore)
    app.user_datastore = user_datastore

    # cache.init_app(app)
    # excel.init_excel(app)
    # admin.init_app(app)
    # moment.init_app(app)
    # login.init_app(app)
    babel.init_app(app)
    cors.init_app(app)
    setup_admin(app)
    with app.app_context():
        db.create_all()
        # generate_dummy_data()
        # initialize_db(user_datastore)
        # import app.views

    # Register Blueprints
    # app.register_blueprint(user_api_bp, user_datastore=user_datastore)
    app.register_blueprint(api_bp)        
    # app.register_blueprint(user_api_call_bp)
    # app.register_blueprint(librarian_bp)
    app.register_blueprint(member_bp)
    # app.register_blueprint(main_bp)
    # app.register_blueprint(api_call_bp)

    # # This is for streaming
    # app.register_blueprint(sse, url_prefix="/stream")

    return app
