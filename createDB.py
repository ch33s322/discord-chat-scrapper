#Dakota Deets 6/30/2026
#program to create the discord scraper database

import sqlite3

def createSchema(conn):
    cursor = conn.cursor()
    #messages table
    messagesSQL = """CREATE TABLE IF NOT EXISTS messages (
                ID INTEGER PRIMARY KEY AUTOINCREMENT,
                mID INTEGER NOT NULL, 
                channel TEXT NOT NULL,
                userName TEXT NOT NULL,
                link TEXT NOT NULL,
                messageContent TEXT NOT NULL
                )"""
    cursor.execute(messagesSQL)
    print(messagesSQL)



    #reacts table
    reactSQL = """CREATE TABLE IF NOT EXISTS reactions (
                mID INTEGER NOT NULL, 
                name TEXT NOT NULL,
                Number INTEGER NOT NULL
            )"""
    cursor.execute(reactSQL)
    print(reactSQL)

    # Save changes
    conn.commit()

    # Close the connection
    conn.close()

    print("schema created")


# main
def main():
    conn = sqlite3.connect('library.db')  # Creates a new database file if it doesn’t exist
    createSchema(conn)










# run main
# __name__
if __name__=="__main__":
    main()