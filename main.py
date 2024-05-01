from dotenv import load_dotenv
import os
from clients.splitwise import SplitwiseClient
from clients.monarch import MonarchClient
import asyncio

load_dotenv()


SPLITWISE_KEY = os.environ['SPLITWISE_KEY']
SPLITWISE_SECRET = os.environ['SPLITWISE_SECRET']
SPLITWISE_API_KEY = os.environ['SPLITWISE_API_KEY']

MONARCH_EMAIL = os.environ['MONARCH_EMAIL']
MONARCH_PASSWORD = os.environ['MONARCH_PASSWORD']


async def main():  
    s = SplitwiseClient(SPLITWISE_KEY, SPLITWISE_SECRET, SPLITWISE_API_KEY)
    splitwise_expenses = s.get_expenses() 

    m = MonarchClient(MONARCH_EMAIL, MONARCH_PASSWORD)
    await m.login()
    await m.find_matches(splitwise_expenses)



asyncio.run(main())