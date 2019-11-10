import json

from flask import render_template, request, abort
from datetime import datetime
from . import create_app
from .database.models import Items
from .database import database


app = create_app()


@app.route("/welcome")
def welcome():
    return render_template("welcome.html", message="my api!")


@app.route("/date")
def date():
    return "Today is: " + str(datetime.now())


counter = 0


@app.route("/count")
def count():
    global counter
    counter += 1
    return "Counter is: " + str(counter)


@app.route("/items/render/<int:id>")
def render_items(id):
    try:
        item = database.get_by_id(Items, id)
        new_item = {
            "id": item.id,
            "name": item.name,
            "description": item.description,
            "quantity": item.quantity
        }
        return render_template("items.html", item=new_item)
    except Exception:
        abort(404)


@app.route('/items', methods=['GET'])
def fetch():
    items = database.get_all(Items)
    items_array = []
    for item in items:
        new_item = {
            "id": item.id,
            "name": item.name,
            "description": item.description,
            "quantity": item.quantity
        }

        items_array.append(new_item)
    return json.dumps(items_array), 200


@app.route('/items/<int:id>', methods=['GET'])
def fetch_by_id(id):
    try:
        item = database.get_by_id(Items, id)
        new_item = {
            "id": item.id,
            "name": item.name,
            "description": item.description,
            "quantity": item.quantity
        }
        return json.dumps(new_item), 200
    except Exception:
        abort(404)


@app.route('/items', methods=['POST'])
def add():
    data = request.get_json()
    name = data['name']
    desc = data['description']
    qt = data['quantity']

    database.add_instance(Items, name=name, description=desc, quantity=qt)
    return json.dumps("Added"), 200
