from orders import ORDERS, list_orders


def summary():
    rows = list_orders(ORDERS)
    return f"{len(rows)} orders, total {sum(r['total'] for r in rows)}"


if __name__ == "__main__":
    print(summary())
