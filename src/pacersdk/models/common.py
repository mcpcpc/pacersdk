"""
Common models shared across multiple API response types.
"""

from typing import List
from typing import TypedDict


class ReceiptInfo(TypedDict):
    """
    Receipt metadata for tracking billing and usage.
    """

    transactionDate: str
    billablePages: int
    loginId: str
    search: str
    description: str
    csoId: int
    reportId: str
    searchFee: str


class PageInfo(TypedDict):
    """
    Metadata about paginated result sets.
    """

    number: int
    size: int
    totalPages: int
    totalElements: int
    numberOfElements: int
    first: bool
    last: bool


class CourtCase(TypedDict):
    """
    Additional case detail attached to each record in the response.
    """

    caseNumberFull: str
    caseYearFrom: str
    caseYearTo: str
    jmplNumber: int
    caseOffice: str
    caseType: List[str]
    caseTitle: str
    dateFiledFrom: str
    dateFiledTo: str
    effectiveDateClosedFrom: str
    effectiveDateClosedTo: str
    dateReopenedFrom: str
    dateReopenedTo: str
    dateDismissedTo: str
    dateDismissedFrom: str
    dateDischargedTo: str
    dateDischargedFrom: str
    federalBankruptcyChapter: List[str]
    dispositionMethod: str
    dispoMethodJt: str
    dateDismissedJtFrom: str
    dateDismissedJtTo: str
    caseJoint: str
    jurisdictionType: str
    natureOfSuit: List[str]
    caseStatus: str


class BaseCaseSearch(TypedDict, total=False):
    """
    Common fields used in both CaseSearchRequest and BatchCaseRequest.
    """

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
    federalBankruptcyChapter: List[str]
    dateDismissedFrom: str
    dateDismissedTo: str
    natureOfSuit: List[str]
    jpmlNumber: int


class BasePartySearch(TypedDict, total=False):
    """
    Common fields used in both PartySearchRequest and BatchPartyRequest.
    """

    reportId: str
    courtId: List[str]
    caseId: int
    caseNumberFull: str
    lastName: str
    firstName: str
    middleName: str
    generation: str
    partyType: str
    role: List[str]
    exactNameMatch: bool
    caseYearFrom: str
    caseYearTo: str
    jurisdictionType: str
    ssn: str
    ssn4: str
