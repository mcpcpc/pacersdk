from typing import TypedDict

from .types import DateTime
from .types import Money


class PageInfo(TypedDict):
    """
    Metadata about a paginated API response.
    """
    number: int
    size: int
    totalPages: int
    totalElements: int
    numberOfElements: int
    first: bool
    last: bool


class Receipt(TypedDict):
    """
    Details of a billable transaction or search receipt.
    """
    transactionId: int
    transactionDate: DateTime
    billablePages: int
    fee: Money
    loginId: str
    clientCode: str
    firmId: str
    search: str
    description: str
    csoId: int
    juId: str
    reportId: str
