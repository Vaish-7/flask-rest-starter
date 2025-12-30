from flask import Blueprint, request, jsonify
from flask_jwt_extended import jwt_required
from ..models import Item
from ..db import db
from ..schemas import ItemSchema

items_bp = Blueprint("items", __name__)
item_schema = ItemSchema()
items_schema = ItemSchema(many=True)

@items_bp.route("/", methods=["POST"])
@jwt_required(optional=True)
def create_item():
    payload = request.get_json() or {}
    errors = item_schema.validate(payload)
    if errors:
        return jsonify(errors), 400
    item = Item(name=payload["name"], description=payload.get("description"))
    db.session.add(item)
    db.session.commit()
    return jsonify(item_schema.dump(item)), 201

@items_bp.route("/", methods=["GET"])
def list_items():
    items = Item.query.all()
    return jsonify(item_schema.dump(items)), 200

@items_bp.route("/<int:item_id>", methods=["GET"])
def get_item(item_id):
    item = Item.query.get_or_404(item_id)
    return jsonify(item_schema.dump(item)), 200
