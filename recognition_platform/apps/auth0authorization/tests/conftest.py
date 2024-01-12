import pytest
from rest_framework.test import APIClient
from rest_framework.authtoken.models import Token


@pytest.fixture()
def inject_attrs(request, api_client):
    request.cls.api_client = api_client


@pytest.fixture()
def api_client():
    return APIClient()


def get_token(api_client, user):
    token, _ = Token.objects.get_or_create(user=user)
    api_client.credentials(HTTP_AUTHORIZATION='Token ' + token.key)
    return api_client
