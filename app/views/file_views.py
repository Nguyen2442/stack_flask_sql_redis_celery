from flask.json import jsonify
from flask import Blueprint , request
from flask.views import MethodView
from app.constants import HTTP_200_OK,HTTP_201_CREATED, HTTP_400_BAD_REQUEST, HTTP_404_NOT_FOUND , HTTP_401_UNAUTHORIZED
from app.models.user_model import User, db
from app.schemas.user_schema import UserInput
from app.schemas.file_schema import FileInput
from flask_pydantic import validate
from app.core.app_celery.task import generate_large_file
from app.core.database.redis import redis_client
import uuid, os



file_views = Blueprint('file_api', __name__)


class FileView(MethodView):
        
    
    def post(self):
        # Generate a unique task ID
        #task_id = uuid.uuid4().hex

        # Trigger the Celery task with the task ID
        task = generate_large_file.delay()
        task_id = task.id
        # Trigger the Celery task
        # Store the task ID in Redis
        redis_client.set(task_id, 'PENDING')

        # Return a response indicating that the task is in progress
        response = jsonify({'status': 'IN_PROGRESS', 'task_id': task_id})
        return response


class FileResultView(MethodView):
    @validate()
    def post(self, body: FileInput):
        task_id = body.task_id
        task = generate_large_file.AsyncResult(task_id)
        print(task.state)
        if task.state == 'PENDING':
            response = jsonify({'status': 'IS_PROGRESS'})
        elif task.state == 'SUCCESS':
            #Return the file once it's done
            file_path = os.path.abspath('large_file.csv')
            with open(file_path, 'r') as f:
                contents = f.read()
            os.remove(file_path)
            response = jsonify({'status': 'DONE', 'file_contents': contents})
            return response
        else:
            response = jsonify({'status': 'FAILED'})
        
        return response


        # Check the status of the task in Redis
        #status = str(redis_client.get(task_id), 'utf-8')
        # if task_result.successful():
        #     # Return the file once it's done
        #     file_path = os.path.abspath('large_file.csv')
        #     with open(file_path, 'r') as f:
        #         contents = f.read()
        #     os.remove(file_path)
        #     response = jsonify({'status': 'DONE', 'file_contents': contents})
        #     return response
        # else:
        #     response = jsonify({'status': 'UNKNOWN'})
        #     return response
    

file_views.add_url_rule('/api/v1/file', view_func=FileView.as_view('file_view'), methods=['POST'])
file_views.add_url_rule('/api/v1/file/result', view_func=FileResultView.as_view('file_res_view'), methods=['POST'])