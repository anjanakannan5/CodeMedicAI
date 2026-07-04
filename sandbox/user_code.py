def update_inventory(current_stock, arrivals):
    for item, quantity in arrivals.items():
        if item in current_stock:
            current_stock[item] += quantity
        else:
            current_stock[item] = quantity
    return current_stock

def verify_and_clear_shipment(shipment_box):
    for item in shipment_box:
        if shipment_box[item] <= 0:
            del shipment_box[item]
    return shipment_box

my_stock = {"apples": 10, "oranges": 5}
new_shipment = {"apples": 5, "bananas": 12, "grapes": 0}

updated_stock = update_inventory(my_stock, new_shipment)
clean_shipment = verify_and_clear_shipment(new_shipment)

print("Inventory update complete.")