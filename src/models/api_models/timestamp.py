from datetime import datetime
from pydantic import BaseModel
class Timestamp(BaseModel):
    value: datetime
    def __str__(self):
        return str(self.value)