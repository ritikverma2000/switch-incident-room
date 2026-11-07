def cart_total(items, coupon=None):
    subtotal = sum(i["price"] * i["qty"] for i in items)
    if coupon:
        discount = subtotal * coupon["percent"] / 100
        return round(subtotal - discount, 2)
    return round(subtotal, 2)
