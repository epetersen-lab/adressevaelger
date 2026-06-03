import responses

import adressevaelger
from adressevaelger.models import Fund, Husnummersoegning


class TestSoegHusnummer:
    def test_default(self):
        search = Husnummersoegning()
        assert search.tekst is None
        assert search.vejnavn is None
        assert search.husnummer is None
        assert search.postnummer is None
        assert search.kommunekode is None
        assert search.medtagforeloebige is None
        assert search.maksimum is None

    @responses.activate
    def test_soeg_husnummer_fonetisk(self, client: adressevaelger.Client):
        response_body = {
            "status": "ok",
            "beskrivelse": "",
            "fund": [
                {
                    "type": "husnummer",
                    "id": "0a3a20b6-7ae6-37b8-e944-0233ba298019",
                    "titel": "Vejnavn 1, 1234 By",
                    "vejnavn": "Vejnavn",
                    "husnummer": "1",
                    "postnr": "1234",
                    "postdistrikt": "By",
                    "antal_husnumre": 20,
                }
            ],
        }
        responses.add(
            method=responses.GET,
            url=client.base_url
            + f"/husnumre/soeg?vejnavn=Vejnavn&husnummer=1&postnummer=1234&token={client.token}",
            json=response_body,
            status=200,
        )
        results = client.soeg_fonetisk(
            Husnummersoegning(
                tekst="",
                vejnavn="Vejnavn",
                husnummer="1",
                postnummer="1234",
            )
        )
        assert len(results) == 1
        assert results[0] == Fund(
            type="husnummer",
            id="0a3a20b6-7ae6-37b8-e944-0233ba298019",
            titel="Vejnavn 1, 1234 By",
            vejnavn="Vejnavn",
            husnummer="1",
            postnr="1234",
            postdistrikt="By",
            antal_husnumre=20,
        )
