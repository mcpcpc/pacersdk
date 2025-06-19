from typing import List
from typing import Optional
from typing import TypedDict

from .types import Date
from .types import JurisdictionType
from .billing import PageInfo
from .billing import Receipt
from .cases import CourtCase


class BaseParty(TypedDict):
    """
    Basic party information associated with a court case.
    """
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
    """
    A list of parties with associated metadata and optional receipt.
    """
    receipt: Optional[Receipt]
    pageInfo: Optional[PageInfo]
    masterCase: Optional[CourtCase]
    content: List[BaseParty]


class PartyListXml(TypedDict):
    """
    XML-wrapped party list structure.
    """
    receipt: Receipt
    pageInfo: Optional[PageInfo]
    content: List[BaseParty]


class Parties(TypedDict):
    """
    A variation of the party list with optional receipt and parties.
    """
    receipt: Optional[Receipt]
    pageInfo: Optional[PageInfo]
    content: Optional[List[BaseParty]]


class PartyType(TypedDict):
    """
    Container for a single party with an optional receipt.
    """
    receipt: Optional[Receipt]
    item: Optional[BaseParty]
