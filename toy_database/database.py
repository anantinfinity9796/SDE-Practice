# database.py

from interfaces.idatabase import Idatabase

class MyDatabase(Idatabase):
    """ This is the MyDatabase class which will implement a simple append only file database"""

    def __init__(self):
        super().__init__()

        self.max_key_length = 20
        self.max_value_length = 20
        self.key_offset_map  = {}

    def read(self, input_key:str)-> str:
        with open("./data/disk_dump.bat",'rb') as file:
            data = file.readlines()
            key_present = False
            for key_value_pair in data:
                # print(key_value_pair)
                key,value = key_value_pair[:21].replace(b'0',b'').decode(encoding='utf-8'), key_value_pair[21:].replace(b'0',b'').decode(encoding='utf-8')

                if key == input_key:
                    key_present = True
                    print(f"The pair is : {key} | {value}")
                    return value
            
            if not key_present:
                print("Key does not exist")
    
    def write(self, key:str, value:str)->str:
        if len(key) > self.max_key_length:
            print("Max allowed length of key exceeded | Please enter a shorter string")

        elif len(key) <= self.max_key_length:
            key = key.zfill(self.max_key_length)

        if len(value)>self.max_value_length:
            print("Max allowed length of value exceeded | Please enter a shorter string")
        elif len(value) <= self.max_value_length:
            value = value.zfill(self.max_value_length)


        # Store the key and the offset of its value in the in-memory dictionary
            
        key_binary_repr = key.encode('utf-8')
        value_binary_repr = value.encode('utf-8')
        line_sep_binary_repr = '\n'.encode('utf-8')

        try:
            with open('./data/disk_dump.bat', 'ab') as file:
                file.write(key_binary_repr)
                file.write(value_binary_repr)
                file.write(line_sep_binary_repr)
                print(f"Write successful")
        except Exception as e:
            print("Write not successful")
            print(e)
        return
