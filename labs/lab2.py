import httpx
import json
from pprint import pprint
#from models import ServerStatusResponse,Server,read_server_list,add_new_server
import models
from fastapi import FastAPI
 
servers=models.read_server_list()
app=FastAPI()

@app.get("/server")
def get_server(server_name:str)->models.ServerStatusResponse:
    server_status=False
    
    for server in servers:
        if server.name==server_name:
            server_status=server.online
            return models.ServerStatusResponse(server_name=server_name,server_status=server_status)
        else:
            return models.ServerStatusResponse(server_name=server_name,server_status="server not found")
        
@app.post("/server")
def create_server(server_name:str)->models.ServerStatusResponse:
    new_server=models.Server(name=server_name,online=True,cpus=7,ram=12)
    models.add_new_server(new_server)
    servers.append(new_server)
    return models.ServerStatusResponse(server_name=server_name,server_status="new server added")
        