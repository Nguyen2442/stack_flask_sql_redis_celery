from typing import Optional
from pydantic import BaseModel, validator
from app.core.exceptions import ErrorResponseException
from app.core.schema.api_response import get_error_code

        

class FileInput(BaseModel):
    task_id: str