
import config
from pyrogram import Client, filters
import sqlite3
from time import sleep
import asyncio
import requests
import json
import threading
import websocket




botTG = Client("bot", api_id=config.API_ID, api_hash=config.API_HASH,
    bot_token=config.TOKENTG)


#DATA STRUCTURE

datasheet = ''
to_retranslate = ''



def send_json_request(ws, request):
    ws.send(json.dumps(request))


def recieve_json_response(ws):
    response = ws.recv()
    if response:
        return json.loads(response)


def heartbeat(interval, ws):
    print('so it begins')
    while True:
        sleep(interval)
        heartbeatJSON = {
        "op": 1,
        "d": "null"
        }

        send_json_request(ws, heartbeatJSON)
        print("so it sent")

def retranslate():
    global to_retranslate

    time_to_sleep_when_captcha = 5
    ws = websocket.WebSocket()
    ws.connect('wss://gateway.discord.gg/?v=9&encoding=json')
    event = recieve_json_response(ws)

    heartbeat_interval = event['d']['heartbeat_interval'] / 1000
    threading._start_new_thread(heartbeat, (heartbeat_interval, ws))
    payload = {
        'op': 2,
        'd': {
        "token": config.token,
        "properties": {
        "$os": "linux",
        "$browser": "firefox",
        "$device": 'pc'
            }
        }
    }

    send_json_request(ws, payload)
       
    event = recieve_json_response(ws)

    try:
        print(f"{event['d']['author']['username']}: {event['d']['content']}")
        to_retranslate = f"{event['d']['author']['username']}: {event['d']['content']}"
        print(type(to_retranslate))
        op_code = event('op')
        if op_code == 11:
            print("so it begins recieved")
    except:
        sleep(time_to_sleep_when_captcha)
        time_to_sleep_when_captcha += 1


    return to_retranslate

#WORK WITH DATABASE

#messages1 = Messages(config.MESSAGES)
#datasheet = messages1.exection()




def messagebotTG(to_retranslate):
    
    #sending(datasheet)
    print(botTG.export_session_string())
    botTG.send_message(config.GROUP_TO_TOKEN, to_retranslate)




async def main():
    await botTG.start()
    
    await botTG.send_message(config.GROUP_TO_TOKEN, to_retranslate)
    await botTG.stop()
    

if __name__=="__main__":
    retranslate()
    botTG.run(main())

    



