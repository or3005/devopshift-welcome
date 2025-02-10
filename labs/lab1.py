import logging
import json
import os
import sys

class JasonFormatter(logging.Formatter):
    def format(self, record: logging.LogRecord)->str:
        log={
            
            "timestamp":self.formatTime(record,self.datefmt),
            "level":record.levelname,
            "message":record.getMessage()}
        return json.dumps(log)


valid_servers = ["nginx", "docker", "apache", "mysql"]

LOG_FORMAT=os.environ.get("LOG_FORMAT","TEXT")

LOG_LEVEL=os.environ.get("Log_level","DEBUG")
logging.basicConfig(filename="orloger",level=logging.INFO,format="%(asctime)s - %(levelname)s - %(message)s")


logger=logging.getLogger("orloger")

logger.setLevel(LOG_LEVEL)      
handler=logging.StreamHandler(sys.stdout)
file_handler=logging.FileHandler("orlog")
#handler2=logging.StreamHandler(sys.stderr)
# logger.sethandler(handler)


class InvalidServerNameError(Exception):

    def __init__(self, *args):
         super().__init__(*args)
         logger.error("Invalid input. Please enter a number and letters.")
         ValueError()



def check_service_status(server_name):
    # try:
        
        if server_name not in valid_servers:
            print("server not recognized.")
            logger.error("server not recognized")
            raise ValueError()
        else:
            logger.info("server"+server_name +" is runnig")
            print("Server name is running.")
    # except  InvalidServerNameError :
    #      logger.error("Invalid input")
         
def user_input():   
        # Get user input
        user_input = input("Enter a server name: ").strip()
        return user_input


                  
while True:
    
    try:
        server=user_input()
        if not server or " " in server :
            raise InvalidServerNameError("Invalid server name.")
        else:
            jso_log=input("Enter json or Log:")  
            
            check_service_status(server)
            if jso_log=="json":
              handler.setFormatter(JasonFormatter())
              file_handler.setFormatter(JasonFormatter())
              break
            
    except InvalidServerNameError as err:
        logging.error(err)          
    except ValueError as e:
        logging.error(e)
        print(f"Error: {e}")
        
