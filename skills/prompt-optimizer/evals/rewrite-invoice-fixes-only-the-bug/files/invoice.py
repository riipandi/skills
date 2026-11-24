TAX = 0.11


def total(items, discount=0):
    subtotal = sum(item["price"] for item in items)
    return round((subtotal - discount) * (1 + TAX), 2)
