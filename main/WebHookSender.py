

from pathlib import Path
from datetime import datetime
import os
import http.client
import json
import socket


index = []
module = ["webhook.py", "user.py", "install.bat"]
local_ip = socket.gethostbyname(socket.gethostname())
content = Path('example.txt').read_text()

    

client = http.client.HTTPSConnection(url)
name = Path('WebHookName').read_text()
text = Path('Content').read_text()
url = "discord.com"
id = Path('WebhookLink').read_text()
headers = {
    "Content-Type": "application/json"
}

data = {
    "content": text,
    "username": name
}



json_data = json.dumps(data)
client.request("POST", id, body=json_data, headers=headers)
response = client.getresponse()
client.close()

print("[GATEWAY] Opened Request")
print("[GATEWAY] Sent Id")
print("[WEBHOOK] Checking files...")
print("[GATEWAY] Closed Gateway")

