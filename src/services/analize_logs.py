from src.models.domain.log import Log
from src.models.domain.user import User


def analyze_logs(logs:list[Log]):
    users_dict = {}
    for log in logs:
        if log.user_id.value not in users_dict:
            u = User(user_id=log.user_id.value, ip=log.ip.value)
            u.add_requested_route(log.endpoint)
            u.add_requests_timestamp(log.timestamp)
            users_dict[log.user_id.value] = u
        else:
            u = users_dict[log.user_id.value]
            u.add_requests_timestamp(log.timestamp)
            u.add_requested_route(log.endpoint)
        pass
    return users_dict