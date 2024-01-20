# collection_metadata.py

from interfaces.icollection_metadata import ICollectionMetadata


class CollectionMetadata(ICollectionMetadata):
    """ 1. Class for defining the metadata of the collections.
        2. We will have dytpe:filename mapping and we will have adding methods to add dtypes.
    """

    def __init__(self):
        self._metadata_dict = {}

    def read_collection_metadata(self, dtype:str):
        return self._metadata_dict[dtype]
    
    def write_new_collection_metadata(self, dtype:str):
        """ This function will write the metadata into the dict"""
        if dtype in self._metadata_dict.keys():
            print("Dtype already present. No need to add")

        else:
            # We will define the filename based on the data_type | Data repr : <<key_len><key>:string<valuelen><value>:collection_type>>
            if dtype in ['int','str','float','bool']:
                filename = f"collection_{dtype}.bat"
                self._metadata_dict[dtype] = filename
            else:
                raise ValueError("Provided dtype not supported. | Supported dtypes are ['int','str','float','bool']")
            
        return