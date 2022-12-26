import websocket
import json
import threading
import time
import config


def send_json_request(ws, request):
	ws.send(json.dumps(request))


def recieve_json_response(ws):
	response = ws.recv()
	if response:
		return json.loads(response)


def heartbeat(interval, ws):
	print('so it begins')
	while True:
		time.sleep(interval)
		heartbeat.JSON = {
		"op": 1,
		"d": "null"
		}

		send_json_request(ws, heartbeatJSON)
		print("so it sent")


ws = websocket.WebSocket()
ws.connect('wss://gateway.discord.gg/?v=&&encoding=json')
event = recieve_json_response(ws)

heartbeat_interval = event['d']['heartbeat_interval'] / 1000
threading.start_new_thread(heartbeat, (heartbeat_interval, ws))
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


while True:
	event = recieve_json_response(ws)

	try:
		print(f"{event['d']['author']['username']}: {event['d']['content']}")
		op_code = event('op')
		if op_code == 11:
			print("so it begins recieved")
	except:
		pass