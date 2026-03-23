from enum import Enum

class StatusEnum(str, Enum):
    present = "Present"
    absent = "Absent"