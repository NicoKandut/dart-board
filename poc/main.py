from utility_stuff.config_parsing import parseConfigFile
from shared_memory_dict import SharedMemoryDict
import dart_detection.service as dds
#import display_infos.service as dis
import webservice.service as ws

import threading

data = {
    "score": 0,
    "remainding": 0,
    "player": 0,
    "game_state": 0,
    "last_dart_x_pos": 0,
    "last_dart_y_pos": 0 
    }

t_dart_detection: threading.Thread = None
t_display_infos: threading.Thread = None
t_webservice: threading.Thread = None


### FUNCTIONS --------------------------------------------------------------------
def init():
    # parsing config file
    config = parseConfigFile()

    global t_dart_detection 
    t_dart_detection = threading.Thread(target=dds.main, args=(config, data))
    
    global t_display_infos
    #t_display_infos = threading.Thread(target=dis.main, args=(config, data))

    global t_webservice
    t_webservice = threading.Thread(target=ws.main, args=(config, data))

    t_dart_detection.start()
    #t_display_infos.start()
    t_webservice.start()


### MAIN -----------------------------------------------------------------
if __name__ == "__main__":

    init()

    t_dart_detection.join()
    #t_display_infos.join()
    t_webservice.join()

    
    
