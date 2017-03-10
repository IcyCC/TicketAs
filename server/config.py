import os
basedir = os.path.abspath(os.path.dirname(__file__))

class Config:
    SECRET_KEY = 'hardgussstring'
    SQLALCHEMY_COMMIT_TEARDOWN = True
    FLASKY_ADMIN = 'hardgussstringsss'
    WTF_CSRF_SECRET_KEY = 'hardgussstringaaa'
    @staticmethod
    def init_app(app):
        pass

class DevelopmentConfig(Config):
    DEBUG = True
    SQLALCHEMY_DATABASE_URI =   \
        'sqlite:///' + os.path.join(basedir, 'data.sqlite')
        
class RunConfig(Config):
    DEBUG = False
    SQLALCHEMY_DATABASE_URI =   \
        'sqlite:///' + os.path.join(basedir, 'date-run.sqlite')

config = {
    'development':DevelopmentConfig,
    'run':RunConfig
}