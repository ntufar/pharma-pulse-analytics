from typing import List, Optional
from ..models.customer import Customer

class CustomerService:
    def __init__(self):
        self.customers: List[Customer] = []

    def create_customer(self, customer: Customer) -> Customer:
        self.customers.append(customer)
        return customer

    def get_customer(self, customer_id: str) -> Optional[Customer]:
        for customer in self.customers:
            if customer.id == customer_id:
                return customer
        return None

    def get_all_customers(self) -> List[Customer]:
        return self.customers

    def update_customer(self, customer_id: str, updated_customer: Customer) -> Optional[Customer]:
        for i, customer in enumerate(self.customers):
            if customer.id == customer_id:
                self.customers[i] = updated_customer
                return updated_customer
        return None

    def delete_customer(self, customer_id: str) -> bool:
        initial_len = len(self.customers)
        self.customers = [c for c in self.customers if c.id != customer_id]
        return len(self.customers) < initial_len
