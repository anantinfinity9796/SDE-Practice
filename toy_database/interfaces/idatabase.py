# idatabase.py
# This is the iterface class of the database class.

class Idatabase():
    """Interface for Database class"""
    
    def __init__(self):
        pass
    
    def read(self, key:str)->tuple:
        pass
    
    def write(self, key, value):
        pass

    def collection_metadata_update(self):
        pass
