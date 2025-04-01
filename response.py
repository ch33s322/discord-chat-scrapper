from random import choice
from operator import itemgetter


async def scrape(channel) -> None:
    print(f'scrapping {channel}')
    rcount = 0
    lulcount = 0
    thiscount = 0
    lfgcount = 0
    realcount = 0
    hitcount = 0
    misscount = 0
    cbowcount = 0
    matpatcount = 0
    villcount = 0
    sadgrycount = 0
    cbowthumbcount = 0
    bonkcount = 0
    firecount = 0
    repostcount = 0


    counter = 0
    #lists
    significant_messages = list()
    most_hyperlul = list()
    most_THIS = list()
    most_cbow = list()
    most_lfg = list()
    most_hit = list()
    most_real = list()
    most_miss = list()
    most_matpat = list()
    most_vill = list()
    most_sadgry = list()
    most_cbowthumb = list()
    most_bonk = list()
    most_fire = list()
    most_repost = list()


    def write_list(channel, emoji, list) -> None:
        f = open(f'{channel}-{emoji}.txt', 'w', encoding="utf-8")
        for entry in list:
            f.write(str(entry) + '\n')
        f.close()

    def sort_list_data(list) -> list:
        return sorted(list, key=itemgetter(1))



    async for message in channel.history(limit=999999):
        counter += 1
        if counter % 100 == 0:
            print(f'processed {counter} messages... \n{len(significant_messages)} significant messages so far')
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
                    elif str(react) == '<:MISS:1322082326611755171>':
                        misscount += react.count
                    elif str(react) == '🔥':
                        firecount += react.count
                    elif str(react) == '<:pain:900784292492365915>':
                        sadgrycount += react.count
                    elif str(react) == '<:yourepostedinthewrongguild:1182358903959335044>':
                        repostcount += react.count
                    elif str(react) == '<:herm:771547713543733268>':
                        villcount += react.count
                    elif str(react) == '<:MatPat:804046397586407464>':
                        matpatcount += react.count
                    elif str(react) == '<:cowbowserthumb:758107973066162226>':
                        cbowthumbcount += react.count
                    elif str(react) == '<:BONK:776198945416151040>':
                        bonkcount += react.count
                    rcount += react.count
        #put it on a list of interesting things
        if rcount >= 1:
            significant_messages.append([counter, rcount, message.content, message.jump_url])
        if lulcount >= 1:
            most_hyperlul.append([counter,  lulcount, message.content, message.jump_url])
        if thiscount >= 1:
            most_THIS.append([counter,  thiscount, message.content, message.jump_url])
        if cbowcount >= 1:
            most_cbow.append([counter,  cbowcount, message.content, message.jump_url])
        if hitcount >= 1:
            most_hit.append([counter,  hitcount, message.content, message.jump_url])
        if realcount >= 1:
            most_real.append([counter,  realcount, message.content, message.jump_url])
        if lfgcount >= 1:
            most_lfg.append([counter,  lfgcount, message.content, message.jump_url])
        if misscount >= 1:
            most_miss.append([counter,  misscount, message.content, message.jump_url])
        if matpatcount >= 1:
            most_matpat.append([counter,  matpatcount, message.content, message.jump_url])
        if bonkcount >= 1:
            most_bonk.append([counter,  bonkcount, message.content, message.jump_url])
        if firecount >= 1:
            most_fire.append([counter,  firecount, message.content, message.jump_url])
        if villcount >= 1:
            most_vill.append([counter,  villcount, message.content, message.jump_url])
        if repostcount >= 1:
            most_repost.append([counter,  repostcount, message.content, message.jump_url])
        if sadgrycount >= 1:
            most_sadgry.append([counter,  sadgrycount, message.content, message.jump_url])
        #reset all our iterators
        rcount = 0
        lulcount = 0
        thiscount = 0    
        cbowcount = 0
        realcount = 0
        lfgcount = 0
        hitcount = 0
        sadgrycount = 0
        misscount = 0
        villcount = 0
        firecount = 0
        matpatcount = 0
        bonkcount = 0
        repostcount = 0

    #sort all our lists
    significant_messages = sort_list_data(significant_messages)
    most_cbow = sort_list_data(most_cbow)
    most_cbowthumb = sort_list_data(most_cbowthumb)
    most_hyperlul = sort_list_data(most_hyperlul)
    most_lfg = sort_list_data(most_lfg)
    most_real = sort_list_data(most_real)
    most_bonk = sort_list_data(most_bonk)
    most_fire = sort_list_data(most_fire)
    most_hit = sort_list_data(most_hit)
    most_miss = sort_list_data(most_miss)
    most_matpat = sort_list_data(most_matpat)
    most_repost = sort_list_data(most_repost)
    most_sadgry = sort_list_data(most_sadgry)
    most_THIS = sort_list_data(most_THIS)
    most_vill = sort_list_data(most_vill)



    #write results to file
    write_list(channel, 'all', significant_messages)
    write_list(channel, 'cbow', most_cbow)
    write_list(channel, 'hyperlul', most_hyperlul)
    write_list(channel, '100', most_real)
    write_list(channel, 'hit', most_hit)
    write_list(channel, 'lfg', most_lfg)
    write_list(channel, 'THIS', most_THIS)
    write_list(channel, 'matpat', most_matpat)
    write_list(channel, 'bonk', most_bonk)
    write_list(channel, 'cbowthumb', most_cbowthumb)
    write_list(channel, 'miss', most_miss)
    write_list(channel, 'repost', most_repost)
    write_list(channel, 'herm', most_vill)
    write_list(channel, 'sadgry', most_sadgry)



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
    

