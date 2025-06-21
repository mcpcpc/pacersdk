"""
TypedDict models for search query criteria and responses.

Includes reusable criteria structures for querying the PACER system,
including `GenericSearchCriteria`, `CombinedSearchCriteria`, and others.
"""

from typing import List, Optional, TypedDict

from .billing import PageInfo, Receipt
from .types import Character, Date


class GenericSearchCriteria(TypedDict, total=False):
    courtId: List[str]
    reportId: str
    caseId: str
    caseYear: Optional[int]
    caseYearFrom: Optional[int]
    caseYearTo: Optional[int]
    caseNumber: Optional[int]
    jurisdictionType: str
    page: str
    searchType: str
    requestType: str
    requestSource: str


class CourtSearchCriteria(TypedDict):
    courtId: Optional[List[str]]
    courtName: str
    courtType: str
    beginDateFrom: Date
    beginDateTo: Date
    endDateFrom: Date
    endDateTo: Date
    page: str
    searchType: str


class BaseCourtCaseSearchCriteria(GenericSearchCriteria, total=False):
    nos: Optional[List[str]]
    caseNumberFull: str
    jpmlNumber: Optional[int]
    caseOffice: str
    caseType: Optional[List[str]]
    caseTitle: str
    dateFiledFrom: Date
    dateFiledTo: Date
    dateTermedFrom: Date
    dateTermedTo: Date
    dateReopenedFrom: Date
    dateReopenedTo: Date
    dateDismissedFrom: Date
    dateDismissedTo: Date
    dateDischargedFrom: Date
    dateDischargedTo: Date
    federalBankruptcyChapter: Optional[List[str]]
    dispositionMethod: str
    dispMethodJt: str
    dateDismissJtFrom: Date
    dateDismissJtTo: Date
    dateDischargeJtFrom: Date
    dateDischargeJtTo: Date
    caseJoint: Character


class BasePartySearchCriteria(GenericSearchCriteria, total=False):
    role: Optional[List[str]]
    lastName: str
    firstName: str
    middleName: str
    generation: str
    partyType: str
    seqNo: Optional[int]
    aliasEq: Optional[int]
    exactNameMatch: Optional[bool]
    aliasType: str
    description: str
    ssn: str
    ssn4: str


class CourtCaseSearchCriteria(BaseCourtCaseSearchCriteria, total=False):
    party: Optional[BasePartySearchCriteria]


class PartySearchCriteria(BasePartySearchCriteria, total=False):
    courtCase: Optional[BaseCourtCaseSearchCriteria]


class CombinedSearchCriteria(BaseCourtCaseSearchCriteria, total=False):
    party: Optional[BasePartySearchCriteria]
    courtCase: Optional[BaseCourtCaseSearchCriteria]
    role: Optional[List[str]]
    lastName: str
    firstName: str
    middleName: str
    generation: str
    partyType: str
    seqNo: Optional[int]
    aliasEq: Optional[int]
    exactNameMatch: Optional[bool]
    aliasType: str
    description: str
    ssn: str
    ssn4: str


class BaseSearchResult(TypedDict):
    courtId: str
    caseId: str
    caseYear: int
    caseNumber: int
    caseNumberFull: str
    caseOffice: str
    caseType: str
    caseTitle: str
    dateFiled: Date
    dateTermed: Date
    dateReopened: Date
    dateDismissed: Date
    dateDischarged: Date
    bankruptcyChapter: str
    dispositionMethod: str
    jointDispositionMethod: str
    jointDismissDate: Date
    jointDischargeDate: Date
    jointBankruptcyFlag: Character
    natureOfSuit: str


class CourtCaseSearchResult(BaseSearchResult):
    mdlCaseNumber: int
    mdlCourtId: str
    mdlDateOrdered: Date
    mdlDateReceived: Date
    mdlExtension: str
    mdlLitType: str
    mdlStatus: str
    mdlTransfereeDistrict: str
    judgeLastName: str
    civilCtoNumber: str
    civilStatDisposition: str
    civilStatInitiated: str
    civilStatTerminated: str
    civilTransferee: str
    civilDateDisposition: Date
    civilDateInitiated: Date
    civilDateTerminated: Date
    caseLink: str


class PartySearchResult(BaseSearchResult):
    lastName: str
    firstName: str
    middleName: str
    generation: str
    partyType: str
    partyRole: str
    disposition: str
    caseLink: str


class CourtSearchResult(TypedDict):
    courtId: str
    courtName: str
    courtType: str
    beginDate: Date
    endDate: Date
    url: str


class BaseSearchResults(TypedDict, total=False):
    receipt: Optional[Receipt]
    pageInfo: Optional[PageInfo]


class SearchContent(TypedDict, total=False):
    courtCase: Optional[List[CourtCaseSearchResult]]
    party: Optional[List[PartySearchResult]]
    court: Optional[List[CourtSearchResult]]
