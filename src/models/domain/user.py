import datetime
from math import log1p

from src.models.domain.consts import *
import math
class User:

    def __init__(self,user_id,ip):
        self.requests_time = None
        self.user_id = user_id
        self.ip = ip
        self.requested_routes = {}
        self.requests_count = 0
        self.requests_times = 0
        self.requested_routes_count = {}
        self.last_request = None
        self.score = {}
    def add_requested_route(self,requested_route):
        if requested_route.value not in self.requested_routes:
            self.requested_routes[requested_route.value] = 1
            self.requested_routes_count[requested_route.value] = 1
            self.requests_count += 1
        else:
            self.requested_routes_count[requested_route.value] += 1
            self.requests_count += 1
    def add_requests_timestamp(self,timestamp):
        if self.last_request is None:
            self.last_request = timestamp.value
            self.requests_time = 0
            return

        delta = timestamp.value.timestamp() - self.last_request.timestamp()
        if delta < 0:
            delta = 0
        self.requests_time = delta
        self.last_request = timestamp.value
        pass
    def generate_score(self):
        self.score = {}
        self.score["routes"] = 0
        number_routes = 0
        for routes in self.requested_routes:
            if routes not in sensive_routes:
                continue
            number_routes += 1
            weight = sensive_routes[routes]
            self.score["routes"] += 100 * (1 - math.e ** (weight * -0.13 * log1p(self.requested_routes_count[routes])))
        if number_routes != 0 : self.score["routes"] = self.score["routes"] / number_routes
        return self.score
    def __str__(self):
        return f"* User id: {self.user_id}\n*Requested routes:{self.requested_routes}\n*Requested routes count:{self.requested_routes_count}\n*Requested routes time:{self.requests_time}\n*Last request:{self.last_request}"