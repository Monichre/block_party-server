import os
basedir = os.path.abspath(os.path.dirname(__file__))


class Config(object):
    DEBUG = True
    TESTING = False
    CSRF_ENABLED = True
    SECRET_KEY = 'this-really-needs-to-be-changed'
    SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URL') or 'postgresql://localhost/block_party'


class ProductionConfig(Config):
    DEBUG = True
    SQLALCHEMY_DATABASE_URI = 'postgres://vyifvrvzhxfqjr:6abb99931b0b754a6cef72d4e5c09218e8329d29fcb079527fa86739eff363c2@ec2-23-21-246-25.compute-1.amazonaws.com:5432/d7kdus8jfnjbhj'


class StagingConfig(Config):
    DEVELOPMENT = True
    DEBUG = True
    SQLALCHEMY_DATABASE_URI = 'postgres://thcnzodhdmfmci:f444914121c12078f50b98a0183dbfa38385d2f1165a520fb9dac8856b71b69e@ec2-107-21-95-70.compute-1.amazonaws.com:5432/d8otav6il3klb1'


class DevelopmentConfig(Config):
    DEVELOPMENT = True
    # SQLALCHEMY_DATABASE_URI = 'postgresql://localhost/block_party'
    DEBUG = True


def apply_config(app):

    """ Apply configuration for application based on OS environ """
    
    if os.environ.get('productionConfig', False):
        config = ProductionConfig
    elif os.environ.get('stagingConfig', False):
        config = StagingConfig
    else:
        config = DevelopmentConfig

    app.config.from_object(config)
