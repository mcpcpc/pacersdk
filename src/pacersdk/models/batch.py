"""
Data models for batch search requests and responses.
"""

from typing import List
from typing import TypedDict

from .common import BaseCaseSearch
from .common import BasePartySearch
from .common import PageInfo
from .common import ReceiptInfo


class BatchCaseRequest(BaseCaseSearch, total=False):
    """
    Request model for batch case searches.
    Inherits shared filters from BaseCaseSearch.
    """

    pass


class BatchCaseResponse(TypedDict):
    """
    Response model for a submitted batch case search.
    """

    receipt: ReceiptInfo


class BatchPartyRequest(BasePartySearch, total=False):
    """
    Request model for batch party searches.
    Inherits filters from BasePartySearch.
    """

    pass


class BatchPartyResponse(TypedDict):
    """
    Response model for a submitted batch party search.
    """

    receipt: ReceiptInfo
