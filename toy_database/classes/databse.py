# database.py

from toy_database.interfaces.idatabase import Idatabase
from datatype import Datatype
from query_parser import QueryParser
from storage_engine import StorageEngine
from collection_metadata import CollectionMetadata

class Database(Idatabase):
    def __init__(self):
        self._query_parse = QueryParser()
        super().__init__()

    def read(self, key: str) -> tuple:
        return 
    
    def write(self, key, key_type:str, value):
        
        
        return