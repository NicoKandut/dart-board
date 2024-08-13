import RPi.GPIO as GPIO
import threading
import time

def setGPIOModeToBoard() -> None :
    GPIO.setmode(GPIO.BOARD)

def high(port: int):
    GPIO.output(port, GPIO.HIGH)

def low(port: int):
    GPIO.output(port, GPIO.LOW)

def pulsing(port: int, rate: float, stop_event: threading.Event):
    while not stop_event.is_set():
        high(port)
        time.sleep(rate)
        low(port)
        time.sleep(rate)
