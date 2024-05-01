from monarchmoney import MonarchMoney
import json

class MonarchClient:
    def __init__(self, email, password):
        self.client = MonarchMoney()
        self.email = email
        self.password = password

    async def login(self):
        await self.client.login(self.email, self.password)

    async def _get_reimbursement_category_id(self):
        categories = (await m.client.get_transaction_categories())['categories']
        reimbursements_category_id = next((c for c in categories if c['name'] == 'Reimbursements'))['id']
           
    async def find_matches(self, splitwise_expenses):
        txns = []
        offset = 0
        batch_size = 500
        total_transactions = float('inf')

        while True:
            if offset > total_transactions:
                break

            print(f'fetching {batch_size} transactions starting from offset {offset}')
            response = await self.client.get_transactions(limit=batch_size, offset=offset)
            txns += response['allTransactions']['results']

            offset += batch_size
            total_transactions = response['allTransactions']['totalCount']

        print(splitwise_expenses.keys())
        for txn in txns:
            amount = -1 * txn['amount']
            if amount in splitwise_expenses.keys():
                splitwise_expense = splitwise_expenses[amount]
                print('Found', splitwise_expense)
                # del splitwise_expenses[amount]

        print('Not found', json.dumps(splitwise_expenses, indent=4))
