from werkzeug.security import generate_password_hash, check_password_hash

from apps.app import db


class User:
    def __init__(self, username, email, password):
        self.username = username
        self.email = email
        self.password_hash = password

    @staticmethod
    def from_dict(data):
        return User(
            username=data.get('username'),
            email=data.get('email'),
            password=data.get('password_hash')
        )

    def to_dict(self):
        return {
            'username': self.username,
            'email': self.email,
            'password_hash': generate_password_hash(self.password_hash, method="pbkdf2:sha256")
        }

    @staticmethod
    def find_by_id(user_id):
        user_data = db.users.find_one({'_id': user_id})
        if user_data:
            return User.from_dict(user_data)
        return None

    @staticmethod
    def find_by_username(username):
        user_data = db.users.find_one({'username': username})
        if user_data:
            return User.from_dict(user_data)
        return None

    def save(self):
        user_data = self.to_dict()
        result = db.users.insert_one(user_data)
        return result.inserted_id

    def check_password(self, password):
        return check_password_hash(self.password_hash, password)
