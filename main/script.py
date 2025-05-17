

# https://discord.com/api/webhooks/1371537518440349766/GhFi3_FQxUqvFao2Xc6iDvXIOh9JwDShocDjJ-AH6WICe1ltvv_03YgUn2aFSCs4xf8y
# Uranium is an Open Source Webhook Sender

# Libaries
from datetime import datetime
import os
import http.client
import json
import socket


index = []
module = ["webhook.py", "user.py", "install.bat"]
local_ip = socket.gethostbyname(socket.gethostname())

  
    

client = http.client.HTTPSConnection(url)
name = 
text = 
url = 
id = 
headers = {
    "Content-Type": "application/json"
}

data = {
    "content": text",
    "username": name
}



json_data = json.dumps(data)
client.request("POST", id, body=json_data, headers=headers)
response = client.getresponse()
client.close()

os.system('info * "URANIUM is now running"')
