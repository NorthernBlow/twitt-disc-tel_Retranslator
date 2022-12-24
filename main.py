import discord
import config
from discord.ext import commands
from pyrogram import Client, filters
import sqlite3
from time import sleep
import asyncio




intents = discord.Intents.all();
botDS = commands.Bot(intents=intents, command_prefix='>')
botTG = Client("bot", api_id=config.API_ID, api_hash=config.API_HASH,
    bot_token=config.TOKENTG)


datsheet = ''


with botTG:
    print(botTG.export_session_string())
    botTG.send_message(config.GROUP_TO_TOKEN, datasheet)
def funcfunc():
    
    print("Вы находитесь здесь1")
    #res = messages1.exection(message.text)
        #print(res)
        #print(botTG.export_session_string())
    #print(repos)
    print(config.GROUP_TO_TOKEN)
    return botTG.send_message(config.GROUP_TO_TOKEN, 'fuck')



author = ''
repos = ''
datsheet = ''

#DATABASE CONNECTION, CREATE, EXECUTE, UPDATE AND CLOSE  \\\\\\\\\\\\//////////

class Messages:
    def __init__(self, database):
        self.connection = sqlite3.connect(database, check_same_thread=False)
        self.cursor = self.connection.cursor()
        with self.connection:
            self.cursor.execute(
                "CREATE TABLE IF NOT EXISTS messages(target INTEGER, source INTEGER, message INTEGER, text VARCHAR(4096));")

    def exists(self, target, source, message: int):
        with self.connection:
            result = self.cursor.execute("SELECT * FROM messages WHERE target=? AND source=? AND message=?;",
                                         (target, source, message)).fetchall()
            print(result)
            return bool(len(result))

    def exection(self):
        with self.connection:
            datasheet = self.cursor.execute("SELECT * FROM messages WHERE message=1;")
            print(datsheet)
            return datsheet



    def add(self, message: int, text: str):
        with self.connection:
            return self.cursor.execute("INSERT INTO messages VALUES (?, ?, ?, ?);", (None, None, message, text))

    def close(self):
        self.connection.close()


messages1 = Messages(config.MESSAGES)





@botDS.event
async def on_message(message):
    author = message.author.name
    try:
        repos = message.content #+ ' ' +message.attachments[0].url
    except:
        repos = message.content
    print(repos)
    database = open(r'./dot.txt', 'r+')
    
    database.write(repos)
    
    tmp = database.read()
    database.close()


    # store message in the database
    #messages1.add(1, message.content)
    #messages1.close()
    



def handler():
    #database = database.readline()
    #print(database)
    print("Вы находитесь здесь1")
    if messages1.exists(message.id, message.text):
        print("Вы находитесь здесь")
        botTG.send_message(config.GROUP_TO_TOKEN, message.id, message.text)
        print(message.author.name, message.content)
        r = 'fuck'



def main():
    botDS.run(config.TOKENDS)
    botTG.run()


asyncio.run(main())

