import logging
from dataclasses import asdict
from datetime import datetime, timezone
from time import sleep
from typing import List, Optional

import requests
from dacite import Config, from_dict

from .exceptions import (
    ApiConnectionError,
    ApiError,
    ApiRetryError,
    ApiTooManyRequests,
)
from .models import (
    Adresse,
    Adresseopslag,
    Adressesoegning,
    Fund,
    Husnummer,
    Husnummeropslag,
    Husnummersoegning,
    Soegeresultat,
)

logger = logging.getLogger(__name__)
logger.addHandler(logging.NullHandler())


def parse_iso_z(value: str) -> datetime:
    """Convert string into datetime type."""
    if value.endswith("Z"):
        return datetime.fromisoformat(value[:-1]).replace(tzinfo=timezone.utc)
    return datetime.fromisoformat(value)


class Client:
    def __init__(
        self,
        base_url: str = "https://adressevaelger.dk",
        token: str = "adressevaelger123",
        ssl_verify: bool = True,
        max_retries: int = 5,
        initial_backoff: int = 5,
    ) -> None:
        self.base_url = base_url
        self.token = token
        self.ssl_verify = ssl_verify
        self.session = requests.Session()
        self.max_retries = max_retries
        self.initial_backoff = initial_backoff

    def _request(
        self, method: str, path: str, headers: dict = {}, params: dict = {}
    ) -> requests.Response:
        headers.update({"Accept": "application/json"})
        params.update({"token": self.token})
        retry_count = -1
        backoff_seconds = self.initial_backoff
        while retry_count < self.max_retries:
            retry_count += 1
            try:
                response = requests.request(
                    method=method,
                    url=self.base_url + f"/{path}",
                    headers=headers,
                    params=params,
                )
                logger.debug(f"Requ: {response.request.url}")
                logger.debug(
                    f"Resp: Status code={response.status_code}, Payload={response.text}"
                )
                response.raise_for_status()
                return response

            except requests.ConnectionError as err:
                logger.exception(err)
                if retry_count >= self.max_retries:
                    raise ApiConnectionError(err.strerror) from err

            except requests.HTTPError as err:
                logger.exception(err)
                if response.status_code == 429:
                    if retry_count >= self.max_retries:
                        raise ApiTooManyRequests("Too many requests") from err
                sleep(backoff_seconds)
                backoff_seconds *= 2
        raise ApiRetryError("Max retry limit reached")

    def soeg_fonetisk(
        self, soegning: Adressesoegning | Husnummersoegning
    ) -> List[Fund]:
        """Search for 'Adresser' or 'Husnumre'."""
        if isinstance(soegning, Adressesoegning):
            response = self._request("GET", "adresser/soeg", params=asdict(soegning))
        elif isinstance(soegning, Husnummersoegning):
            response = self._request("GET", "husnumre/soeg", params=asdict(soegning))
        result = from_dict(data_class=Soegeresultat, data=response.json())
        if result.status == "ok":
            return result.fund
        else:
            raise ApiError(result.beskrivelse)

    def husnummer_id(self, husnummer_id: str) -> Husnummer | None:
        """Lookup 'Husnummer' by id."""
        config = Config(type_hooks={datetime: parse_iso_z})
        response = self._request("GET", f"husnumre/{husnummer_id}")
        result = from_dict(
            data_class=Husnummeropslag, data=response.json(), config=config
        )
        if result.status == "ok":
            return result.husnummer
        else:
            return None

    def adresse_id(self, adresse_id: str) -> Optional[Adresse]:
        """Lookup 'Adresse' by id."""
        config = Config(type_hooks={datetime: parse_iso_z})
        response = self._request("GET", f"adresser/{adresse_id}")
        result = from_dict(
            data_class=Adresseopslag, data=response.json(), config=config
        )
        if result.status == "ok":
            return result.adresse
        else:
            return None
