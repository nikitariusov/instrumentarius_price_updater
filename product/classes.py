class Product_item:
    """Данные товара что обновляются"""
    def __init__(self, vendor_code, price, available):
        self.vendor_code = vendor_code
        self.price = price
        self.available = available
