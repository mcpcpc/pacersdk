"""
Data models for case search requests and responses in the PACER API.
"""

from typing import List
from typing import Optional
from typing import TypedDict

from .common import BaseCaseSearch
from .common import CourtCase
from .common import ReceiptInfo
from .common import PageInfo


class CaseSearchRequest(BaseCaseSearch, total=False):
    """
    Request model for case search criteria.
    Inherits shared filters from BaseCaseSearch.
    """

    pass


class CaseRecord(TypedDict):
    """
    Individual result item returned in the search response.
    """

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


class CaseSearchResponse(TypedDict):
    """
    Full API response for a case search request.
    """

    receipt: ReceiptInfo
    pageInfo: PageInfo
    content: List[CaseRecord]
