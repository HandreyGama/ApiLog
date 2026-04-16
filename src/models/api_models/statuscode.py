from http import HTTPStatus
from pydantic import BaseModel
class StatusCode(BaseModel):
    value: HTTPStatus
    def __str__(self):
        return str(self.value)