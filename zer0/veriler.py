import os
import json
from pathlib import Path


cwd = Path(__file__).parents[0]
cwd = str(cwd)
print(f"(cwd)\n-----")




def lv_come(user):
    userID = str(user.id)
    with open('users.json', 'r') as f:
            users = json.load(f)

    return users[userID]['level']

  

def exp_come(user):
    userID = str(user.id)

    with open('users.json', 'r') as f:
            users = json.load(f)

    return users[userID]['experience']
              

def openfile():
    if os.path.isfile('veriler.json'):
        with open('veriler.json', 'r') as fp:
            data = json.load(fp)
            return data
    else:
        return None    

def setfile(data):
    if os.path.isfile('veriler.json'):
        with open('veriler.json', 'w') as fp:
            json.dump(data, fp, indent=4)        

def xp_ekle(user, xp):
    userID = str(user.id)

    level = {

        "deneme1" : 0,
        "deneme2" : 30,
        "deneme3" : 60,
        "deneme4" : 100,

    }


    if os.path.isfile('veriler.json'):
        with open('veriler.json', 'r') as fp:
            data = json.load(fp)

        if userID in data:
            data[userID]['name'] = user.name
            data[userID]['xp'] += xp
            for lvl in level:
                if xp >= level[lvl]:
                    data[userID]['level'] = lvl
                    break
            with open('veriler.json', 'w') as fp:
                json.dump(data, fp, indent=4)
        else:
            data[userID] = {}
            data[userID]['name'] = user.name
            data[userID]['xp']  = xp
            for lvl in level:
                if xp >= level[lvl]:
                    data[userID]['level'] = lvl
                    break
            with open('veriler.json', 'w') as fp:
                json.dump(data, fp, indent=4)
    else:
        data = {}
        data[userID] = {}
        data[userID]['name'] = user.name
        data[userID]['xp'] = xp
        for lvl in level:
            if xp >= level[lvl]:
                data[userID]['level'] = lvl
                break
        with open('veriler.json', 'w') as fp:
            json.dump(data, fp, indent=4)
        
def xp_getir(user):
    userID = str(user.id)
    if os.path.isfile('veriler.json'):
        with open('veriler.json', 'r') as fp:
            data = json.load(fp)

        return data[userID]['xp']
    else:
        return None

def level_Getir(user):
    userID = str(user.id)
    if os.path.isfile('veriler.json'):
        with open('veriler.json', 'r') as fp:
            data = json.load(fp)

        return data[userID]['level']

    else:
        return None


def set_afk(user, durum:str):
    userID = str(user.id)
    data = openfile()

    if data == None:
        data = {}
        data[userID] = {}
        data[userID]['afkdurum'] = durum
        setfile(data)

    else:
        if userID in data:
           data[userID]['afkdurum'] = durum
           setfile(data)
        else:
           data[userID] = {} 
           data[userID]['afkdurum'] = durum
           setfile(data)    
          
def get_afk(user):
    userID = str(user.id)
    data = openfile()

    if data == None:
        return None
    else:
        try:
           return data[userID]['afkdurum']    
        except KeyError:
            return None