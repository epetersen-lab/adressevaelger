import pytest

import adressevaelger


@pytest.fixture(scope="package")
def client() -> adressevaelger.Client:
    return adressevaelger.Client(
        base_url="https://adressevaelger.local", max_retries=2, initial_backoff=1
    )
