from enum import Enum

"""
Contains constants for accessing MUD vocabulary terms
TODO: this should belong in it's own library and be published to PyPi for reuse
"""

MUD_BASE_URL = "https://raw.githubusercontent.com/Multi-User-Domain/vocab/main/mud.ttl"
MUD_ACCT_BASE_URL = "https://raw.githubusercontent.com/Multi-User-Domain/vocab/main/mudacct.ttl"

# NOTE: when upgrading to Python 3.11, this class can be replaced with the built-in class StrEnum
class StrEnum(str, Enum):
    def __str__(self) -> str:
        return self.value

class MUD(StrEnum):
    pass

class MUD_ACCT(StrEnum):
    Account = MUD_ACCT_BASE_URL + "#Account",
    charactersList = MUD_ACCT_BASE_URL + "#CharacterList",
