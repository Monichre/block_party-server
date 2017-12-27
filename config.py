import os
from urllib import parse


class DevConfig():
    DEBUG = True

    BASE_URL = 'http://localhost:5000/'
 

class WebStagingConfig():
    DEBUG = True

    BASE_URL = 'https://himembers-staging.herokuapp.com/'
  

class WebProdConfig():
    BASE_URL = 'https://members.hikarl.com/'



def apply_config(app):
    """ Apply configuration for application based on OS environ """
    if os.environ.get('WEB_PROD', False):
        config = ProdConfig
    elif os.environ.get('WEB_STAGING', False):
        config = StagingConfig
    else:
        config = DevConfig

    app.config.from_object(config)
