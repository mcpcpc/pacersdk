"""
Type aliases representing common PACER scalar types.

Includes newtypes like `Date`, `DateTime`, `Money`, and `Character`
used throughout the PACER SDK for strong typing and validation.
"""

from decimal import Decimal
from typing import NewType

#: Represents a single alphanumeric character (0-9, a-z, A-Z)
Character = NewType("Character", str)

#: Up to 4 alphanumeric characters
JurisdictionType = NewType("JurisdictionType", str)

#: Date in format: YYYY-MM-DD or YYYY/MM/DD
Date = NewType("Date", str)

#: ISO-like datetime format: YYYY-MM-DDTHH:MM:SS.sssZ or YYYY/MM/DDTHH:MM:SS.sssZ
DateTime = NewType("DateTime", str)

#: Decimal with two fraction digits
Money = NewType("Money", Decimal)
