ORDERS = [{"id": i, "status": "paid" if i % 2 else "open", "total": 100 * i} for i in range(1, 6)]


def list_orders(orders, status=None):
    """Return orders, optionally filtered by status."""
    return [o for o in orders if status is None or o["status"] == status]
