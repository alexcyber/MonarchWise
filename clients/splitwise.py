import logging
import datetime
from splitwise import Splitwise
from functools import lru_cache
# logging.basicConfig(level=logging.DEBUG)


class SplitwiseClient:
    def __init__(self, key, secret, api_key):
        self.client = Splitwise(key, secret, api_key=api_key)
        self.expenses = self.client.getExpenses()

        for expense in self.expenses:
            dt = datetime.datetime.strptime(expense.date, "%Y-%m-%dT%H:%M:%SZ")
            formatted_date = dt.strftime("%m/%d/%y")
            print(expense.description, f'${expense.cost}', formatted_date)
            [print(f'\t{self.get_name(d.fromUser)} => {self.get_name(d.toUser)} (${d.amount})') for d in expense.repayments]

        print(self.client.getCurrentUser().getId())
        print(self.get_name(self.client.getCurrentUser().getId()))
    @lru_cache
    def get_name(self, id):
        # if id == self.client.getCurrentUser():
        #     print(f'hello {client.getUser(id)}')
        user = self.client.getUser(id)
        print(f'{user.first_name}{f" {user.last_name}" if user.last_name else ""} is {id}')
        return f'{user.first_name}{f" {user.last_name}" if user.last_name else ""}'

    
    