from flask import Blueprint, request, jsonify, abort
from models import Item
from extensions import db

items_bp = Blueprint("items", __name__)

@items_bp.route("", methods=["GET"])
def list_items():
    return jsonify([i.to_dict() for i in Item.query.all()])

@items_bp.route("", methods=["POST"])
def create_item():
    data = request.get_json() or {}
    if not data.get("name"):
        abort(400, "Missing `name`")
    item = Item(name=data["name"])
    db.session.add(item); db.session.commit()
    return jsonify(item.to_dict()), 201

# …and so on for GET/<id>, PUT, DELETE …
