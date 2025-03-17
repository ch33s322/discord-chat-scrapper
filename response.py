from random import choice


async def scrape(channel) -> None:
    print(f'scrapping {channel}')
    rcount = 0
    lulcount = 0
    thiscount = 0
    lfgcount = 0
    realcount = 0
    hitcount = 0
    cbowcount = 0

    counter = 0
    #lists
    significant_messages = list()
    most_hyperlul = list()
    most_THIS = list()
    most_cbow = list()
    most_lfg = list()
    most_hit = list()
    most_real = list()


    def write_list(channel, emoji, list) -> None:
        f = open(f'{channel}-{emoji}.txt', 'w')
        for entry in list:
            f.write(str(entry) + '\n')
        f.close()


    async for message in channel.history(limit=999999):
        counter += 1
        if counter % 100 == 0:
            print(f'processed {counter} messages... \n{significant_messages.count()} significant messages so far')
        if message.reactions != list():
            if message.reactions[0].count >= 1:
                for react in message.reactions:
                    if str(react) == '<:hyperlul:821845277169811535>':
                        lulcount += react.count
                    elif str(react) == '<:THIS:871238720530055168>':
                        thiscount += react.count
                    elif str(react) == '<:LETSFUCKINKOOOOOOO:896082288612352000>':
                        lfgcount += react.count
                    elif str(react) == '<:HIT:1322082302372745286>':
                        hitcount += react.count
                    elif str(react) == '<:cowbowser:896862779913404427>':
                        cbowcount += react.count
                    elif str(react) == '💯':
                        realcount += react.count
                    rcount += react.count
        #put it on a list of interesting things
        if rcount >= 1:
            significant_messages.append([{'message_num': counter},  {'reactions': rcount}, {'message_content': message.content}, {'link': message.jump_url}])
        if lulcount >= 1:
            most_hyperlul.append([{'message_num': counter},  {'reactions': lulcount}, {'message_content': message.content}, {'link': message.jump_url}])
        if thiscount >= 1:
            most_THIS.append([{'message_num': counter},  {'reactions': thiscount}, {'message_content': message.content}, {'link': message.jump_url}])
        if cbowcount >= 1:
            most_cbow.append([{'message_num': counter},  {'reactions': cbowcount}, {'message_content': message.content}, {'link': message.jump_url}])
        if hitcount >= 1:
            most_hit.append([{'message_num': counter},  {'reactions': hitcount}, {'message_content': message.content}, {'link': message.jump_url}])
        if realcount >= 1:
            most_real.append([{'message_num': counter},  {'reactions': realcount}, {'message_content': message.content}, {'link': message.jump_url}])
        if lfgcount >= 1:
            most_lfg.append([{'message_num': counter},  {'reactions': lfgcount}, {'message_content': message.content}, {'link': message.jump_url}])
        #reset all our iterators
        rcount = 0
        lulcount = 0
        thiscount = 0    
        cbowcount = 0
        realcount = 0
        lfgcount = 0
        hitcount = 0
    #write results to file
    write_list(channel, 'all', significant_messages)
    write_list(channel, 'cbow', most_cbow)
    write_list(channel, 'hyperlul', most_hyperlul)
    write_list(channel, '100', most_real)
    write_list(channel, 'hit', most_hit)
    write_list(channel, 'lfg', most_lfg)
    write_list(channel, 'THIS', most_THIS)


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
    

