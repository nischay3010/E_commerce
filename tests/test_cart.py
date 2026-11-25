from cart.cart_validation import check_stock_available

def test_stock_is_sufficient():
    assert check_stock_available(10, 5) is True

def test_stock_is_insufficient():
    assert check_stock_available(10, 15) is False

def test_zero_quantity_is_invalid():
    assert check_stock_available(10, 0) is False

def test_negative_quantity_is_invalid():
    assert check_stock_available(10, -2) is False
    
