import uuid
from dataclasses import dataclass, field
from enum import Enum


class AccountType(Enum):
    checkings = "checkings"
    savings = "savings"

@dataclass
class Account:
    """Class for Accounts"""
    name: str
    balance: int
    account_type: AccountType
    account_id: uuid.UUID = field(default_factory=uuid.uuid4)