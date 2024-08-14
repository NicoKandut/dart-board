from utility_stuff.hardware import *
from utility_stuff.gpio import *

### GLOBALS
o_player: Shifter= None
o_score: Shifter = None
o_remain: Shifter = None

def init(config: dict):
    conf_gpios = config['GPIOS']

    setGPIOModeToBoard()    
    o_player     = Shifter(conf_gpios['PLAYER_DATA_OUT']   , conf_gpios['CLOCK'], conf_gpios['CLEAR_DATA'])
    o_score      = Shifter(conf_gpios['SCORE_DATA_OUT']    , conf_gpios['CLOCK'], conf_gpios['CLEAR_DATA'])
    o_remain     = Shifter(conf_gpios['REMAINDER_DATA_OUT'], conf_gpios['CLOCK'], conf_gpios['CLEAR_DATA'])
    

def main(config: dict, data: dict):
    init(config)

    while True:
        break
    pass