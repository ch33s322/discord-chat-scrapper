#Dakota Deets 6/30/2026
#program to create the discord scraper database

import sqlite3

def createSchema(conn):
    cursor = conn.cursor()
    #messages table
    sql = """CREATE TABLE IF NOT EXISTS messages (
                id INTEGER PRIMARY KEY AUTOINCREMENT, 
                userName TEXT NOT NULL,
                link TEXT NOT NULL,
                messageContent TEXT NOT NULL,
                react1 INTEGER,
                react2 INTEGER,
                react3 INTEGER,
                react4 INTEGER,
                react5 INTEGER,
                react6 INTEGER,
                react7 INTEGER,
                react8 INTEGER,
                react9 INTEGER,
                react10 INTEGER,
                react11 INTEGER,
                react12 INTEGER,
                react13 INTEGER,
                react14 INTEGER,
                react15 INTEGER,
                react16 INTEGER,
                react17 INTEGER,
                react18 INTEGER,
                react19 INTEGER,
                react20 INTEGER,
                react21 INTEGER,
                react22 INTEGER,
                react23 INTEGER,
                react24 INTEGER,
                react25 INTEGER,
                react26 INTEGER,
                react27 INTEGER,
                react28 INTEGER,
                react29 INTEGER,
                react30 INTEGER
            );"""
    cursor.execute(sql)
    print(sql)

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