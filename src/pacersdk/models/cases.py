"""
TypedDict models representing PACER case metadata.

Defines `BaseCourtCase`, `CourtCase`, and related structures used to
describe court case information, including jurisdiction, dates, and case identifiers.
"""

from typing import List, Optional, TypedDict

from .billing import PageInfo, Receipt
from .types import Character, Date, JurisdictionType


class BaseCourtCase(TypedDict):
    courtId: str
    caseId: str
    caseYear: int
    caseNumber: int
    caseNumberFull: str
    caseOffice: str
    caseType: str
    caseTitle: str
    bankruptcyChapter: str
    dispositionMethod: str
    jointDispositionMethod: str
    jointBankruptcyFlag: Character
    natureOfSuit: str
    jurisdictionType: JurisdictionType
    jpmlNumber: Optional[int]
    mdlCourtId: str
    civilStatInitiated: str
    civilStatDisposition: str
    civilStatTerminated: str
    civilCtoNumber: str
    civilTransferee: str
    mdlExtension: str
    mdlTransfereeDistrict: str
    mdlLitType: str
    mdlStatus: str
    mdlTransferee: str
    judgeLastName: str
    caseLink: str
    dateFiled: Date
    dateTermed: Date
    dateReopened: Date
    dateDismissed: Date
    dateDischarged: Date
    jointDismissedDate: Date
    jointDischargedDate: Date
    civilDateInitiated: Date
    civilDateDisposition: Date
    civilDateTerminated: Date
    mdlDateReceived: Date
    mdlDateOrdered: Date


class CourtCase(BaseCourtCase):
    receipt: Optional[Receipt]


class CourtCaseList(TypedDict):
    receipt: Optional[Receipt]
    pageInfo: Optional[PageInfo]
    masterCase: Optional[BaseCourtCase]
    content: List[BaseCourtCase]


class CourtCases(TypedDict):
    receipt: Optional[Receipt]
    pageInfo: Optional[PageInfo]
    masterCase: Optional[BaseCourtCase]
    content: List[BaseCourtCase]


class SimpleCourtCaseList(TypedDict):
    case: List[BaseCourtCase]


class CourtCaseListContent(TypedDict):
    case: List[BaseCourtCase]
