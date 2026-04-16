from src.models.api_models.endpoint import EndPoint
from src.models.api_models.ip import IpAddrs
from src.models.api_models.statuscode import StatusCode
from src.models.api_models.timestamp import Timestamp
from src.models.api_models.userid import Userid
from pydantic import BaseModel

from src.models.domain.log import Log


class LogBase(BaseModel):
    timestamp: Timestamp
    ip: IpAddrs
    endpoint: EndPoint
    status: StatusCode
    user_id: Userid

    """
    Base Log class:
    {
      "timestamp": "2026-04-09T10:00:00",
      "ip": "192.168.0.1",
      "endpoint": "/login",
      "status": 401,
      "user_id": "123"
    }

    """

    @staticmethod
    def to_domain(self):
        log = Log()
        log.timestamp = self.timestamp
        log.ip = self.ip
        log.endpoint = self.endpoint
        log.status = self.status
        log.user_id = self.user_id
        return log