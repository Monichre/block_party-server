import os
basedir = os.path.abspath(os.path.dirname(__file__))


class Config:
    DEBUG = False
    TESTING = False
    CSRF_ENABLED = True
    SECRET_KEY = 'this-really-needs-to-be-changed'
    SQLALCHEMY_DATABASE_URI = os.environ.get("DATABASE_URL")


class ProductionConfig(Config):
    DEBUG = False

class StagingConfig(Config):
    DEVELOPMENT = True
    DEBUG = True


class DevelopmentConfig(Config):
    DEVELOPMENT = True
    SQLALCHEMY_DATABASE_URI = 'postgresql://localhost/block_party'
    DEBUG = True


def apply_config(app):

    """ Apply configuration for application based on OS environ """
    
    if os.environ.get('productionConfig', False):
        config = ProdConfig
    elif os.environ.get('stagingConfig', False):
        config = StagingConfig
    else:
        config = DevelopmentConfig

    app.config.from_object(config)
