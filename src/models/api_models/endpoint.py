import re
from typing import ClassVar

from pydantic import BaseModel, field_validator


class EndPoint(BaseModel):
    value: str
    REGEX_PATTERN: ClassVar[str] = r"^\/[a-zA-Z0-9._\-\/]*$"

    @field_validator("value")
    def check_valid_value(value):
        if type(value) is not str: return False
        result = re.match(EndPoint.REGEX_PATTERN,value)
        if not result:
            return False
        return value

