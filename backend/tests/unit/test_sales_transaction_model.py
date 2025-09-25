import pytest
from datetime import datetime
from backend.src.models.sales_transaction import SalesTransaction

def test_sales_transaction_creation():
    transaction = SalesTransaction(
        id="st_001",
        product_id="prod_001",
        customer_id="cust_001",
        territory_id="terr_001",
        transaction_date=datetime.now(),
        quantity=2,
        price_per_unit=25.50,
        total_amount=51.00,
    )
    assert transaction.id == "st_001"
    assert transaction.product_id == "prod_001"
    assert transaction.customer_id == "cust_001"
    assert transaction.territory_id == "terr_001"
    assert transaction.quantity == 2
    assert transaction.price_per_unit == 25.50
    assert transaction.total_amount == 51.00

def test_sales_transaction_invalid_quantity():
    with pytest.raises(ValueError):
        SalesTransaction(
            id="st_002",
            product_id="prod_001",
            customer_id="cust_001",
            territory_id="terr_001",
            transaction_date=datetime.now(),
            quantity=0,
            price_per_unit=25.50,
            total_amount=0.00,
        )

def test_sales_transaction_invalid_price_per_unit():
    with pytest.raises(ValueError):
        SalesTransaction(
            id="st_003",
            product_id="prod_001",
            customer_id="cust_001",
            territory_id="terr_001",
            transaction_date=datetime.now(),
            quantity=1,
            price_per_unit=0.00,
            total_amount=0.00,
        )
