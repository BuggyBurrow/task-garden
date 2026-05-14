from enum import Enum
from dataclasses import dataclass, field
from datetime import datetime
import random
import uuid

from task_garden_app.config import WILT_THRESHOLD_SECONDS

class TaskStatus(Enum):
    INCOMPLETE = "incomplete"
    COMPLETE = "complete"
    WILTING = "wilting"     # task has not been updated recently
    EXPIRED = "expired"     # task has not been completed by the specified deadline
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

    def update_status(self):
        if self.status == TaskStatus.COMPLETE or self.status == TaskStatus.DELETED:
            return
        
        now = datetime.now()

        if self.deadline and self.deadline < now:
            self.status = TaskStatus.EXPIRED
        elif (now - self.updated_at).total_seconds() > WILT_THRESHOLD_SECONDS:
            self.status = TaskStatus.WILTING

    def mark_complete(self):
        if self.status == TaskStatus.DELETED:
            return
        self.status = TaskStatus.COMPLETE

        now = datetime.now()
        self.completed_at = now
        self.updated_at = now
