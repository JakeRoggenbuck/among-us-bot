import motor.motor_asyncio as motor


class DatabaseCommunicator:
    def __init__(self, guild: int, location: str = "localhost", port: int = 27017):
        self.location = location
        self.port = port
        self.guild = guild
        self.connect()

    def connect(self):
        self.client = motor.AsyncIOMotorClient(self.location, self.port)
        self.database = self.client[self.guild]
        self.auth = self.database.auth
