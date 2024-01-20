# app2.py

from classes.datatype import Datatype
from classes.storage_engine import StorageEngine
from classes.collection_metadata import CollectionMetadata




def main():
    # before  that we will need to 
    # Start the database
    print("Initializing the database....")
    db_shutdown=False
    while db_shutdown != True:
        action = ''
        # Get keys and values from the user
        while action not in ['r','w','quit']:
            action = input(f"Read/Write/Quit ? (r/w/quit): ")
        
        # When we get the action we perform the reads and writes according to it
        if action == 'w':
            key, value = get_write_key_value_data_from_user()
            # db.write(key, value)
        elif action == 'r':
            key = get_key_for_read()
            # db.read(key)
        elif action =='quit':
            db_shutdown=True
            print(f"Shutting Down....")
            break


    return




if __name__=="__main__":
    main()