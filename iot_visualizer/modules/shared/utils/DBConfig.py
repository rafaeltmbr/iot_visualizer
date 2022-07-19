class DBConfig:
    def __init__(self, protocol, user, password, host, port, database):
        self.protocol = protocol
        self.user = user
        self.password = password
        self.host = host
        self.port = port
        self.database = database

    def url(self):
        return f'{self.protocol}://{self.user}:{self.password}@{self.host}:{self.port}/{self.database}'