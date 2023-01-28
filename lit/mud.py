from enum import Enum

"""
Contains constants for accessing MUD vocabulary terms
TODO: this should belong in it's own library and be published to PyPi for reuse
"""

MUD_BASE_URL = "https://raw.githubusercontent.com/Multi-User-Domain/vocab/main/mud.ttl"
MUD_ACCT_BASE_URL = "https://raw.githubusercontent.com/Multi-User-Domain/vocab/main/mudacct.ttl"

class MUD:
    pass


class MUD_ACCT:
    Account = MUD_ACCT_BASE_URL + "#Account"
    charactersList = MUD_ACCT_BASE_URL + "#CharacterList"
