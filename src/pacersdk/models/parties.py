"""
TypedDict models related to parties in PACER cases.

Defines `BaseParty`, `Party`, and `PartyList` to represent individual
and grouped search results for litigants and other involved persons/entities.
"""

from typing import List, Optional, TypedDict

from .billing import PageInfo, Receipt
from .cases import CourtCase
from .types import Date, JurisdictionType


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


class Parties(TypedDict):
    receipt: Optional[Receipt]
    pageInfo: Optional[PageInfo]
    content: Optional[List[BaseParty]]


class PartyType(TypedDict):
    receipt: Optional[Receipt]
    item: Optional[BaseParty]
