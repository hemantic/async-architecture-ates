from app.conf.environ import env

AUTH_USER_MODEL = 'app.User'
SOCIAL_AUTH_JSONFIELD_ENABLED = True

AUTHENTICATION_BACKENDS = [
    'app.auth.AtesOAuth2',
    'django.contrib.auth.backends.ModelBackend',
    'django.contrib.auth.backends.RemoteUserBackend',
]

SOCIAL_AUTH_ATES_KEY = env('SOCIAL_AUTH_ATES_KEY', cast=str, default='')
SOCIAL_AUTH_ATES_SECRET = env('SOCIAL_AUTH_ATES_SECRET', cast=str, default='')

LOGIN_URL = '/auth/login/oauth-baseoauth2/'

LOGIN_REDIRECT_URL = '/'
LOGOUT_REDIRECT_URL = '/'
