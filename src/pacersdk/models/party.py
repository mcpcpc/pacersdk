"""
Data models for party search requests and responses in the PACER API.
"""

from typing import List
from typing import Optional
from typing import TypedDict

from .common import BasePartySearch
from .common import CourtCase
from .common import ReceiptInfo
from .common import PageInfo


class PartySearchRequest(BasePartySearch, total=False):
    """
    Request model for party search criteria.
    Inherits all optional filters from BasePartySearch.
    """

    pass


class PartyRecord(TypedDict):
    """
    Individual result item returned in the party search response.
    """

    lastName: str
    firstName: str
    middleName: str
    generation: str
    partyType: str
    partyRole: str
    caseLink: str
    jurisdictionType: str
    caseId: int
    caseNumberFull: str
    caseTitle: str
    caseOffice: str
    caseNumber: str
    caseType: List[str]
    caseYear: str
    courtId: List[str]
    dateFiledFrom: str
    dateFiledTo: str
    effectiveDateClosedFrom: str
    effectiveDateClosedTo: str
    courtCase: CourtCase


class PartySearchResponse(TypedDict):
    """
    Full API response for a party search request.
    """

    receipt: ReceiptInfo
    pageInfo: PageInfo
    content: List[PartyRecord]
