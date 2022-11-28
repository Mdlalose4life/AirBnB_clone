from datetime import datetime
import uuid
import models


class BaseModel:
    """The class that defines all
    common attributes/Methods for other classes"""

    def __init__(self, *argrs, **kwargs):
        """Base class initilization of"""
        if kwargs:
            for each_key, each_value in kwargs.iterm():
                if each_key == "created_at":
                    format = "%Y-%m-%dT%H:%M:%S.%f"
                    object = datetime.strptime(each_value, format)
                    setattr(self, each_key, object)

        elif each_key != '__class__':
            setattr(self, each_key, each_value)

        else:
            self.id = str(uuid.uuid4())
            self.created_at = datetime.now()
            self.updated_at = datetime.now()
            models.storage.new(self)

    def __str__(self):
        """ Returns a string representation """
        return f"[{self.__class__.__name__}]({self.id}){self.__dict__}"

    def save(self):
        """ update the public instance attribute
        updated_at with the current datetime """
        self.updated_at = datetime.now()
        models.storage.save()

    def to_dict(self):
        """ Returns a dictionary
        representation containing keys/values of __dict__"""
        my_dict = dict(self.__dict__)
        my_dict["__class__"] = self.__class__.__name__
        my_dict["created_at"] = self.created_at.isoformat()
        my_dict["updated_at"] = self.updated_at.isoformat()
        return my_dict
