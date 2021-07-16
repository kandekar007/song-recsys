import os

class Config(object):
    key = str(os.urandom(32))
    SECRET_KEY="powerful secretkey",
    WTF_CSRF_SECRET_KEY="a csrf secret key"
