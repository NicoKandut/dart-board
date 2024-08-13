import time
#from utility_stuff.hardware import *

## GLOBALS
snap_rate = None

photo_res = None

cam1_port = None
cam2_port = None
cam3_port = None

#o_status_led: Led = None

def calibrateCams():
    #TODO: calibrateCams()
    pass


def init(config: dict):

    conf_cams = config['CAMS']
    conf_photo = config['PHOTO']
    conf_general = config['GENERAL']
    conf_gpios = config['GPIOS']

    global snap_rate
    snap_rate = float(conf_general['SNAP_RATE'])

    global photo_res
    photo_res = int(conf_photo['PHOTO_RESOLUTION'])

    global cam1_port
    cam1_port = int(conf_cams['CAM_PORT_1'])
    global cam2_port
    cam2_port = int(conf_cams['CAM_PORT_2'])
    global cam3_port
    cam3_port = int(conf_cams['CAM_PORT_3'])

    global o_status_led
    #o_status_led = Led(conf_gpios['STAUS_LED'])

def main(config: dict, data: dict):
    init(config)

    while True:
        #TODO: dart_detection main loop
        break
    pass