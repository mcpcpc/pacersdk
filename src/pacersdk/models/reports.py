"""
TypedDict models for report generation and sorting.

Defines report-specific models such as `ReportSortInfo`, along with
structures to support combined search and reporting functionality in PACER.
"""

from typing import List, Optional, TypedDict

from .billing import PageInfo, Receipt
from .query import (
    CombinedSearchCriteria,
    BasePartySearchCriteria,
    CourtCaseSearchCriteria,
    CourtCaseSearchResult,
    PartySearchResult,
)
from .types import DateTime, Money


class ReportSortInfo(TypedDict):
    direction: str
    property: str
    ignoreCase: bool
    nullHandling: str


class ReportSortInfoList(TypedDict):
    orders: List[ReportSortInfo]


class ReportInfo(TypedDict):
    reportId: int
    status: str
    startTime: DateTime
    endTime: DateTime
    recordCount: int
    unbilledPageCount: int
    downloadFee: Money
    pages: int
    criteria: Optional[CombinedSearchCriteria]
    partyCriteria: Optional[BasePartySearchCriteria]
    caseCriteria: Optional[CourtCaseSearchCriteria]
    searchType: str
    sort: List[ReportSortInfo]


class ReportList(TypedDict):
    pageInfo: Optional[PageInfo]
    receipt: Optional[Receipt]
    content: List[ReportInfo]


class Download(TypedDict):
    receipt: Optional[Receipt]
    pageInfo: Optional[PageInfo]
    courtCase: Optional[List[CourtCaseSearchResult]]
    party: Optional[List[PartySearchResult]]


class CaseDownload(TypedDict):
    receipt: Optional[Receipt]
    pageInfo: Optional[PageInfo]
    content: Optional[List[CourtCaseSearchResult]]


class PartyDownload(TypedDict):
    receipt: Optional[Receipt]
    pageInfo: Optional[PageInfo]
    content: Optional[List[PartySearchResult]]
