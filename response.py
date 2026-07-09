from random import choice
from operator import itemgetter
import datetime



def insertMessage(message, c):
    conn = sqlite3.connect('library.db')  # Creates a new database file if it doesn’t exist

    messageID = message.ID
    userName = message.author
    link = message.jump_url
    content = message.content
    channel = c
    sql = f"""INSERT INTO messages (mID, channel, userNAme, link, content)
             VALUES ({messageID}, {channel}, {userName}, {link}, {content}); """
    cursor.execute(sql)
    print(sql)
    # Save changes
    conn.commit()
    # Close the connection
    conn.close()

def insertReaction(message, r):
    messageID = message.ID
    react = r
    sql = f"""INSERT INTO reactions (mID, reactID, name, number)
             VALUES ({messageID}, {channel}, {react}, {react.count}); """
    cursor.execute(sql)
    print(sql)
    # Save changes
    conn.commit()
    # Close the connection
    conn.close()


async def scrape(channel) -> None:
    print(f'scrapping {channel}')
    rcount = 0
    counter = 0

    async for message in channel.history(limit=999999, after=datetime.datetime.utcnow()-datetime.timedelta(days=365)):
        counter += 1
        if counter % 100 == 0:
            print(f'processed {counter} messages... \n{len(significant_messages)} significant messages so far')

        insertMessage(message, channel)

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
    

