import uuid
from dataclasses import dataclass, field
from datetime import date
from enum import Enum


class TransactionType(Enum):
    expense = "expense"
    income = "income"

@dataclass
class Transaction:
    """Class for keeping track of transactions."""
    amount: int
    date: date
    description: str
    type: TransactionType
    account_id: uuid.UUID
    category_id: uuid.UUID | None = None
    transaction_id: uuid.UUID = field(default_factory=uuid.uuid4)