import os

basedir = os.path.abspath(os.path.dirname(__file__))


class Config(object):

    # SECRET KEY
    SECRET_KEY = os.environ.get('SECRET_KEY') or 'A-VERY-LONG-SECRET-KEY'

    # RECAPTCHA PUBLIC KEY
    # RECAPTCHA_PUBLIC_KEY = os.environ.get('RECAPTCHA_PUBLIC_KEY') or 'yckhbev23y74rfgtkdbnfcvsr9iq2r3w4^$#%^&^&RE^$HCGVNB'

    # RECAPTCHA PRIVATE KEY
    # RECAPTCHA_PRIVATE_KEY = os.environ.get('RECAPTCHA_PRIVATE_KEY') or 'yckhbev23y74rfgtkdbnfcvsr9iq2r3w4^$#%^&^&RE^$HCGVNB'


    # Database configuration
    SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URL') or 'sqlite:///' + os.path.join(basedir, 'app.db')
    SQLALCHEMY_TRACK_MODIFICATIONS = False
