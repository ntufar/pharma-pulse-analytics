from typing import List, Optional
from ..models.sales_transaction import SalesTransaction

class SalesTransactionService:
    def __init__(self):
        self.sales_transactions: List[SalesTransaction] = []

    def create_sales_transaction(self, sales_transaction: SalesTransaction) -> SalesTransaction:
        self.sales_transactions.append(sales_transaction)
        return sales_transaction

    def get_sales_transaction(self, transaction_id: str) -> Optional[SalesTransaction]:
        for transaction in self.sales_transactions:
            if transaction.id == transaction_id:
                return transaction
        return None

    def get_all_sales_transactions(self) -> List[SalesTransaction]:
        return self.sales_transactions

    def update_sales_transaction(self, transaction_id: str, updated_transaction: SalesTransaction) -> Optional[SalesTransaction]:
        for i, transaction in enumerate(self.sales_transactions):
            if transaction.id == transaction_id:
                self.sales_transactions[i] = updated_transaction
                return updated_transaction
        return None

    def delete_sales_transaction(self, transaction_id: str) -> bool:
        initial_len = len(self.sales_transactions)
        self.sales_transactions = [t for t in self.sales_transactions if t.id != transaction_id]
        return len(self.sales_transactions) < initial_len
