import pytest
import requests
import responses

import adressevaelger
from adressevaelger.exceptions import ApiConnectionError, ApiError
from adressevaelger.models import Adressesoegning


class TestClient:
    def test_default_url(self, client: adressevaelger.Client):
        assert client.base_url == "https://adressevaelger.dk"

    def test_default_token(self, client: adressevaelger.Client):
        assert client.token == "adressevaelger123"

    @responses.activate
    def test_connection_error(self, client: adressevaelger.Client):
        responses.add(
            method=responses.GET,
            url=client.base_url + f"/adresser/soeg?token={client.token}",
            body=requests.ConnectionError(),
        )
        with pytest.raises(ApiConnectionError):
            client.soeg_fonetisk(Adressesoegning())

    @responses.activate
    def test_server_error(self, client: adressevaelger.Client):
        responses.add(
            method=responses.GET,
            url=client.base_url + f"/adresser/soeg?token={client.token}",
            body="",
            status=500
        )
        with pytest.raises(ApiError):
            client.soeg_fonetisk(Adressesoegning())
