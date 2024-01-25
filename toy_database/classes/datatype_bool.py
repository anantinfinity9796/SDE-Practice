# datatype_bool.py

from toy_database.interfaces.idatatype import IDatatype

class MyBoolDatatype(IDatatype):
    """ This class will do the encoding and decoding based on the data-type passed in the constructor"""

    def __init__(self, dtype:str):
        super().__init__()
        self._dtype = dtype
        self._filename = 'collection_bool.dat'

    @property
    def dtype(self):
        return self._dtype
    
    def encode(self, value:str )->bytes:
        dtype_bytes = self._dtype.zfill(5).encode(encoding='utf-8')
        value_bytes = value.to_bytes(length = 1, bytorder='big')
        return (dtype_bytes, value_bytes)
    
    def decode(self, bytestring:bytes)->str:
        # So for the datatype we will see the first 5 bytes for the bytearray and then 
        pass