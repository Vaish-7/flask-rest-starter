from flask_jwt_extended import JWTManager, create_access_token, jwt_required, get_jwt_identity
from flask import Blueprint, request, jsonify

jwt = JWTManager()
auth_bp = Blueprint("auth", __name__, url_prefix="/api/v1/auth")

@auth_bp.route("/token", methods=["POST"])
def login():
    data = request.get_json() or {}
    username = data.get("username")
    password = data.get("password")
    # Demo auth: replace with real user lookup
    if username == "demo" and password == "demo":
        token = create_access_token(identity=username)
        return jsonify(access_token=token), 200
    return jsonify(msg="Bad credentials"), 401
