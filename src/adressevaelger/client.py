import logging
from dataclasses import asdict
from datetime import datetime, timezone
from typing import List, Optional

import requests
from dacite import Config, from_dict
from requests.adapters import HTTPAdapter
from requests.packages.urllib3.util.retry import Retry

from .exceptions import ApiConnectionError, ApiError
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
    ) -> None:
        self.base_url = base_url
        self.token = token
        self.ssl_verify = ssl_verify
        self.session = requests.Session()
        retry_strategy = Retry(
            total=3,
            status_forcelist=[429, 502, 503, 504],
            allowed_methods={"GET"},
            backoff_factor=1,
        )
        adapter = HTTPAdapter(max_retries=retry_strategy)
        self.session.mount("https://", adapter)
        self.session.mount("http://", adapter)

    def _request(self, method: str, path: str, headers: dict = {}, params: dict = {}):
        headers.update({"Accept": "application/json"})
        params.update({"token": self.token})
        try:
            response = self.session.request(
                method=method,
                url=self.base_url + f"/{path}",
                headers=headers,
                params=params,
                verify=self.ssl_verify,
            )
            logger.debug(f"Requ: {response.request.url}")
            logger.debug(
                f"Resp: Status code={response.status_code}, Payload={response.text}"
            )
            response.raise_for_status()
            return response
        except requests.ConnectionError as err:
            logger.exception(err)
            raise ApiConnectionError(str(err)) from err
        except requests.HTTPError as err:
            logger.exception(err)
            raise ApiError(response.text) from err

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
