import re
from typing import ClassVar

from pydantic import BaseModel, field_validator


class Userid(BaseModel):
    value: str
    REGEX_PATTERN: ClassVar[str] = r"^[a-zA-Z0-9\-]+$"

    @field_validator("value")
    def check_valid_value(value):
        if type(value) is not str: return False
        result = re.match(Userid.REGEX_PATTERN, value)
        if result is None:
            return False
        return value
    def __str__(self):
        return str(self.value)