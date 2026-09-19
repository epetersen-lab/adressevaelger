import datetime
from dataclasses import asdict, dataclass


@dataclass
class Adressesoegning:
    tekst: str | None = None
    vejnavn: str | None = None
    husnummer: str | None = None
    postnummer: str | None = None
    kommunekode: str | None = None
    medtagforeloebige: str | None = None
    etage: str | None = None
    doer: str | None = None
    maksimum: int | None = None


@dataclass
class Husnummersoegning:
    tekst: str | None = None
    vejnavn: str | None = None
    husnummer: str | None = None
    postnummer: str | None = None
    kommunekode: str | None = None
    medtagforeloebige: str | None = None
    maksimum: int | None = None


@dataclass
class Fund:
    type: str
    id: str
    titel: str | None = None
    vejnavn: str | None = None
    husnummer: str | None = None
    postnr: str | None = None
    postdistrikt: str | None = None
    antal_husnumre: int | None = None
    husnummerId: str | None = None

    def asdict(self):
        return asdict(self)


@dataclass
class Soegeresultat:
    status: str
    beskrivelse: str
    fund: list[Fund]


@dataclass
class Koordinater:
    x: float | None
    y: float | None


@dataclass
class CRSProperties:
    name: str | None


@dataclass
class CRS:
    type: str | None
    properties: CRSProperties | None


@dataclass
class Geometri:
    type: str | None
    crs: CRS | None
    coordinates: list[float] | None


@dataclass
class Adgangspunkt:
    id_lokalid: str | None
    status: str | None
    virkningfra: datetime.datetime | None
    virkningtil: datetime.datetime | None
    registreringfra: datetime.datetime | None
    registreringtil: datetime.datetime | None
    geometri: Geometri | None
    koordinater: Koordinater | None


@dataclass
class Postnummer:
    id_lokalid: str | None
    navn: str | None
    postnr: str | None
    status: str | None
    virkningfra: datetime.datetime | None
    virkningtil: datetime.datetime | None
    registreringfra: datetime.datetime | None
    registreringtil: datetime.datetime | None


@dataclass()
class NavngivenVej:
    id_lokalid: str | None
    vejnavn: str | None
    virkningfra: datetime.datetime | None
    virkningtil: datetime.datetime | None
    registreringfra: datetime.datetime | None
    registreringtil: datetime.datetime | None


@dataclass()
class NavngivenVejKommunedel:
    id_lokalid: str | None
    kommune: str | None
    vejkode: str | None
    navngivenvej: str | None
    virkningfra: datetime.datetime | None
    virkningtil: datetime.datetime | None
    registreringfra: datetime.datetime | None
    registreringtil: datetime.datetime | None


@dataclass()
class NavngivenVejPostnummer:
    id_lokalid: str | None
    virkningfra: datetime.datetime | None
    virkningtil: datetime.datetime | None
    registreringfra: datetime.datetime | None
    registreringtil: datetime.datetime | None


@dataclass()
class SupplerendeBynavn:
    id_lokalid: str | None
    status: str | None
    supplerendebynavn: str | None
    navn: str | None
    virkningfra: datetime.datetime | None
    virkningtil: datetime.datetime | None
    registreringfra: datetime.datetime | None
    registreringtil: datetime.datetime | None


@dataclass
class Husnummer:
    id_lokalid: str
    husnummertekst: str | None
    adgangsadressebetegnelse: str | None
    vejnavn: str | None
    status: str | None
    virkningfra: datetime.datetime | None
    virkningtil: datetime.datetime | None
    registreringfra: datetime.datetime | None
    registreringtil: datetime.datetime | None
    adgangspunkt: Adgangspunkt | None
    postnummer: Postnummer | None
    navngivenvej: NavngivenVej | None
    navngivenvejkommunedel: NavngivenVejKommunedel | None
    navngivenvejpostnummer: NavngivenVejPostnummer | None
    supplerendebynavn: SupplerendeBynavn | None


@dataclass
class Husnummeropslag:
    status: str
    husnummer: Husnummer


@dataclass
class Adresse:
    id_lokalid: str
    adressebetegnelse: str | None
    etagebetegnelse: str | None
    doerbetegnelse: str | None
    status: str | None
    virkningfra: datetime.datetime | None
    virkningtil: datetime.datetime | None
    registreringfra: datetime.datetime | None
    registreringtil: datetime.datetime | None
    husnummer: Husnummer | None


@dataclass
class Adresseopslag:
    status: str | None
    adresse: Adresse | None
