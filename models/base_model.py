import uuid
import datetime

class BaseModel:
    
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        if kwargs:
        # kwargs is not empty
        else:
        # kwargs is empty
        self.id = str(uuid.uuid4())
        self.created_at = datetime.datetime.now()
        self.updated_at = datetime.datetime.now()
        
    def __str__(self):
        return "[{}] ({}, {}) ".format(
            self.__class__.__name__, self.id, self.__dict__
    )
        
    def save(self):
        """Updates the public instance attribute updated_at with the current datetime."""
        self.updated_at = datetime.datetime.now()
        
    def to_dict(self):
        dict_ =  self.__dict__.copy()
        dict_["class"] = self.__class__.__name__
        dict_["created_at"] = self.created_at.isoformat()
        dict_["updated_at"] = self.updated_at.isoformat()
        return dict_
    
if __name__ == "__main__":
    base = BaseModel()
    print(base)