import re
from typing import ClassVar

from pydantic import BaseModel, field_validator


class IpAddrs(BaseModel):
    value: str
    REGEX_PATTERN:ClassVar[str] = r"[\d]{1,3}.[\d]{1,3}.[\d]{1,3}.[\d]{1,3}"

    @field_validator("value")
    def check_valid_value(value):
        if type(value) is not str: return False
        result = re.match(IpAddrs.REGEX_PATTERN, value)
        if not result:
            return False
        return value
    def __str__(self):
        return str(self.value)
