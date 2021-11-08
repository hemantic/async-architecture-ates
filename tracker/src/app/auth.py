from urllib.parse import urlencode

from social_core.backends.oauth import BaseOAuth2


class AtesOAuth2(BaseOAuth2):
    name = 'ates'
    AUTHORIZATION_URL = 'http://ates-auth:8081/o/authorize/'
    ACCESS_TOKEN_URL = 'http://ates-auth:8081/o/token/'
    ACCESS_TOKEN_METHOD = 'POST'
    SCOPE_SEPARATOR = ','

    def get_user_details(self, response):
        return {
            'username': response.get('username'),
            'email': response.get('email') or '',
        }

    def user_data(self, access_token, *args, **kwargs):
        url = 'http://ates-auth:8081/profile/' + urlencode({
            'access_token': access_token
        })

        return self.get_json(url)
