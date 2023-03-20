from typing import Optional
from pydantic import BaseModel, validator
from app.core.exceptions import ErrorResponseException
from app.core.schema.api_response import get_error_code

        

class AuthLoginInput(BaseModel):
    email: str
    password: str

    # @validator('')
    # def check_username(cls, v):
    #     if v.isdigit():
    #         print(100*" false ")
    #         return v
    #     else:
    #         print(10*"here ? ")
    #         raise ErrorResponseException(**get_error_code(3001))
