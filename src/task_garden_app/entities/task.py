from enum import Enum
from dataclasses import dataclass, field
from datetime import datetime
import random
import uuid

class TaskStatus(Enum):
    INCOMPLETE = "incomplete"
    COMPLETE = "complete"
    WILTING = "wilting"     # task has not been updated in 72 hours (default time)
    EXPIRED = "expired"     # past the specified deadline
    DELETED = "deleted"

@dataclass
class Task:
    # Required
    title: str

    # Defaults
    task_id: uuid.UUID = field(default_factory=uuid.uuid4)
    status: TaskStatus = TaskStatus.INCOMPLETE
    variant: int = field(default_factory=lambda: random.randint(1,4))
    memo: str = ""
    tags: list[str] = field(default_factory=list)
    
    # Time Management
    created_at: datetime = field(default_factory=datetime.now)
    updated_at: datetime = field(default_factory=datetime.now)
    completed_at: datetime | None = None
    deadline: datetime | None = None
