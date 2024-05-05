# 

## Notes to self
For whatever reason, after a transaction split Monarch creates separate objects with separate IDs, and the original transaction ID will no longer appear in the response from `client.get_transactions()`. However, with the split transaction ID, you can call `client.get_transaction_details(split_id)`, find the original transaction ID, then call `client.get_transaction_splits(original_id)` to get the relevant information. 