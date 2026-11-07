from cart import cart_total
items = [{"price": 50.0, "qty": 2}]
def test_no_coupon():
    assert cart_total(items) == 100.0
def test_new_coupon_format():
    assert cart_total(items, {"code": "FALL10", "pct": 10}) == 90.0
