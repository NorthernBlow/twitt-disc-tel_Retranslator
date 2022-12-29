from pyrogram import Client, filters
import os
from datetime import datetime


config = {
    "name": "tgmrelay",
    "messages": "messages.db",
    "api_id": 2843096,
    "api_hash": "b3fe86810322a24fc277cde79cd318ca",
    "source_chat_id": -1001461338272,
    "target_chat_id": -1001597517662,
}


app = Client(config["name"], config["api_id"], config["api_hash"], system_version='Arch', no_updates=False, hide_password=True)
with app:
    print(app.export_session_string())


userdir = "users/"
directory = os.scandir(path=userdir)
users = {}
for entry in directory:
    if not entry.name.startswith('.') and entry.is_file():
        file = open(userdir + entry.name, "r")
        data = file.read().splitlines()
        users[entry.name] = list()
        file.close()
        for source in data:
            users[entry.name].append(source)



@app.on_message()
def get_post(client, message):
    groupid = message.chat.id
    print(type(message.chat.id))
    #print(groupid, 'это гроуп айди')
    to_retranslate = message.chat.title + ' -> ' + message.from_user.username + ': ' + message.text
    for cortege in users.items():
        #print(cortege, "это кортеже")
        for sources in cortege[1]:
            #print(sources)
            sources = sources.split('|')
            #print(sources[0], 'это соурсес 0')
            #print(cortege[0], 'это кортеже 0')
            print(type(sources[0]))
            if groupid == int(sources[0]):
                print("работает?")  
                if len(sources) > 2:
                    if to_retranslate.find(sources[2]) != -1:
                        # with app:
                        app.send_message(cortege[0], to_retranslate)
                else:
                    # with app:
                    app.send_message(cortege[0], to_retranslate)



    print(to_retranslate)
    #app.send_message(132669168, to_retranslate)
    


def main():
    print(datetime.today().strftime(f'%H:%M:%S | Started.'))
    app.run()




if __name__ == '__main__':
    main()
