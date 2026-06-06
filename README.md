# Adressevælger API Client

## Introduction

Client library for accessing "Adressevælger" Web API.

- [API Documentation](https://confluence.sdfi.dk/pages/viewpage.action?pageId=234782998)
- [API Base Address](https://adressevaelger.dk)


## Example

```python
import adressevaelger
from adressevaelger import Adressesoegning, Husnummersoegning


def main():
    client = adressevaelger.Client()
    try:
        print("Adresse søgning:")
        results = client.soeg_fonetisk(
            Adressesoegning(vejnavn="sankt keld", husnummer="11", postnummer="2100")
        )
        adresse_id = ""
        for result in results:
            adresse_id = result.id
            print(result)

        print("\nAdresse id opslag:")
        result = client.adresse_id(adresse_id=adresse_id)
        print(result)

        print("\nHusnummer søgning:")
        results = client.soeg_fonetisk(
            Husnummersoegning(vejnavn="sankt keld", husnummer="11", postnummer="2100")
        )
        husnummer_id = ""
        for result in results:
            husnummer_id = result.id
            print(result)

        print("\nHusnummer id opslag:")
        result = client.husnummer_id(husnummer_id=husnummer_id)
        print(result)

    except adressevaelger.ApiConnectionError as err:
        print(err)
    except adressevaelger.ApiError as err:
        print(err)


if __name__ == "__main__":
    main()
´´´
