"""
Models for specifying sort fields for search results.
"""

from typing import Literal
from typing import TypedDict


class SortableCaseField(TypedDict):
    """
    Represents a sortable field and direction for case search.
    """

    field: Literal[
        "courtId",
        "caseId",
        "caseYear",
        "caseNumber",
        "caseOffice",
        "caseType",
        "caseTitle",
        "dateFiled",
        "effectiveDateClosed",
        "dateReopened",
        "dateDismissed",
        "dateDischarged",
        "bankrupctyChapter",
        "dispositionMethod",
        "jointDispositionMethod",
        "jointDismissedDate",
        "jointDischargedDate",
        "jointBankruptcyFlag",
        "natureOfSuit",
        "jurisdictionType",
        "jpmlNumber",
        "mdlCourtId",
        "civilDateInitiate",
        "civilDateDisposition",
        "civilDateTerminated",
        "civilStatDisposition",
        "civilStatTerminated",
        "civilCtoNumber",
        "civilTransferee",
        "mdlExtension",
        "mdlTransfereeDistrict",
        "mdlLittype",
        "mdlStatus",
        "mdlDateReceived",
        "mdlDateOrdered",
        "mdlTransferee",
    ]
    order: Literal["ASC", "DESC"]


class SortablePartyField(TypedDict):
    """
    Represents a sortable field and direction for party search.
    """

    field: Literal[
        "courtId",
        "caseId",
        "caseYear",
        "caseNumber",
        "lastName",
        "firstName",
        "middleName",
        "generation",
        "partyType",
        "role",
        "jurisdictionType",
        "seqNo",
        "aliasEq",
        "aliasType",
        "description",
    ]
    order: Literal["ASC", "DESC"]
