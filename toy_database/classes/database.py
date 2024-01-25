# database.py

from toy_database.interfaces.idatabase import Idatabase
from toy_database.classes.datatype_int import MyIntDatatype
from toy_database.classes.datatype_str import MyStrDatatype
from query_parser import QueryParser
from storage_engine import StorageEngine
from collection_metadata import CollectionMetadata
from storage_engine import StorageEngine

class Database(Idatabase):
    def __init__(self):
        super().__init__()
        self._query_parser = QueryParser()
        self._key_dtype_offset_map = {}
        # self._collection_metadata_object = CollectionMetadata()
        self._intger_encoder_decoder = MyIntDatatype()
        self._string_encode_decoder = MyStrDatatype()
        self._storage_engine = StorageEngine() 

    def read(self) -> tuple:
        return 
    
    def write(self):
        """ This will write the data to the required collection file and also place the keys, datatype and offset info in the
            in-memory dict"""
        # first we will need to read the user query
        query_object = self._query_parser.get_query_string_and_parse_query()

        # Then get the filename and offset from the collection_metadata_object
        # filename = self._collection_metadata_object.read_collection_metadata(query_object.dtype)

        # Now get the encoded bytes according to the datatypes.
        if query_object.dtype == 'int':
            encoded_string = self._intger_encoder_decoder.encode(query_object.key_name, query_object.dtype, query_object.key_value)
        elif query_object.dtype == 'str':
            encoded_string = self._intger_encoder_decoder.encode(query_object.key_name, query_object.dtype, query_object.key_value)

        # Now we have got the encoded string and now what we will do is that we will use the storage layer to write our data.
        self._storage_engine.write_to_file(encoded_bytes=encoded_string,
                                           dtype=query_object.dtype)

        
        return