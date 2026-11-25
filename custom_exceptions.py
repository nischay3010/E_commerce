class EcommerceError(Exception):
    pass

class ProductNotFoundError(Exception):
    pass

class CategoryNotFoundError(Exception):
    pass
class CartEmptyError(Exception):
    pass
class UserNotSignInError(Exception):
    pass
class UnAuthorizedAccessError(Exception):
    pass
class InvalidPriceError(Exception):
    pass
class InsufficientStockError(Exception):
    pass