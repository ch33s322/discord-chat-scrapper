from random import choice
from operator import itemgetter
import datetime
import sqlite3


def insertMessage(message):
    conn = sqlite3.connect('library.db')  # Creates a new database file if it doesn’t exist
    cursor = conn.cursor()
    messageID = message.id
    userName = message.author.name
    link = message.jump_url
    content = message.content
    channel = message.channel.name
    sql = f"""INSERT INTO messages (mID, channel, userNAme, link, messageContent)
             VALUES (?, ?, ?, ?, ?); """
    cursor.execute(sql, (messageID, channel, userName, link, content))
    # Save changes
    conn.commit()
    # Close the connection
    conn.close()

def insertReaction(message, r):
    conn = sqlite3.connect('library.db')  # Creates a new database file if it doesn’t exist
    cursor = conn.cursor()
    messageID = message.id
    react = r
    sql = f"""INSERT INTO reactions (mID, name, number)
             VALUES (?, ?, ?); """
    cursor.execute(sql, (messageID, str(react.emoji), react.count))
    # Save changes
    conn.commit()
    # Close the connection
    conn.close()


async def scrape(channel) -> None:
    print(f'scrapping {channel}')
    rcount = 0
    counter = 0

    async for message in channel.history(limit=999999, after=datetime.datetime.utcnow()-datetime.timedelta(days=365)): #after=datetime.datetime.utcnow()-datetime.timedelta(days=365)
        counter += 1
        if counter % 100 == 0:
            print(f'processed {counter} messages... \n')

        insertMessage(message)

        if message.reactions != list():
            if message.reactions[0].count >= 1:
                for react in message.reactions:
                    insertReaction(message, react)

    print(f'{counter} messages where processed in {channel}')
    


async def get_response(user_input: str, channel) -> str:
    lowered: str = user_input.lower()

    if lowered == '!scrape':
        #start scraping the entire server for info
        await scrape(channel)
        return 'channel fully scraped.'
    else:
        #do nothing
        return ''
    

