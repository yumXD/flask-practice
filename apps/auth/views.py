from flask import Blueprint, render_template, request, jsonify

from apps.auth.models import User

bp = Blueprint("auth", __name__, template_folder="templates", static_folder="static")


@bp.route("/")
def index():
    return render_template("auth/index.html")


@bp.route('/register', methods=['POST'])
def register_user():
    username = request.json['username']
    email = request.json['email']
    password = request.json['password']

    existing_user = User.find_by_username(username)
    if existing_user:
        return jsonify({'message': 'Username already exists'}), 400

    new_user = User(username=username, email=email, password=password)
    new_user.save()

    return jsonify({'message': 'User registered successfully'}), 201


@bp.route('/login', methods=['POST'])
def login_user():
    username = request.json['username']
    password = request.json['password']

    user = User.find_by_username(username)
    if user and user.check_password(password):
        return jsonify({'message': 'Login successful'}), 200
    else:
        return jsonify({'message': 'Invalid username or password'}), 401
