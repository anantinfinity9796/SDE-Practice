# storage_engine.py

from toy_database.interfaces.istorage_engine import IStorageEngine

class StorageEngine(IStorageEngine):
    def __init__(self):
        super().__init__()
        pass

    def read_from_file(self, key:bytes, filename:str) -> bytes:

        pass

    def write_to_file(self, key:bytes, value:bytes):
        """ 
        Function to put the data into the files
        Input --> key: bytes, value:bytes
        Ouptut --> None
        """
        # Now first we will also need to get which collection do we write to depending on the data type of the key.

        pass