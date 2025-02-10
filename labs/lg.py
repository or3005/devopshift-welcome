import logging
import json
import os
import sys

class JasonFormatter(logging.Formatter):
    def format(self, record: logging.LogRecord)->str:
        log={"time":record.created,"module":record.module}
        return json.dumps(log)


handler=logging.StreamHandler(sys.stdout)
logger=logging.getLogger("orloger")
logger.addHandler(handler)
handler.setFormatter(JasonFormatter)


# logging.Handler
# logging.Formatter


log_level=os.environ.get("Log_level","DEBUG")
log_format="%(asctime)s - %(name)s - %(levelname)s- %(message)s"
logging.basicConfig(filename="orloger",level=log_level,format=log_format)
   

logger.info("This is info")
logger.debug("this is debug")
logger.error("this is error")
logger.warning("this is warning")
#json.dumps(logger)





