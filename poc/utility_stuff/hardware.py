import gpio
import threading
import RPi.GPIO as GPIO
import time

# This Class is stolen from "https://www.instructables.com/Using-a-shift-register-with-Raspberry-Pi/" ;)
class Shifter():
    def __init__(self, data_port: str, clock_port: str, clear_port: str):
        self.data_port =  int(data_port)
        self.clock_port = int(clock_port)
        self.clear_port = int(clear_port)
        self._setup()
          
    def tick(self):
        gpio.high(self.clock_port)
        gpio.low(self.clock_port)	

    def setValue(self,value):
        #TODO: Shifter.setValue()
        self.tick()

    def clear(self):
        gpio.low(self.clear_port)
        self.tick()
        gpio.heigh(self.clear_port)

    def _setup(self) -> None:
        GPIO.setup(self.port, GPIO.OUT)


#-----------------------------------
#
# status: 0-off, 1-blinking , 2-on 
#
#-----------------------------------
class Led:
    def __init__(self, port: str):
        self.port = int(port)
        self.status = 0
        self.blink_thread: threading.Thread = None
        self.thread_event: threading.Event = threading.Event()
        
        self._setup()

    def on(self) -> None:
        self._stop_blinking_thread()
        gpio.high(self.port)

    def blink(self, rate: float) -> None:
        if self.blink_thread is not None:
            return
        self.blink_thread = threading.Thread(target=gpio.pulsing, args=(self.port, rate, self.thread_event))

    def off(self) -> None:
        self._stop_blinking_thread()
        gpio.low(self.port)

    def _stop_blinking_thread(self) -> None:
        if self.blink_thread is not None:
            self.thread_event.set()
            self.blink_thread.join()
            self.thread_event.clear()
            self.blink_thread = None

    def _setup(self):
        GPIO.setup(self.port, GPIO.OUT)