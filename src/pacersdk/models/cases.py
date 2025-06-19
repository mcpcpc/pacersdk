from typing import List
from typing import Optional
from typing import TypedDict

from .types import Character
from .types import Date
from .types import JurisdictionType
from .billing import PageInfo
from .billing import Receipt


class BaseCourtCase(TypedDict):
    """
    Core case information as defined by BaseCourtCaseType.
    """
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
    """
    Extended court case with optional receipt, as defined by CourtCaseType.
    """
    receipt: Optional[Receipt]


class CourtCaseList(TypedDict):
    """
    Case list structure with optional receipt, pageInfo, master case, and content cases.
    """
    receipt: Optional[Receipt]
    pageInfo: Optional[PageInfo]
    masterCase: Optional[BaseCourtCase]
    content: List[BaseCourtCase]


class CourtCaseListXml(TypedDict):
    """
    Wrapper for court case list XML with receipt, optional pageInfo, and list of cases.
    """
    receipt: Receipt
    pageInfo: Optional[PageInfo]
    content: List[BaseCourtCase]


class CourtCases(TypedDict):
    """
    Similar to CourtCaseList, representing an alternate list format.
    """
    receipt: Optional[Receipt]
    pageInfo: Optional[PageInfo]
    masterCase: Optional[BaseCourtCase]
    content: List[BaseCourtCase]


class SimpleCourtCaseList(TypedDict):
    """
    Simple case list with a flat list of cases.
    """
    case: List[BaseCourtCase]


class CourtCaseListContent(TypedDict):
    """
    Variant of SimpleCourtCaseList with an identical structure.
    """
    case: List[BaseCourtCase]
