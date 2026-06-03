from datetime import datetime, timezone

import responses

import adressevaelger


class TestHusnummerId:
    def test_husnummer_id(self, client: adressevaelger.Client):
        id = "0a3f5090-48fe-32b8-e044-0003ba298018"
        response_body = """{ 
            "status": "ok",
            "husnummer": {
                "id_lokalid": "0a3f5090-48fe-32b8-e044-0003ba298018",
                "husnummertekst": "87A",
                "adgangsadressebetegnelse": "Nr. Bjertvej 87A, Nr Bjert, 6000 Kolding",
                "vejnavn": "Nr. Bjertvej",
                "status": "3",
                "virkningfra": "2021-01-05T14:56:02.099Z",
                "virkningtil": null,
                "registreringfra": "2021-01-05T14:56:02.099Z",
                "registreringtil": null,
                "adgangspunkt": {
                    "id_lokalid": "0a3f5090-48fe-32b8-e044-0003ba298018",
                    "status": "8",
                    "virkningfra": "2018-08-09T12:05:02.078138+00:00",
                    "virkningtil": null,
                    "registreringfra": "2018-08-09T12:05:02.078138+00:00",
                    "registreringtil": null,
                    "geometri": {
                        "type": "Point",
                        "crs": {
                            "type": "name",
                            "properties": {
                                "name": "EPSG:25832"
                            }
                        },
                        "coordinates": [533640.58, 6152135.2]
                    },
                    "koordinater": {
                        "x": 533640.58,
                        "y": 6152135.2
                    }
                },
                "postnummer": 
                "id_lokalid": "3a6b09ec-cfd7-4cc9-8eed-d9f3f0e4978a",
                "navn": "Kolding",
                "postnr": "6000",
                "status": "3",
                "virkningfra": "2023-03-24T16:23:10.278819+00:00",
                "virkningtil": null,
                "registreringfra": "2023-03-24T16:23:10.278819+00:00",
                "registreringtil": null
                },
                "navngivenvej": {
                "id_lokalid": "bb1dc312-85e4-4716-905d-af17080d2c5f",
                "vejnavn": "Nr. Bjertvej",
                "virkningfra": "2026-04-25T14:14:58.864301+00:00",
                "virkningtil": null,
                "registreringfra": "2026-04-25T14:14:58.864301+00:00",
                "registreringtil": null
                },
                "navngivenvejkommunedel": {
                "id_lokalid": "5cb378e9-4eae-11e8-93fd-066cff24d637",
                "kommune": "0621",
                "vejkode": "5842",
                "navngivenvej": "bb1dc312-85e4-4716-905d-af17080d2c5f",
                "virkningfra": "2024-03-01T18:06:40.065587+00:00",
                "virkningtil": null,
                "registreringfra": "2024-03-01T18:06:40.065587+00:00",
                "registreringtil": null
                },
                "navngivenvejpostnummer": {
                "id_lokalid": "7f77286f-37bc-4dc8-9c7b-ebd0af1f93c9",
                "virkningfra": "2020-12-18T15:17:19.000774+00:00",
                "virkningtil": null,
                "registreringfra": "2020-12-18T15:17:19.000774+00:00",
                "registreringtil": null
                },
                "supplerendebynavn": {
                "id_lokalid": "542c9041-e487-4b63-8fd0-af4f5c71eaa5",
                "status": "3",
                "supplerendebynavn": "665549",
                "navn": "Nr Bjert",
                "virkningfra": "2021-01-05T14:56:02.099849+00:00",
                "virkningtil": null,
                "registreringfra": "2021-01-05T14:56:02.099849+00:00",
                "registreringtil": null
                }
            }
        }"""
        responses.add("GET", client.base_url + "husnumre/" + id, body=response_body)

        husnummer = client.husnummer_id(id)
        assert husnummer is not None
        assert husnummer.id_lokalid == id
        assert husnummer.husnummertekst == "87A"
        assert husnummer.vejnavn == "Nr. Bjertvej"
        assert husnummer.status == "3"
        assert husnummer.virkningfra == datetime(
            2021, 1, 5, 14, 56, 2, 99000, tzinfo=timezone.utc
        )
        assert husnummer.virkningtil is None
        assert husnummer.registreringfra == datetime(
            2021, 1, 5, 14, 56, 2, 99000, tzinfo=timezone.utc
        )
        assert husnummer.registreringtil is None

        assert husnummer.adgangspunkt is not None
        assert husnummer.adgangspunkt.id_lokalid == id
        assert husnummer.adgangspunkt.status == "8"
        assert husnummer.adgangspunkt.virkningfra == datetime(
            2018, 8, 9, 12, 5, 2, 78138, tzinfo=timezone.utc
        )
        assert husnummer.adgangspunkt.virkningtil is None
        assert husnummer.adgangspunkt.registreringfra == datetime(
            2018, 8, 9, 12, 5, 2, 78138, tzinfo=timezone.utc
        )
        assert husnummer.adgangspunkt.registreringtil is None

        assert husnummer.adgangspunkt.koordinater is not None
        assert husnummer.adgangspunkt.koordinater.x == 533640.58
        assert husnummer.adgangspunkt.koordinater.y == 6152135.2

        assert husnummer.adgangspunkt.geometri is not None
        assert husnummer.adgangspunkt.geometri.type == "Point"
        assert husnummer.adgangspunkt.geometri.crs is not None
        assert husnummer.adgangspunkt.geometri.crs.type == "name"
        assert husnummer.adgangspunkt.geometri.crs.properties is not None
        assert husnummer.adgangspunkt.geometri.crs.properties.name == "EPSG:25832"
        assert husnummer.adgangspunkt.geometri.coordinates == [533640.58, 6152135.2]

        assert husnummer.postnummer is not None
        assert husnummer.postnummer.id_lokalid == "3a6b09ec-cfd7-4cc9-8eed-d9f3f0e4978a"
        assert husnummer.postnummer.navn == "Kolding"
        assert husnummer.postnummer.postnr == "6000"
        assert husnummer.postnummer.status == "3"
        assert husnummer.postnummer.virkningfra == datetime(
            2023, 3, 24, 16, 23, 10, 278819, tzinfo=timezone.utc
        )
        assert husnummer.postnummer.virkningtil is None
        assert husnummer.postnummer.registreringfra == datetime(
            2023, 3, 24, 16, 23, 10, 278819, tzinfo=timezone.utc
        )
        assert husnummer.postnummer.registreringtil is None

        assert husnummer.navngivenvej is not None
        assert (
            husnummer.navngivenvej.id_lokalid == "bb1dc312-85e4-4716-905d-af17080d2c5f"
        )
        assert husnummer.navngivenvej.vejnavn == "Nr. Bjertvej"
        assert husnummer.navngivenvej.virkningfra == datetime(
            2026, 4, 25, 14, 14, 58, 864301, tzinfo=timezone.utc
        )
        assert husnummer.navngivenvej.virkningtil is None
        assert husnummer.navngivenvej.registreringfra == datetime(
            2026, 4, 25, 14, 14, 58, 864301, tzinfo=timezone.utc
        )
        assert husnummer.navngivenvej.registreringtil is None

        assert husnummer.navngivenvejkommunedel is not None
        assert (
            husnummer.navngivenvejkommunedel.id_lokalid
            == "5cb378e9-4eae-11e8-93fd-066cff24d637"
        )
        assert husnummer.navngivenvejkommunedel.kommune == "0621"
        assert husnummer.navngivenvejkommunedel.vejkode == "5842"
        assert (
            husnummer.navngivenvejkommunedel.navngivenvej
            == "bb1dc312-85e4-4716-905d-af17080d2c5f"
        )
        assert husnummer.navngivenvejkommunedel.virkningfra == datetime(
            2024, 3, 1, 18, 6, 40, 65587, tzinfo=timezone.utc
        )
        assert husnummer.navngivenvejkommunedel.virkningtil is None
        assert husnummer.navngivenvejkommunedel.registreringfra == datetime(
            2024, 3, 1, 18, 6, 40, 65587, tzinfo=timezone.utc
        )
        assert husnummer.navngivenvejkommunedel.registreringtil is None

        assert husnummer.navngivenvejpostnummer is not None
        assert (
            husnummer.navngivenvejpostnummer.id_lokalid
            == "7f77286f-37bc-4dc8-9c7b-ebd0af1f93c9"
        )
        assert husnummer.navngivenvejpostnummer.virkningfra == datetime(
            2020, 12, 18, 15, 17, 19, 774, tzinfo=timezone.utc
        )
        assert husnummer.navngivenvejpostnummer.virkningtil is None
        assert husnummer.navngivenvejpostnummer.registreringfra == datetime(
            2020, 12, 18, 15, 17, 19, 774, tzinfo=timezone.utc
        )
        assert husnummer.navngivenvejpostnummer.registreringtil is None

        assert husnummer.supplerendebynavn is not None
        assert (
            husnummer.supplerendebynavn.id_lokalid
            == "542c9041-e487-4b63-8fd0-af4f5c71eaa5"
        )
        assert husnummer.supplerendebynavn.status == "3"
        assert husnummer.supplerendebynavn.supplerendebynavn == "665549"
        assert husnummer.supplerendebynavn.navn == "Nr Bjert"
        assert husnummer.supplerendebynavn.virkningfra == datetime(
            2021, 1, 5, 14, 56, 2, 99849, tzinfo=timezone.utc
        )
        assert husnummer.supplerendebynavn.virkningtil is None
        assert husnummer.supplerendebynavn.registreringfra == datetime(
            2021, 1, 5, 14, 56, 2, 99849, tzinfo=timezone.utc
        )
        assert husnummer.supplerendebynavn.registreringtil is None
