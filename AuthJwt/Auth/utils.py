import datetime

import jwt
from django.conf import settings


def generate_access_token(access_dic):
    access_token_payload = {
        'exp': datetime.datetime.utcnow() + datetime.timedelta(days=0, minutes=5),
        'iat': datetime.datetime.utcnow(),
    }
    access_token_payload.update(access_dic)
    access_token = jwt.encode(access_token_payload,
                              settings.JWT_SECRET, algorithm='HS256').decode('utf-8')
    return access_token
