# app.py
# This will initialize the database engine and try to control reads and writes
# The database read and write for now is in a single class which might violate the single responsibility principle. Not sure, we'll see.

from database import MyDatabase

def get_write_key_value_data_from_user()->tuple:
    key=None
    value = None
    while (key== None) or (len(key)>20):
        key = input(f'Enter the key of the data (should be less than 20 characters): ')

    while (value== None) or (len(value)>20):
        value = input(f"Enter the value of the data (should be less than 20 characters): ")

    return (key, value)

def get_key_for_read()->str:
    key = ''
    while len(key)==0:
        key = input(f"Enter the key for which you want the value: ")
    return key


def main():
    # Create the database object and start the loop
    print("Initializing the database....")
    db = MyDatabase()
    db_shutdown = False

    while db_shutdown != True:
        action = ''
        # Get keys and values from the user
        while action not in ['r','w','quit']:
            action = input(f"Read/Write/Quit ? (r/w/quit): ")

        if action == 'w':
            key, value = get_write_key_value_data_from_user()
            db.write(key, value)
        elif action == 'r':
            key = get_key_for_read()
            db.read(key)
        elif action =='quit':
            db_shutdown=True
            print(f"Shutting Down....")
            break

    

    return

if __name__=='__main__':
    main()

