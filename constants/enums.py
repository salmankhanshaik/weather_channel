import enum


class BaseStrEnum(str, enum.Enum):
    @classmethod
    def values_list(cls):
        return [item.value for item in cls]

    def __repr__(self):
        return self._value_

    def __str__(self):
        return self._value_




# -------------------------- Global Enums -------------------------------
class StatusType(BaseStrEnum):
    SUCCESS            = "success"
    ERROR              = "error"
