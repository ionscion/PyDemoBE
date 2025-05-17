from flask import Blueprint, request, jsonify, abort
from models import User
from extensions import db

users_bp = Blueprint("users", __name__)

@users_bp.route("", methods=["GET"])
def list_users():
    return jsonify([u.to_dict() for u in User.query.all()])

@users_bp.route("", methods=["POST"])
def create_user():
    data = request.get_json() or {}
    u = User(
      first_name  = data.get("first_name"),
      middle_name = data.get("middle_name"),
      last_name    = data.get("last_name")
    )
    db.session.add(u); db.session.commit()
    return jsonify(u.to_dict()), 201
