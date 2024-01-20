# datatype.py

from toy_database.interfaces.idatatype import IDatatype
from typing import Tuple
# from typing import Optional

class Datatype(IDatatype):
    """ Class for encodng and decoding the key-value pairs of the data according to data-types """

    def __init__(self,):
        super().__init__()
        self._dtypemapper = {
                                "int":int,
                                "float":float,
                                "str":str,
                                "bool":bool
                             }
    
    def encode(self, value_dtype:str, value:str )->bytes:
        pass

    def decode(self, value:bytes)->str:
        pass