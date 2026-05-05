import uuid
from dataclasses import dataclass, field

@dataclass
class Category:
    """Class for Categories"""
    name: str
    color: str | None = None
    category_id: uuid.UUID = field(default_factory=uuid.uuid4)