import os
import json
from pathlib import Path


cwd = Path(__file__).parents[0]
cwd = str(cwd)
print(f"(cwd)\n-----")



def set_channel(channel):
    channelID = channel.id
    guildID = str(channel.guild.id)


    if os.path.isfile('sunucular.json'):
        with open('sunucular.json', 'r') as fp:
           myGuild = json.load(fp)
        if guildID in myGuild:
           myGuild[guildID]['hgkanali'] = channelID 
           with open('sunucular.json', 'w') as fp:
               json.dump(myGuild, fp,indent=4)
        else:
           myGuild[guildID] = {}
           myGuild[guildID]['hgkanali'] = channelID     
           with open('sunucular.json', 'w') as fp:
               json.dump(myGuild, fp,indent=4)
    else:
        myGuild = {}
        myGuild[guildID] = {}
        myGuild[guildID]['hgkanali'] = channelID 
        with open('sunucular.json', 'w') as fp:
               json.dump(myGuild, fp,indent=4)


def get_channel(guild):
    guildID = str(guild.id) 
    if os.path.isfile('sunucular.json'):          
        with open('sunucular.json', 'r') as fp:
            myGuild = json.load(fp)
        if guildID in myGuild:
            try:
                return myGuild[guildID]['hgkanali']
            except:
                return None

        else:
            return None                
    else:
        return None



def set_otorol(guild, role, value=1):
    roleID = role.id
    guildID = str(guild.id)
    if value == 0:
        roleID = '0'

    if os.path.isfile('sunucular.json'):
        with open('sunucular.json', 'r') as fp:
           myGuild = json.load(fp)
        if guildID in myGuild:
           myGuild[guildID]['otorol'] = roleID 
           with open('sunucular.json', 'w') as fp:
               json.dump(myGuild, fp,indent=4)
        else:
           myGuild[guildID] = {}
           myGuild[guildID]['otorol'] = roleID     
           with open('sunucular.json', 'w') as fp:
               json.dump(myGuild, fp,indent=4)
    else:
        myGuild = {}
        myGuild[guildID] = {}
        myGuild[guildID]['otorol'] = roleID 
        with open('sunucular.json', 'w') as fp:
               json.dump(myGuild, fp,indent=4)


def get_otorol(guild):
    guildID = str(guild.id) 
    if os.path.isfile('sunucular.json'):          
        with open('sunucular.json', 'r') as fp:
            myGuild = json.load(fp)
        if guildID in myGuild:
            try:
                return myGuild[guildID]['otorol']
            except:
                return None

        else:
            return None                
    else:
        return None        





def set_reklam(guild, value=1):
    guildID = str(guild.id)

    if os.path.isfile('sunucular.json'):
        with open('sunucular.json', 'r') as fp:
           myGuild = json.load(fp)
        if guildID in myGuild:
           myGuild[guildID]['reklam'] = value 
           with open('sunucular.json', 'w') as fp:
               json.dump(myGuild, fp,indent=4)
        else:
           myGuild[guildID] = {}
           myGuild[guildID]['reklam'] = value     
           with open('sunucular.json', 'w') as fp:
               json.dump(myGuild, fp,indent=4)
    else:
        myGuild = {}
        myGuild[guildID] = {}
        myGuild[guildID]['reklam'] = value 
        with open('sunucular.json', 'w') as fp:
               json.dump(myGuild, fp,indent=4)

def get_reklam(guild):
    guildID = str(guild.id) 
    if os.path.isfile('sunucular.json'):          
        with open('sunucular.json', 'r') as fp:
            myGuild = json.load(fp)
        if guildID in myGuild:
            try:
                return myGuild[guildID]['reklam']
            except:
                return None

        else:
            return None                
    else:
        return None   


def set_kufur(guild, value=1):
    guildID = str(guild.id)

    if os.path.isfile('sunucular.json'):
        with open('sunucular.json', 'r') as fp:
           myGuild = json.load(fp)
        if guildID in myGuild:
           myGuild[guildID]['kufur'] = value 
           with open('sunucular.json', 'w') as fp:
               json.dump(myGuild, fp,indent=4)
        else:
           myGuild[guildID] = {}
           myGuild[guildID]['kufur'] = value     
           with open('sunucular.json', 'w') as fp:
               json.dump(myGuild, fp,indent=4)
    else:
        myGuild = {}
        myGuild[guildID] = {}
        myGuild[guildID]['kufur'] = value 
        with open('sunucular.json', 'w') as fp:
               json.dump(myGuild, fp,indent=4)

def get_kufur(guild):
    guildID = str(guild.id) 
    if os.path.isfile('sunucular.json'):          
        with open('sunucular.json', 'r') as fp:
            myGuild = json.load(fp)
        if guildID in myGuild:
            try:
                return myGuild[guildID]['kufur']
            except:
                return None

        else:
            return None                
    else:
        return None          