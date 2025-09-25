from typing import List, Optional
from ..models.product import Product

class ProductService:
    def __init__(self):
        self.products: List[Product] = []

    def create_product(self, product: Product) -> Product:
        self.products.append(product)
        return product

    def get_product(self, product_id: str) -> Optional[Product]:
        for product in self.products:
            if product.id == product_id:
                return product
        return None

    def get_all_products(self) -> List[Product]:
        return self.products

    def update_product(self, product_id: str, updated_product: Product) -> Optional[Product]:
        for i, product in enumerate(self.products):
            if product.id == product_id:
                self.products[i] = updated_product
                return updated_product
        return None

    def delete_product(self, product_id: str) -> bool:
        initial_len = len(self.products)
        self.products = [p for p in self.products if p.id != product_id]
        return len(self.products) < initial_len
