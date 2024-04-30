from dotenv import load_dotenv
import os
from clients.splitwise import SplitwiseClient
from clients.monarch import MonarchClient
import asyncio
import json
load_dotenv()


SPLITWISE_KEY = os.environ['SPLITWISE_KEY']
SPLITWISE_SECRET = os.environ['SPLITWISE_SECRET']
SPLITWISE_API_KEY = os.environ['SPLITWISE_API_KEY']

MONARCH_EMAIL = os.environ['MONARCH_EMAIL']
MONARCH_PASSWORD = os.environ['MONARCH_PASSWORD']

s = SplitwiseClient(SPLITWISE_KEY, SPLITWISE_SECRET, SPLITWISE_API_KEY)


# async def main():
#     m = MonarchClient(MONARCH_EMAIL, MONARCH_PASSWORD)
#     await m.login()

#     txns = (await m.client.get_transactions())
#     # print(json.dumps(txns, indent=4))

# asyncio.run(main())