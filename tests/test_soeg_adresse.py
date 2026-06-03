import pytest
import responses

import adressevaelger
from adressevaelger.models import Adressesoegning, Fund


class TestAdresseSoegning:
    def test_default(self):
        search = Adressesoegning()
        assert search.tekst is None
        assert search.vejnavn is None
        assert search.husnummer is None
        assert search.postnummer is None
        assert search.kommunekode is None
        assert search.medtagforeloebige is None
        assert search.etage is None
        assert search.doer is None
        assert search.maksimum is None


class TestSoegAdresse:
    @responses.activate
    def test_soeg_adresse_fonetisk(self, client: adressevaelger.Client):
        response_body = {
            "status": "ok",
            "beskrivelse": "",
            "fund": [
                {
                    "type": "adresse",
                    "id": "0a3a20b6-7ae6-37b8-e944-0233ba298019",
                    "titel": "Vejnavn 1, 1234 By",
                    "vejnavn": "Vejnavn",
                    "husnummer": "1",
                    "postnr": "1234",
                    "postdistrikt": "By",
                    "antal_husnumre": 20,
                    "husnummerId": "0a3f508b-5d5f-32b8-e044-0003ba298018",
                }
            ],
        }
        responses.add(
            method=responses.GET,
            url=client.base_url
            + f"/adresser/soeg?vejnavn=Vejnavn&husnummer=1&postnummer=1234&kommunekode=4321&token={client.token}",
            json=response_body,
            status=200,
        )
        results = client.soeg_fonetisk(
            Adressesoegning(
                tekst="",
                vejnavn="Vejnavn",
                husnummer="1",
                postnummer="1234",
                kommunekode="4321",
            )
        )
        assert len(results) == 1
        assert results[0] == Fund(
            type="adresse",
            id="0a3a20b6-7ae6-37b8-e944-0233ba298019",
            titel="Vejnavn 1, 1234 By",
            vejnavn="Vejnavn",
            husnummer="1",
            postnr="1234",
            postdistrikt="By",
            antal_husnumre=20,
            husnummerId="0a3f508b-5d5f-32b8-e044-0003ba298018",
        )

    @responses.activate
    def test_soeg_adresse_fonetisk_no_match(self, client: adressevaelger.Client):
        response_body = {"status": "ok", "beskrivelse": "", "fund": []}
        responses.add(
            method=responses.GET,
            url=client.base_url
            + f"/adresser/soeg?vejnavn=Vejnavn&husnummer=1&postnummer=1234&kommunekode=4321&token={client.token}",
            json=response_body,
            status=200,
        )
        results = client.soeg_fonetisk(
            Adressesoegning(
                tekst="",
                vejnavn="Vejnavn",
                husnummer="1",
                postnummer="1234",
                kommunekode="4321",
            )
        )
        assert len(results) == 0
        assert results == []

    @responses.activate
    def test_soeg_adresse_fonetisk_api_error(self, client: adressevaelger.Client):
        response_body = {
            "status": "fejl",
            "beskrivelse": "Der opstod en fejl",
            "fund": [],
        }
        responses.add(
            method=responses.GET,
            url=client.base_url
            + f"/adresser/soeg?vejnavn=Vejnavn&husnummer=1&postnummer=1234&kommunekode=4321&token={client.token}",
            json=response_body,
            status=200,
        )
        with pytest.raises(adressevaelger.ApiError) as err:
            client.soeg_fonetisk(
                Adressesoegning(
                    tekst="",
                    vejnavn="Vejnavn",
                    husnummer="1",
                    postnummer="1234",
                    kommunekode="4321",
                )
            )
        assert "Der opstod en fejl" in str(err.value)
