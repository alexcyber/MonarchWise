from monarchmoney import MonarchMoney
import json
import copy


class MonarchClient(object):
    @classmethod
    async def create(cls, email, password):
        self = cls()
        self.client = MonarchMoney()
        self.email = email
        self.password = password

        await self.client.login(self.email, self.password)
        self.categories = (await self.client.get_transaction_categories())['categories']
        self.reimbursements_category_id = next(
            (c for c in self.categories if c['name'] == 'Reimbursements'))['id']
        return self

    async def find_matches(self, splitwise_expenses):
        txns = []
        offset = 0
        batch_size = 200
        total_transactions = float('inf')

        while True:
            if offset > total_transactions:
                break

            print(
                f'fetching {batch_size} transactions starting from offset {offset}')
            response = await self.client.get_transactions(limit=batch_size, offset=offset)
            txns += response['allTransactions']['results']

            offset += batch_size
            total_transactions = response['allTransactions']['totalCount']

        with open('mm.json', 'w') as f:
            f.write(json.dumps(txns, indent=4))

        print(splitwise_expenses.keys())
        txns_to_split = []
        for txn in txns:
            if txn['isSplitTransaction']:
                continue

            amount = -1 * txn['amount']
            if amount in splitwise_expenses.keys():
                splitwise_expense = splitwise_expenses[amount]
                print('Found', splitwise_expense)
                print(json.dumps(txn, indent=2))
                # del splitwise_expenses[amount]

                monarch_id = txn['id']
                monarch_merchant = txn['merchant']['name']
                original_category = txn['category']['id']
                reimbursement = splitwise_expense['amount_reimbursed']

                split_data = [
                    {
                        'merchantName': monarch_merchant,
                        'amount': -1 * (amount - reimbursement),
                        'categoryId': original_category
                    },
                    {
                        'merchantName': monarch_merchant,
                        'amount': -1 * (reimbursement),
                        'categoryId': self.reimbursements_category_id
                    }
                ]

                print(f'Splitting transaction for {monarch_merchant} into ${reimbursement} reimbursed and {amount - reimbursement} for {txn["category"]["name"]}')
                print('Confirm? Y/N')
                if(input().lower() == 'y'):
                    print(await self.client.update_transaction_splits(monarch_id, split_data))
