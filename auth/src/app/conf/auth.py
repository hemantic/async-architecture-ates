AUTH_USER_MODEL = 'app.User'

AUTHENTICATION_BACKENDS = [
    'django.contrib.auth.backends.ModelBackend',
    'django.contrib.auth.backends.RemoteUserBackend',
]

LOGIN_URL='/admin/login/'
