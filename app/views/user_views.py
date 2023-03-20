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
            'user': list_users,
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

    @validate()
    def put(self, body: UserInput):
        user_info = dict(
            username=body.username,
        )
        existing_user = User.query.filter(id=id).first()
        if not existing_user:
            return jsonify({
                'message': "User not found",
                'user': "meomeo"
            }), HTTP_404_NOT_FOUND
        partial_update_object(existing_user, user_info)
        db.session.commit()

        return jsonify({
            'message': "User is updated",
            'success': True
        }), HTTP_200_OK
    

user_views.add_url_rule('/api/v1/user', view_func=UserView.as_view('user_view'), methods=['GET', 'POST', 'PUT'])