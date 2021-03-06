import os

basedir = os.path.abspath(os.path.dirname(__file__))

SECRET_KEY = os.environ.get('SECRET_KEY') or 'you-will-never-guess'
SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URL') or \
    'sqlite:///' + os.path.join(basedir, 'app.db')
SQLALCHEMY_MIGRATE_REPO = os.path.join(basedir, 'db_repository')
SQLALCHEMY_TRACK_MODIFICATIONS = False
CSRF_ENABLED = True
    #SECRET_KEY = 'you-will-never-guess'

'''
SQLALCHEMY_DATABASE_URI = 'sqlite:///' + os.path.join(basedir, 'app.db')
SQLALCHEMY_MIGRATE_REPO = os.path.join(basedir, 'db_repository')
SQLALCHEMY_TRACK_MODIFICATIONS = False
'''
