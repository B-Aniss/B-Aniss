from websocket import create_connection
import json

socket = create_connection("wss://socket.streamable.com/")
socket.send(json.dumps({"type": "handshake"}))
handshake_response = json.loads(socket.recv())

session_key = handshake_response['payload']['session']


print("[+] Handshake Success")
amount = int(input("[?] View amount: ").strip())
shortcode = input("[?] Shortcode: ").strip()

for i in range(amount):
    socket.send(json.dumps({
        "type":"play",
        "progress":"0.00",
        "shortcode":shortcode,
        "loops":0,
        "timestamp":1708897483,
        "id":session_key,
        "referrer":""
    }))
