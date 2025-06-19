from typing import TypedDict

from .types import DateTime
from .types import Money


class PageInfo(TypedDict):
    number: int
    size: int
    totalPages: int
    totalElements: int
    numberOfElements: int
    first: bool
    last: bool


class Receipt(TypedDict):
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
