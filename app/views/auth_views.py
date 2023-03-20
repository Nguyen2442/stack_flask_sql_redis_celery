from flask.json import jsonify
from flask import Blueprint , request
from flask.views import MethodView
from app.constants import HTTP_200_OK,HTTP_201_CREATED, HTTP_400_BAD_REQUEST, HTTP_404_NOT_FOUND , HTTP_401_UNAUTHORIZED
from app.models.user_model import User, db
from app.schemas.user_schema import AuthInput
from flask_pydantic import validate



user_views = Blueprint('auth_api', __name__)


class AuthRegisterView(MethodView):
        
    @validate()
    def post(self, body: UserInput):

        username = body.username
        email = body.email
        password = body.password

        
        # query user exist
        if User.query.filter(email=email).exists():
            return jsonify({
                'message': "Email is already registered",
            }), HTTP_400_BAD_REQUEST

        User(
            username=username,
            email=email,
            password=password
        )
        db.session.commit()

        return jsonify({
            'message': "",
            'user': "User is registered"
        }), HTTP_201_CREATED


class AuthRegisterView(MethodView):
        
    @validate()
    def post(self, body: UserInput):

        username = body.username
        email = body.email
        password = body.password

        
        # query user exist
        if User.query.filter(email=email).exists():
            return jsonify({
                'message': "Email is already registered",
            }), HTTP_400_BAD_REQUEST

        User(
            username=username,
            email=email,
            password=password
        )
        db.session.commit()

        return jsonify({
            'message': "",
            'user': "User is registered"
        }), HTTP_201_CREATED


class AuthRegisterView(MethodView):
    @validate()
    def post(self, body: AuthLoginInput):

        username = body.username
        email = body.email
        password = body.password
        # query user exist
        if User.query.filter(email=email).exists():
            return jsonify({
                'message': "Email is already registered",
            }), HTTP_400_BAD_REQUEST

        User(
            username=username,
            email=email,
            password=password
        )
        db.session.commit()

        return jsonify({
            'message': "",
            'user': "User is registered"
        }), HTTP_201_CREATED
    
class AuthLoginView(MethodView):
    @validate()
    def post(self, body: AuthLoginInput):
        email = body.email
        password = body.password

        existing_user = User.query.filter(email=email).exist()
        if not existing_user:
            return jsonify({
                'message': 'User not found'
            }), HTTP_400_BAD_REQUEST
            
        is_password_correct = check_password_hash(existing_user.password, password)
        if not is_password_correct:
            return jsonify({
                'message': 'Password is wrong'
            }), HTTP_400_BAD_REQUEST
        expires = datetime.timedelta(days=1)
        access = create_access_token(
            identity={
                'id': existing_user.id,
                'username': existing_user.username, 
                'email': existing_user.email,
            },
            expires_delta=expires
        )
        access = create_refresh_token(
            identity={
                'id': existing_user.id,
                'username': existing_user.username, 
                'email': existing_user.email,
            }
        )

        return jsonify({
            'message': 'Logged in successfully',
            'access_token' : access,
            'refresh_token' : refresh,
        }), HTTP_201_CREATED
    

user_views.add_url_rule('/api/v1/login', view_func=AuthLoginView.as_view('auth_login_view'), methods=['POST'])
user_views.add_url_rule('/api/v1/register', view_func=AuthRegisterView.as_view('auth_register_view'), methods=['POST'])