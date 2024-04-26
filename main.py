from dotenv import load_dotenv
import os
import logging
from splitwise import Splitwise
import datetime

load_dotenv()

# logging.basicConfig(level=logging.DEBUG)

SPLITWISE_KEY = os.environ['SPLITWISE_KEY']
SPLITWISE_SECRET = os.environ['SPLITWISE_SECRET']
SPLITWISE_API_KEY = os.environ['SPLITWISE_API_KEY']

client = Splitwise(SPLITWISE_KEY, SPLITWISE_SECRET, api_key=SPLITWISE_API_KEY)

def get_name(id):
    if id == client.getCurrentUser():
        print(f'hello {client.getUser(id)}')
    user = client.getUser(id)
    return f'{user.first_name}{f" {user.last_name}" if user.last_name else ""}'

expenses = client.getExpenses()
for expense in expenses:
    dt = datetime.datetime.strptime(expense.date, "%Y-%m-%dT%H:%M:%SZ")
    formatted_date = dt.strftime("%m/%d/%y")
    print(expense.description, f'${expense.cost}', formatted_date)
    [print(f'\t{get_name(d.fromUser)} => {get_name(d.toUser)} (${d.amount})') for d in expense.repayments]
