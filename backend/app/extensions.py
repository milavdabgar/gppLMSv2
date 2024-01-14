# extensions.py
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_bootstrap import Bootstrap
from flask_security import Security
from flask_mail import Mail
from flask_marshmallow import Marshmallow
from flask_babel import Babel
from flask_cors import CORS
# from flask_babelex import Babel
# from flask_admin import Admin
# from flask_caching import Cache
# from flask_moment import Moment
# from flask_jwt_extended import JWTManager
# from flask_login import LoginManager

# from flask_principal import Principal
# from flask_session import Session
# from flask_oauthlib.client import OAuth
# from flask_uploads import UploadSet, IMAGES
# from flask_pydantic import validate



# Initialize extensions, but without any specific app bound to them.
db = SQLAlchemy()
migrate = Migrate()
bootstrap = Bootstrap()
mail = Mail()
security = Security()
ma = Marshmallow()
babel = Babel()
cors = CORS()
# login = LoginManager()
# cache = Cache()
# admin = Admin(name='Gpp', template_mode='bootstrap3')
# moment = Moment()
# jwt = JWTManager()

# principal = Principal()
# session = Session()
# oauth = OAuth()
# image_set = UploadSet("images", IMAGES)