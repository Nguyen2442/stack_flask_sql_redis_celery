from flask.json import jsonify
from flask import Blueprint , request
from flask.views import MethodView
from app.constants import HTTP_200_OK,HTTP_201_CREATED, HTTP_400_BAD_REQUEST, HTTP_404_NOT_FOUND , HTTP_401_UNAUTHORIZED
from app.models.user_model import User, db
from app.schemas.user_schema import UserInput
from flask_pydantic import validate



user_views = Blueprint('user_api', __name__)


class UserView(MethodView):
    def get(self):
            user = User.query.all()
            list_users = [user.format() for user in user]
            return jsonify({
                'message': True,
                'user':list_users,
            }), HTTP_200_OK
        
    
    @validate()
    def post(self, body: UserInput):
        # user_body = body.to_dict()
        print(100*"body")
        print(body)
        # print(body.username)
        # user_dict = dict(
        #     username=user_body.username,
        #     email=user_body.email,
        #     password=user_body.password
        # )

        return jsonify({
            'message': "User validated",
            'user': "meomeo"
        }), HTTP_201_CREATED
        # username = request.json['username']
        # password = request.json['password']

        # if len(username)<3:
        #     return jsonify({'message': 'Username must be at least 3 characters long'}), HTTP_400_BAD_REQUEST

        # if not username.isalnum() or " " in username:
        #     return jsonify({'message': 'Username must be alphanumeric and contain no spaces'}), HTTP_400_BAD_REQUEST

        # if len(password) < 8:
        #     return jsonify({'message': 'Password must be at least 8 characters long'}), HTTP_400_BAD_REQUEST

        # user = User.query.filter_by(username=username).first()
        # if user is not None:
        #     return jsonify({'message': 'Username already exists'}), HTTP_400_BAD_REQUEST
        # else:
        #     new_user = User(username=username, password=password, isAdmin=isAdmin)
        #     db.session.add(new_user)
        #     db.session.commit()

        # return jsonify({
        #     'message': "User created",
        #     'user': {
        #         'username': new_user.username,
        #     }
        # }), HTTP_201_CREATED
    

user_views.add_url_rule('/api/v1/user', view_func=UserView.as_view('user_view'), methods=['GET', 'POST'])