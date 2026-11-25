def check_stock_available(stock, requested_quantity):
    if requested_quantity <= 0:
        return False
    return requested_quantity <= stock

