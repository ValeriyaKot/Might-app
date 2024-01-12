import json
import jwt
import requests
from django.contrib.auth import authenticate
import environ
from .models import EmployeeInfo

env = environ.Env()


def jwt_get_username_from_payload_handler(payload):
    user_guid = payload.get('sub')
    user = authenticate(remote_user=user_guid)
    EmployeeInfo.objects.get_or_create(
        user=user,
        name=payload.get('name'),
        family_name=payload.get('family_name'),
        role=payload.get('role'),
        position=payload.get('position')
    )
    return user_guid


def jwt_decode_token(token):
    header = jwt.get_unverified_header(token)
    jwks = requests.get(
        '{}/.well-known/openid-configuration/jwks'.format(env('JWT_ISSUER')),
        verify=False
    ).json()
    public_key = None
    for jwk in jwks['keys']:
        if jwk['kid'] == header['kid']:
            public_key = jwt.algorithms.RSAAlgorithm.from_jwk(json.dumps(jwk))

    if public_key is None:
        raise Exception('Public key not found.')

    issuer = env('JWT_ISSUER')
    payload = jwt.decode(
        token,
        public_key,
        issuer=issuer,
        audience=None,
        algorithms=['RS256']
    )
    return payload
