"""
TypedDict models for court search results.

Provides `CourtList` and `Courts` structures containing metadata for
paginated court search responses, including court identifiers and names.
"""

from typing import List, Optional, TypedDict

from .billing import PageInfo, Receipt
from .query import CourtSearchResult


class CourtList(TypedDict):
    receipt: Receipt
    pageInfo: Optional[PageInfo]
    content: List[CourtSearchResult]


class Courts(TypedDict):
    receipt: Receipt
    pageInfo: Optional[PageInfo]
    content: Optional[List[CourtSearchResult]]
