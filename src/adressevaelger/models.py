import datetime
from dataclasses import dataclass, asdict
from typing import List, Optional


@dataclass
class Adressesoegning:
    tekst: Optional[str] = None
    vejnavn: Optional[str] = None
    husnummer: Optional[str] = None
    postnummer: Optional[str] = None
    kommunekode: Optional[str] = None
    medtagforeloebige: Optional[str] = None
    etage: Optional[str] = None
    doer: Optional[str] = None
    maksimum: Optional[int] = None


@dataclass
class Husnummersoegning:
    tekst: Optional[str] = None
    vejnavn: Optional[str] = None
    husnummer: Optional[str] = None
    postnummer: Optional[str] = None
    kommunekode: Optional[str] = None
    medtagforeloebige: Optional[str] = None
    maksimum: Optional[int] = None


@dataclass
class Fund:
    type: str
    id: str
    titel: Optional[str] = None
    vejnavn: Optional[str] = None
    husnummer: Optional[str] = None
    postnr: Optional[str] = None
    postdistrikt: Optional[str] = None
    antal_husnumre: Optional[int] = None
    husnummerId: Optional[str] = None

    def asdict(self):
        return asdict(self)


@dataclass
class Soegeresultat:
    status: str
    beskrivelse: str
    fund: List[Fund]


@dataclass
class Koordinater:
    x: Optional[float]
    y: Optional[float]


@dataclass
class CRSProperties:
    name: Optional[str]


@dataclass
class CRS:
    type: Optional[str]
    properties: Optional[CRSProperties]


@dataclass
class Geometri:
    type: Optional[str]
    crs: Optional[CRS]
    coordinates: Optional[List[float]]


@dataclass
class Adgangspunkt:
    id_lokalid: Optional[str]
    status: Optional[str]
    virkningfra: Optional[datetime.datetime]
    virkningtil: Optional[datetime.datetime]
    registreringfra: Optional[datetime.datetime]
    registreringtil: Optional[datetime.datetime]
    geometri: Optional[Geometri]
    koordinater: Optional[Koordinater]


@dataclass
class Postnummer:
    id_lokalid: Optional[str]
    navn: Optional[str]
    postnr: Optional[str]
    status: Optional[str]
    virkningfra: Optional[datetime.datetime]
    virkningtil: Optional[datetime.datetime]
    registreringfra: Optional[datetime.datetime]
    registreringtil: Optional[datetime.datetime]


@dataclass()
class NavngivenVej:
    id_lokalid: Optional[str]
    vejnavn: Optional[str]
    virkningfra: Optional[datetime.datetime]
    virkningtil: Optional[datetime.datetime]
    registreringfra: Optional[datetime.datetime]
    registreringtil: Optional[datetime.datetime]


@dataclass()
class NavngivenVejKommunedel:
    id_lokalid: Optional[str]
    kommune: Optional[str]
    vejkode: Optional[str]
    navngivenvej: Optional[str]
    virkningfra: Optional[datetime.datetime]
    virkningtil: Optional[datetime.datetime]
    registreringfra: Optional[datetime.datetime]
    registreringtil: Optional[datetime.datetime]


@dataclass()
class NavngivenVejPostnummer:
    id_lokalid: Optional[str]
    virkningfra: Optional[datetime.datetime]
    virkningtil: Optional[datetime.datetime]
    registreringfra: Optional[datetime.datetime]
    registreringtil: Optional[datetime.datetime]


@dataclass()
class SupplerendeBynavn:
    id_lokalid: Optional[str]
    status: Optional[str]
    supplerendebynavn: Optional[str]
    navn: Optional[str]
    virkningfra: Optional[datetime.datetime]
    virkningtil: Optional[datetime.datetime]
    registreringfra: Optional[datetime.datetime]
    registreringtil: Optional[datetime.datetime]


@dataclass
class Husnummer:
    id_lokalid: str
    husnummertekst: Optional[str]
    adgangsadressebetegnelse: Optional[str]
    vejnavn: Optional[str]
    status: Optional[str]
    virkningfra: Optional[datetime.datetime]
    virkningtil: Optional[datetime.datetime]
    registreringfra: Optional[datetime.datetime]
    registreringtil: Optional[datetime.datetime]
    adgangspunkt: Optional[Adgangspunkt]
    postnummer: Optional[Postnummer]
    navngivenvej: Optional[NavngivenVej]
    navngivenvejkommunedel: Optional[NavngivenVejKommunedel]
    navngivenvejpostnummer: Optional[NavngivenVejPostnummer]
    supplerendebynavn: Optional[SupplerendeBynavn]


@dataclass
class Husnummeropslag:
    status: str
    husnummer: Husnummer


@dataclass
class Adresse:
    id_lokalid: str
    adressebetegnelse: Optional[str]
    etagebetegnelse: Optional[str]
    doerbetegnelse: Optional[str]
    status: Optional[str]
    virkningfra: Optional[datetime.datetime]
    virkningtil: Optional[datetime.datetime]
    registreringfra: Optional[datetime.datetime]
    registreringtil: Optional[datetime.datetime]
    husnummer: Optional[Husnummer]


@dataclass
class Adresseopslag:
    status: Optional[str]
    adresse: Optional[Adresse]
