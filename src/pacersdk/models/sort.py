"""
TypedDict models for specifying sortable fields in search queries.

Provides structures such as `CaseField` and `PartyField`
to customize result ordering for PACER queries.
"""

from typing import Literal, TypedDict


class CaseField(TypedDict):
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


class PartyField(TypedDict):
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
