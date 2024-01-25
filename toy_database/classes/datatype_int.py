# datatype.py

from toy_database.interfaces.idatatype import IDatatype
from typing import Tuple
# from typing import Optional
from collection_metadata import CollectionMetadata

class MyIntDatatype(IDatatype):
    """ This class will do the encoding and decoding based on the data-type passed in the constructor"""

    def __init__(self):
        super().__init__()
        self._dtype = 'int'
        self._filename = 'collection_int.dat'

    @property
    def dtype(self):
        return self._dtype
    
    def encode(self, key:str, value_dtype:str, value:str )->bytes:

        key_bytes = key.encode()
        key_bytes_len = len(key_bytes).to_bytes(length=4, byteorder='big')
        value_dtype_encoded = value_dtype.encode()
        value_dtype_bytes_len = len(value_dtype_encoded).to_bytes(length=4, byteorder='big')
        value_bytes_encoded = value.to_bytes(length=4, byteorder='big')
        value_byte_encoded_len = len(value_bytes_encoded).to_bytes(length=4, byteorder='big')

        bytes_encoded_array = key_bytes_len \
                             + key_bytes \
                             + value_dtype_bytes_len \
                             + value_dtype_encoded \
                             + value_byte_encoded_len \
                             + value_bytes_encoded
        
        return bytes_encoded_array
        # try:
        #     dtype_bytes = self._dtype.zfill(5).encode(encoding='utf-8')
        #     value_bytes = value.to_bytes(length=4, byteorder='big')
        #     return (dtype_bytes, value_bytes)
        # except OverflowError as e:
        #     print(e)

    def decode(self, bytes_encoded_array:bytes)->str:
        # So for the datatype we will see the first 5 bytes for the bytearray and then 
        reader_pointer = 0
        key_len = int.from_bytes(bytes_encoded_array[reader_pointer:reader_pointer+4], byteorder='big')
        reader_pointer +=4
        key = bytes_encoded_array[reader_pointer:reader_pointer+key_len].decode()
        reader_pointer +=key_len
        value_dtype_len = int.from_bytes(bytes_encoded_array[reader_pointer:reader_pointer+4], byteorder='big')
        reader_pointer +=4
        value_dtype = bytes_encoded_array[reader_pointer:reader_pointer+value_dtype_len].decode()
        reader_pointer +=value_dtype_len
        value_length = int.from_bytes(bytes_encoded_array[reader_pointer:reader_pointer+4], byteorder='big')
        reader_pointer +=4
        value = int.from_bytes(bytes_encoded_array[reader_pointer:reader_pointer+value_length], byteorder='big')

        return (key, value_dtype, value)