from flask_login import login_user, logout_user, login_required, current_user
from .models import User, Conversation
from flask_jwt_extended import create_access_token

main = Blueprint('main', __name__)

@main.route('/api/register', methods=['POST'])
def register():
    data = request.get_json()
    email = data.get('email')
    password = data.get('password')
    name = data.get('name')
    if User.query.filter_by(email=email).first():
        return jsonify(message='User already exists'), 409
    new_user = User(email=email, name=name)
    new_user.set_password(password)
    db.session.add(new_user)
    db.session.commit()
    return jsonify(message='User registered'), 201

@main.route('/api/login', methods=['POST'])
def login():
    data = request.get_json()
    email = data.get('email')
    password = data.get('password')
    user = User.query.filter_by(email=email).first()
    if user and user.check_password(password):
        login_user(user)
        access_token = create_access_token(identity=user.id)
        return jsonify(access_token=access_token), 200
    return jsonify(message='Invalid credentials'), 401

@main.route('/api/logout', methods=['POST'])
@login_required
def logout():
    logout_user()
    return jsonify(message='Logged out'), 200

@main.route('/api/profile', methods=['GET'])
@login_required
def profile():
    return jsonify(name=current_user.name, email=current_user.email), 200

@main.route('/api/conversations', methods=['POST'])
@login_required
def conversations():
    # Your code here
    pass