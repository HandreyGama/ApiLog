class Log:
    def __init__(self,timestamp=None,ip=None,endpoint=None,status=None,user_id=None):
        self.timestamp = timestamp
        self.ip = ip
        self.endpoint = endpoint
        self.status = status
        self.user_id = user_id
        pass
    def __str__(self):
        return str(self.__dict__)