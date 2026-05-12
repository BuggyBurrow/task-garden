from enum import Enum

class TaskStatus(Enum):
    INCOMPLETE = "incomplete"
    COMPLETE = "complete"
    WILTING = "wilting"     # task has not been updated in 72 hours (default time)
    EXPIRED = "expired"     # past the specified deadline
    DELETED = "deleted"

