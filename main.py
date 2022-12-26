import discord
import config
from discord.ext import commands
from pyrogram import Client, filters
import sqlite3
from time import sleep
import asyncio
import requests
import json
import threading
import parser


intents = discord.Intents.all();
#botDS = commands.Bot(intents=intents, command_prefix='!')
botTG = Client("bot", api_id=config.API_ID, api_hash=config.API_HASH,
    bot_token=config.TOKENTG)


#DATA STRUCTURE

datasheet = ''
author = ''
repos = ''
#locker = threading.Lock()

print(repos)


#DATABASE CONNECTION, CREATE, EXECUTE, UPDATE AND CLOSE  \\\\\\\\\\\\//////////
# Должна быть создана база данных для каждого пользователя,

class Userspace:
    def __init__(self, database):
        self.connection = sqlite3.connect(database)
        self.cursor = self.connection.cursor()
        with self.connection:
            self.cursor.execute("CREATE TABLE IF NOT EXISTS User(ID INTEGER, PRIMARY KEY, user_id INTEGER, subscribes INTEGER)")


class Subscribes:
    def __init__(self, database):
        self.connection = sqlite3.connect(database)
        self.curos = self.connection.cursor()
        with self.connection:
            self.cursor.execute("CREATE TABLE IF NOT EXISTS Subscribes(ID INTEGER, PRIMARY KEY, source_id INTEGER)")




class Messages:
    def __init__(self, database):
        self.connection = sqlite3.connect(database, check_same_thread=False)
        self.cursor = self.connection.cursor()
        with self.connection:
            self.cursor.execute(
                "CREATE TABLE IF NOT EXISTS messages(target INTEGER, source INTEGER, message INTEGER, text TEXT);")

    def exists(self, target, source, message: int):
        with self.connection:
            result = self.cursor.execute("SELECT * FROM messages WHERE target=? AND source=? AND message=?;",
                                         (target, source, message)).fetchall()
            print(result)
            return bool(len(result))

    def exection(self):
        with self.connection:
            datasheet = self.cursor.execute('SELECT text FROM messages').fetchall()
            #print(datasheet)
            return datasheet

    def add(self, message: int, text: str):
        with self.connection:
            return self.cursor.execute("INSERT INTO messages VALUES (?, ?, ?, ?);", (None, None, message, text))
            commit()

    def close(self):
        self.connection.close()




#WORK WITH DATABASE

messages1 = Messages(config.MESSAGES)
datasheet = messages1.exection()



# def sending(datasheet):
#     global msg
#     for index, tup in enumerate(datasheet):
#         print(tup)
#         msg = tup[-1]
#         "".join(map(str, msg))
#         print(type(msg))
#         return msg



# @botDS.event
# async def on_message(message):
#     global repos
#     author = message.author.name
#     try:
#         locker.acquire()
#         repos = message.content + ' ' +message.attachments[0].url
#         time.sleep(1)
#     except:
#         repos = message.content
#     # store message in the database
#     messages1.add(1, message.content)
#     print(repos)
#     #messages1.close()
#     return repos
    


def messagebotTG(to_retranslate):
    
    #sending(datasheet)
    print(botTG.export_session_string())
    #print(repos)
    #print(type(repos))
    botTG.send_message(config.GROUP_TO_TOKEN, to_retranslate)



# def send_messageTG(msg, data, func):
#     sending(datasheet)
#     bot = config.TOKENTG
#     conf = config.GROUP_TO_TOKEN
#     text = msg
#     url = f"https://api.telegram.org/bot{bot}/sendMessage"
#     response = requests.post(url, json={'chat_id': conf, 'text': msg})  
#     print(response.text)
#     return response.json()



def main():
    #sending(datasheet)
    botDS.run(config.TOKENDS)
    parser.retranslate()
    botTG.run()
    messagebotTG(to_retranslate)
    print(to_retranslate)
    botTG.send_message(config.GROUP_TO_TOKEN, to_retranslate)
    


main()

