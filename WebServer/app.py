"""
Flask Web Server to to mediate information sharing between the ShoppingBot's
ARuCo Tag scanning module  and the ShoppingBot iOS app. 
"""

import json
from flask import Flask
from flask import request

app = Flask(__name__)


def setup():
    """
    Initializes all variables and reads item prices from item_prices.json
    :returns: a tuple (float, float, dict) of the original budget, remaining
    budget and item prices.
    """
    item_prices = {}
    og_budget = 30.0
    remaining_budget = og_budget
    with open("item_prices.json", "r") as f:
        item_prices = json.load(f)

    return (og_budget, remaining_budget, item_prices)


og_budget, remaining_budget, item_prices = setup()
last_item_price = 0.0


@app.route("/")
def root():
    """
    Dummy route for testing connection to the web server.
    """
    return "Hello, world!"


@app.route("/lookup", methods=["GET"])
def lookup():
    """
    Looks up and price of an item specified by item_id in the request args
    :returns: A json encoding of the item id and item price.
    """
    item_id = request.args.get("item_id", "")

    item_price = float(item_prices[item_id])

    ret = {
        "item_id" : item_id,
        "item_price" : item_price
    }

    return json.dumps(ret)


@app.route("/update", methods=["POST"])
def update():
    """
    Updates the remaining budget. Subtracts either the item_price given in the 
    request args or the price of an item specified by the item_id, if the item
    is known.

    :returns: A json encoding of the remaining budget after the update.
    """
    global remaining_budget
    global last_item_price
    update_budget = float(request.args.get("item_price", "-1"))

    if (update_budget == -1):
        item_id = request.args.get("item_id", "")
        if (item_id != ""):
            update_budget = item_prices[item_id]

    last_item_price = update_budget
    remaining_budget -= update_budget

    ret = { 
        "remaining_budget" : remaining_budget
    }

    return json.dumps(ret)


@app.route("/budget", methods=["POST", "GET"])
def budget():
    """
    Route for either getting or setting budget information
    """
    if request.method == "GET":
        return _get_budget()
    else:
        return _set_budget(request)


@app.route("/remove_item", methods=["POST"])
def removeItem():
    """
    Route to remove the last item from the scanning history and
    update remaining_budget accordingly.
    """
    global remaining_budget
    global last_item_price

    remaining_budget += last_item_price


def _set_budget(request_obj):
    """
    Sets og_budget to the request parameter new_budget in request_obj.
    Can also be used to reset the budget if new_budget parameter is not present.

    :returns: a json encoding of old_budget and new_budget.
    """

    global og_budget
    global remaining_budget

    ret = {
        "old_budget" : og_budget
    }

    new_budget = og_budget

    new_budget = float(request_obj.args.get("new_budget", str(og_budget)))
    og_budget = new_budget
    remaining_budget = new_budget

    ret["new_budget"] = new_budget

    return json.dumps(ret)


def _get_budget():
    """
    Gets infomation about the original and remaining budgets.

    :returns: A json encoded value of remaining_budget and og_budget
    """

    ret = {
        "og_budget" : og_budget,
        "remaining_budget" : remaining_budget
    }

    return json.dumps(ret)


if __name__ == "__main__":
    app.run(host='0.0.0.0', port=8080, debug=True)
