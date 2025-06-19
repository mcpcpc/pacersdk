from typing import List
from typing import Optional
from typing import TypedDict

from .billing import PageInfo
from .billing import Receipt
from .query import CourtSearchResult


class CourtList(TypedDict):
    receipt: Receipt
    pageInfo: Optional[PageInfo]
    content: List[CourtSearchResult]


class Courts(TypedDict):
    receipt: Receipt
    pageInfo: Optional[PageInfo]
    content: Optional[List[CourtSearchResult]]
