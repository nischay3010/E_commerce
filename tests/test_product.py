import pytest
from custom_exceptions import (InvalidPriceError)
from product.products import (calculate_total,ValidatePrice)

def test_calculate_total():
    assert calculate_total(100,3)==300
    
def test_calculate_total_quantity():
    assert calculate_total(100,0)==0

def test_calculate_total_one_quantity():
    assert calculate_total(100,1)==100

def test_validate_price():
    with pytest.raises(InvalidPriceError):
        ValidatePrice(789)
        

    