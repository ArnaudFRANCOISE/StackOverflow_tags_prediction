import os

#test

ENV = 'PRODUCTION'

# SECURITY WARNING: don't run with debug turned on in production!

if os.environ.get('ENV') == 'PRODUCTION':

    DEBUG = False

else:

    DEBUG = True




SECRET_KEY = os.environ.get('SECRET_KEY', 'a@a[|c3]/{l/rW7/n/tMD/x0bY[Ixo') # development key for the moment



ALLOWED_HOSTS = ['stackoverflowtagspredictions.herokuapp.com']



if os.environ.get('ENV') == 'PRODUCTION':



    # Static files settings

    PROJECT_ROOT = os.path.dirname(os.path.abspath(__file__))



    STATIC_ROOT = os.path.join(PROJECT_ROOT, 'staticfiles')



    # Extra places for collectstatic to find static files.

    STATICFILES_DIRS = (

        os.path.join(PROJECT_ROOT, 'static'),

    )



MIDDLEWARE = [

    # ...

    'whitenoise.middleware.WhiteNoiseMiddleware',

    # ...

]



if os.environ.get('ENV') == 'PRODUCTION':

    # ...

    # Simplified static file serving.

    # https://warehouse.python.org/project/whitenoise/

    STATICFILES_STORAGE = 'whitenoise.storage.CompressedManifestStaticFilesStorage'