"""
Utility script for adding item prices and accociating them with ARuCo Tag IDs.
"""
import json

json_dict = {}
for i in range(10):
    item_id = input("Enter item ID: ")
    item_price = float(input("Enter item price: "))

    json_dict[item_id] = item_price


with open("item_prices.json", "w") as f:
    json.dump(json_dict, f)


