import logging
import datetime
from splitwise import Splitwise
from functools import lru_cache
# logging.basicConfig(level=logging.DEBUG)


class SplitwiseClient:
    def __init__(self, key, secret, api_key):
        self.client = Splitwise(key, secret, api_key=api_key)
        self.client.getExpenses
        self.clientUserId = self.client.getCurrentUser().getId()

    @lru_cache
    def _get_name(self, id):
        user = self.client.getUser(id)
        # print(f'{user.first_name}{f" {user.last_name}" if user.last_name else ""} is {id}')
        return f'{user.first_name}{f" {user.last_name}" if user.last_name else ""}'

    def get_expenses(self):
        expenses_data = []
        offset = 0
        while True:
            page = self.client.getExpenses(limit=100, offset=offset)
            if not page:
                break
            expenses_data.extend(page)
            offset += 100

        for expense in expenses_data:
            dt = datetime.datetime.strptime(expense.date, "%Y-%m-%dT%H:%M:%SZ")
            formatted_date = dt.strftime("%m/%d/%y")
            # print(expense.description, f'${expense.cost}', formatted_date)
            # [print(f'\t{self._get_name(d.fromUser)} => {self._get_name(d.toUser)} (${d.amount})') for d in expense.repayments]

            amount_reimbursed = sum(
                [float(d.amount) for d in expense.repayments if d.toUser == self.clientUserId])

            if amount_reimbursed > 0:
                cost = float(expense.cost)
                # assert cost not in expenses.keys()
                expenses[cost] = {
                    'total_cost': cost,
                    'description': expense.description,
                    'date': expense.date,
                    'amount_reimbursed': amount_reimbursed
                }

        return expenses
