# query_parse.py

from toy_database.interfaces.iquery_parser import IQueryParser
from typing import Tuple


class QueryParser(IQueryParser):
    def __init__(self):
        super().__init__()
        self._key_name = None
        self._key_dtype = None
        self._key_value = None
        return
    
    @property
    def key_name(self):
        return self._key_name
    
    @property
    def key_dtype(self):

        return self._key_dtype
    
    @property
    def key_value(self):
        return self._key_value
    
    def __query_parser(self, query_string:str):
        """ This is private method for parsing the query"""
        if query_string=="":
            return None
        else:
            try:
                # Splitting the query_string into a list and casting it to a tuple with datatypes predefined using typing module
                dtype_key_value_split = query_string.split(' ')[0]
                key_dtype, key_value_pair_split = dtype_key_value_split[0], dtype_key_value_split[1].split(':')
                key_name, key_value = key_value_pair_split[0]
                # query_string_split: Tuple[int|str|float|bool, str,str] = tuple(query_string.split(' '))
            except Exception as e:
                # print("Either <value_dtype> is incorrect or <query_string_name> not provided")
                print("Incorrrect Query Format | Correct Format : <value_dtype> key_name:value ")
                print(e)
                return None
        
        return key_dtype, key_name, key_value

    def get_query_string_and_parse_query(self):
        query_string_correctness = False

        # now parse the given query_string into the query_string_dtype, query_string_name
        while query_string_correctness!=True:
            query_string = input("Enter '<value_dtype> key_name:value' e.g: 'str employee1:Anant'")

            parse_query_string_output = self.__parse_query_string(query_string=query_string)

            if parse_query_string_output !=None:
                query_string_correctness=True

                key_dtype, key_name, key_value = parse_query_string_output[0], parse_query_string_output[1], parse_query_string_output[2]

                if key_dtype in ['int','str','float','bool']:
                    self._key_dtype = key_dtype
                    self._key_name = key_name
                    self._key_value = key_value
                else:
                    print("Unsupported key_dtype | Supported dtypes are : ['int','str','float','bool']")
            else:
                continue

        return