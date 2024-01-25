# storage_engine.py

from toy_database.classes.collection_metadata import CollectionMetadata
from toy_database.interfaces.istorage_engine import IStorageEngine

class StorageEngine(IStorageEngine):
    def __init__(self):
        super().__init__()
        self._collection_metadata_object = CollectionMetadata()

    def read_from_file(self, key:bytes, dtype) -> bytes:
        pass

    def write_to_file(self, encoded_bytes:bytes, dtype:str):
        """ 
        Function to put the data into the files
        Input --> key: bytes, value:bytes
        Ouptut --> None
        """
        filename = self._collection_metadata_object.read_collection_metadata(dtype)

        try:
            with open(filename, 'ab') as file:
                file.write(encoded_bytes)
        except Exception as e:
            print(f"Failure writing to the {filename} collection")
            print(e)
        # Now first we will also need to get which collection do we write to depending on the data type of the key.
        pass