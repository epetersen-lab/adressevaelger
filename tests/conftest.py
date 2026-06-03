import pytest

import adressevaelger


@pytest.fixture(scope="package")
def client() -> adressevaelger.Client:
    return adressevaelger.Client()
