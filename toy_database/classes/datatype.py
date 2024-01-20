# datatype.py

from toy_database.interfaces.idatatype import IDatatype
from typing import Tuple
# from typing import Optional

class MyDatatype(IDatatype):
    """ This class will do the encoding and decoding based on the data-type passed in the constructor"""

    def __init__(self, dtype:str):
        super().__init__()
        self._dtype = dtype

    @property
    def dtype(self):
        return self._dtype
    
    def encode(self, value:str )->bytes:

        if self._dtype == 'int':
            try:
                value_bytes = value.to_bytes(length=4, byteorder='big')
                return value_bytes
            except OverflowError as e:
                print(e)

        elif self._dtype == 'str':
            value_bytes = value.encode('utf-8')
            if len(value_bytes) >=20:
                raise OverflowError("Value should be less than 20 bytes. Please provide a shorter value")
            else:
                return value_bytes
            
        elif self._dtype == 'bool':
            value_bytes = value.to_bytes(lenght = 1, bytorder='big')
            return value_bytes
        # Todo : implement for float

    def decode(self, value:bytes)->str:
        pass