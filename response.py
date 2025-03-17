from random import choice


async def scrape(channel) -> None:
    print(f'scrapping {channel}')
    rcount = 0
    lulcount = 0
    thiscount = 0

    counter = 0
    #lists
    significant_messages = list()
    most_hyperlul = list()
    most_THIS = list()


    def myFunc(e):
        return e['reactions']

    async for message in channel.history(limit=999999):
        counter += 1
        if counter % 100 == 0:
            print(f'processed {counter} messages... \n{significant_messages.count()} significant messages so far')
        if message.reactions != list():
            if message.reactions[0].count >= 1:
                for react in message.reactions:
                    if react.emoji.name:
                        match str(react.emoji.name):
                            case 'hyperlul':
                                lulcount += react.count
                            case 'THIS':
                                thiscount += react.count
                    rcount += react.count
        #put it on a list of interesting things
        if rcount >= 1:
            significant_messages.append([{'message_num': counter},  {'reactions': rcount}, {'message_content': message.content}, {'link': message.jump_url}])
        if lulcount >= 1:
            most_hyperlul.append([{'message_num': counter},  {'reactions': lulcount}, {'message_content': message.content}, {'link': message.jump_url}])
        if thiscount >= 1:
            most_THIS.append([{'message_num': counter},  {'reactions': thiscount}, {'message_content': message.content}, {'link': message.jump_url}])
        #reset all our iterators
        rcount = 0
        lulcount = 0
        thiscount = 0
    print((significant_messages[0][0]))                # <class 'list'>    <---- check the data type
    #significant_messages.sort(key=myFunc)
    print(f'{counter} messages where processed in {channel}')
   


async def get_response(user_input: str, channel) -> str:
    lowered: str = user_input.lower()

    if lowered == '!scrape':
        #start scraping the entire server for info
        await scrape(channel)
        return 'channel fully scraped, file name:'
    else:
        #do nothing
        return ''
    

