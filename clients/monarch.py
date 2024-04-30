from monarchmoney import MonarchMoney

class MonarchClient:
    def __init__(self, email, password):
        self.client = MonarchMoney()
        self.email = email
        self.password = password

    async def login(self):
        await self.client.login(self.email, self.password)