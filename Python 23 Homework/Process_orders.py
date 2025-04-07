def process_orders(orders, inventory):
    successful_orders = []
    for order in orders:
        product = order["product"]
        quantity = order["quantity"]

        if product not in inventory:
            raise ValueError(f"Product '{product}' not found in inventory")
        if quantity > inventory[product]:
            raise ValueError(f"Not enough stock for '{product}'")

        inventory[product] -= quantity
        successful_orders.append(order)

    return successful_orders
