import argparse
from api.service import main as api_routine
from dummy_detection.service import main as dummy_det_routine
from utility_stuff.config_parsing import parseConfigFile
from multiprocessing import Process, Array

det_proc = None
api_proc = None

### MAIN -----------------------------------------------------------------
if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--dummy",action="store_true" )
    args = parser.parse_args()

    config = parseConfigFile()

    # initialise shared memory
    shm = Array('i', (0,0,0,0))


    # create Processes
    api_proc = Process(target=api_routine, args=(shm,))
    if args.dummy:
        det_proc = Process(target=dummy_det_routine, args=(shm, config['PHOTO']['PHOTO_RESOLUTION']))
    else:
        det_proc = None # here we call the real detection routine
        pass

    # start sub-processes
    det_proc.start()
    api_proc.start()
    

    # wait till detection is closed and then kill all other sub-processes
    det_proc.join()
    api_proc.terminate()
    

    
    
