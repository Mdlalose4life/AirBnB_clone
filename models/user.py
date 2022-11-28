from models.base_model import BaseModel


class User(BaseModel):
    """User Inherits from Basemodel"""

    email = ""
    password = ""
    first_name = ""
    last_name = ""
