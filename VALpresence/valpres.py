from conv import get_time
from pres import getpresence
import json
from pypresence import Presence
import time


client_id = ""#<- Your Client ID here
RPC = Presence(client_id)
RPC.connect()

def re():
    with open("file.txt","w") as f:
        json.dump(getpresence(),f)
    presenc_checker()

def presenc_checker():
    global x
    with open("file.txt") as f:
        x= json.load(f)
    valpresence()


def idle_pres():
    print("idle rpc")
    RPC.update(state="Away",large_image="idle")
    while True:
        time.sleep(5)
        re()
        


def valpresence():
    if x['isIdle']!=True:
        if x['isValid']==True:
            if x['matchMap']=="":
                print("lobby rpc")
                if x['partyState']!="MATCHMAKING":
                    if x['sessionLoopState']=='MENUS':
                        RPC.update( state="In Lobby",
                                    large_image="active",
                                    details=x['queueId'].upper()
                                  )
                        while True:
                            time.sleep(5)
                            re()
                            
                            
                
                
                elif x['partyState']=="MATCHMAKING":
                        RPC.update( state="Queing",large_image="active",
                                    details=x['queueId'].upper()
                                  )
                        while True:
                            time.sleep(5)
                            re()
                            

                        
            elif x['matchMap']!="": 
                if x['sessionLoopState']=="PREGAME":
                    mapname=x['matchMap'].split("/")
                    print(mapname[3].lower())
                    RPC.update( details="Agent Select",
                                large_image=(mapname[3].lower()),
                                start=get_time(x['queueEntryTime']),
                                large_text=mapname[2]
                              )
                    while True:
                        time.sleep(5)
                        re()

                elif x['sessionLoopState']=="INGAME":
                    mapname=x['matchMap'].split("/")
                    print(mapname[3].lower())
                    RPC.update( details="In a Match",
                                state=f"{x['queueId'].upper()} [{x['partyOwnerMatchScoreAllyTeam']}-{x['partyOwnerMatchScoreEnemyTeam']}]",
                                large_image=(mapname[3].lower()),
                                start=get_time(x['queueEntryTime']),
                                large_text=mapname[2]
                              )
                    while True:
                        time.sleep(5)
                        re()


            else:
                print("invalid")             
    else:
        idle_pres()
        
