# app2.py

from toy_database.classes.datatype_int import Datatype
from toy_database.classes.database import Database




def main():
    # Start the database
    print("Initializing the database....")
    db_shutdown=False
    db = Database()
    while db_shutdown != True:
        action = ''
        while action not in ['r','w','quit']:
            action = input(f"Read/Write/Quit ? (r/w/quit): ")
        
        # When we get the action we perform the reads and writes according to it
        if action == 'w':
            db.write()
        elif action == 'r':
            db.read()
        elif action =='quit':
            db_shutdown=True
            print(f"Shutting Down....")
            break


    return


if __name__=="__main__":
    main()