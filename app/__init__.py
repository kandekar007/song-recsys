from flask import Flask
from flask_bootstrap import Bootstrap
from config import Config

app = Flask(__name__)
bootstrap = Bootstrap(app)
#app.config.update(dict(
#    SECRET_KEY="powerful secretkey",
#    WTF_CSRF_SECRET_KEY="a csrf secret key"
# ))
app.config.from_object(Config)
from app import routes
