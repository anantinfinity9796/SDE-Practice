# idatatype.py

class IDatatype():
    def __init__(self, dtype:str):
        pass

    def encode(self) -> bytes:
        """This function will encode the value passed in it based on the datatype"""
        pass

    def decode(self, value:bytes) -> str:
        """ This function will decode the bytes passed in according to the dtype and convert it to a str"""
        pass