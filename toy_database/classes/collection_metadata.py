# collection_metadata.py

from interfaces.icollection_metadata import ICollectionMetadata


class CollectionMetadata(ICollectionMetadata):
    """ Class for defining the metadata of the collections"""

    def __init__(self, collection_type:str, ):
        # self._metadata_dict = {}
        self._collection_type = collection_type
        self._key_valueoffset_dict = {}

        # We will define the filename based on the data_type | Data repr : <<key_len><key>:string<valuelen><value>:collection_type>>
        self._filename = f"collection_{collection_type}.bat"

    
    @property
    def collection_type(self):
        return self._collection_type


    def read_metadata(self, dtype:str):
        if dtype =='int':
            
        pass
    
    def write_metadata(self, ):
        """ This function will write the metadata into the dict"""
        pass