import json

from flask import render_template, request
from datetime import datetime
from . import create_app, database
from .models import Items


app = create_app()


@app.route("/main")
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


@app.route('/items', methods=['POST'])
def add():
    data = request.get_json()
    name = data['name']
    desc = data['description']
    qt = data['quantity']

    database.add_instance(Items, name=name, description=desc, quantity=qt)
    return json.dumps("Added"), 200
