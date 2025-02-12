from fastapi import FastAPI
from dataclasses import dataclass
import httpx
from tools import set_logger

app=FastAPI()
valid_servers = {"nginx":True, "docker":True, "apache":True, "mysql":True}
serve=""
@dataclass
class User:
    name:str
    email:str

@app.get("/")
def hello_world():
    "this is our main function"
    return {"or,or@gmail.com"}

@app.post("/add_service")
def add_server(server_name : str)->dict:
      if server_name not in valid_servers:
        # valid_servers.add(server_name)
        valid_servers[server_name]=True
        
        return ServerStatusResponse(server_name,"created")
      else: 
            raise ValueError("server is already in the service")
    
@dataclass        
class ServerStatusResponse:
    server_name:str
    server_status:str | bool      
         
@app.get("/server")
def get_server(server_name:str):
    try:
        server_status=valid_servers[server_name]
        return {ServerStatusResponse(server_name,server_status)}
    except KeyError:
        return {ServerStatusResponse(server_name,"does not exist")}
    
        

# @app.post("/server")
# def create_server(server_name:str)->bool:
#     return True
    

@app.get("/users")
def get_users()->list[User]:
    response=httpx.get("https://jsonplacholder.typicode.com/users")
    users=response.json()
    return users


@app.post("/users")
def create_user(new_user: User)->bool:
    return True

