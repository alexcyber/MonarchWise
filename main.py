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


async def main():  
    s = SplitwiseClient(SPLITWISE_KEY, SPLITWISE_SECRET, SPLITWISE_API_KEY)
    print(json.dumps(s.get_expenses(), indent=4))
    # m = MonarchClient(MONARCH_EMAIL, MONARCH_PASSWORD)
    # await m.login()

    # categories = (await m.client.get_transaction_categories())['categories']
    # reimbursements_category_id = next((c for c in categories if c['name'] == 'Reimbursements'))['id']
    # print(reimbursements_category_id)
    # txns = (await m.client.get_transactions())
    # print(json.dumps(txns, indent=4))

asyncio.run(main())