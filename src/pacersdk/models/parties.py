from typing import List
from typing import Optional
from typing import TypedDict

from .billing import PageInfo
from .billing import Receipt
from .cases import CourtCase
from .types import Date
from .types import JurisdictionType


class BaseParty(TypedDict):
    courtId: str
    caseId: str
    caseYear: int
    caseNumber: int
    lastName: str
    firstName: str
    middleName: str
    generation: str
    partyType: str
    partyRole: str
    jurisdictionType: JurisdictionType
    courtCase: Optional[CourtCase]
    caseNumberFull: str
    caseOffice: str
    caseTitle: str
    caseType: str
    dateFiled: Date
    dateTermed: Date
    natureOfSuit: str
    bankruptcyChapter: str
    disposition: str
    seqNo: Optional[int]
    aliasEq: Optional[int]
    aliasType: str
    description: str
    dateDischarged: Date
    dateDismissed: Date


class PartyList(TypedDict):
    receipt: Optional[Receipt]
    pageInfo: Optional[PageInfo]
    masterCase: Optional[CourtCase]
    content: List[BaseParty]


class PartyListXml(TypedDict):
    receipt: Receipt
    pageInfo: Optional[PageInfo]
    content: List[BaseParty]


class Parties(TypedDict):
    receipt: Optional[Receipt]
    pageInfo: Optional[PageInfo]
    content: Optional[List[BaseParty]]


class PartyType(TypedDict):
    receipt: Optional[Receipt]
    item: Optional[BaseParty]
