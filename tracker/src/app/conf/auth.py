AUTH_USER_MODEL = 'app.User'
SOCIAL_AUTH_JSONFIELD_ENABLED = True

AUTHENTICATION_BACKENDS = [
    'app.auth.AtesOAuth2',
    'django.contrib.auth.backends.ModelBackend',
    'django.contrib.auth.backends.RemoteUserBackend',
]

SOCIAL_AUTH_ATES_KEY = 'wn5RijgTbAFpQQl7eA0CiSZIjqvHWpxSKsPIBG7w'
SOCIAL_AUTH_ATES_SECRET = '1HFhsJzftz3BRWcG5LRbbnepRjThomq73tb0i60EHDBkSZff7swITHq1jz0nSJuwWo1Vqj50ykKFGSIa0jSsYkqDexKXHBAfIwzdGgDgYulDA7lgloyNEJ4VvhAqUaqV'

LOGIN_URL = '/auth/login/oauth-baseoauth2/'

LOGIN_REDIRECT_URL = '/'
LOGOUT_REDIRECT_URL = '/'
