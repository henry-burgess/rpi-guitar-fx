import RPi.GPIO as GPIO
from pynput.keyboard import Key, Controller

PRESET_UP = 8
PRESET_DOWN = 10

def change_preset(channel):
    if channel == PRESET_UP:
        keyboard.press(Key.ctrl)
        keyboard.press('+')
        keyboard.release('+')
        keyboard.release(Key.ctrl)
        print("Next preset activated.")
    elif channel == PRESET_DOWN:
        keyboard.press(Key.ctrl)
        keyboard.press('-')
        keyboard.release('-')
        keyboard.release(Key.ctrl)
        print("Previous preset activated.")
    
# Setup keyboard.
keyboard = Controller()

# Setup GPIO.
GPIO.setwarnings(False)
GPIO.setmode(GPIO.BOARD)
GPIO.setup(PRESET_UP, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
GPIO.add_event_detect(PRESET_UP,GPIO.RISING,callback=change_preset)
GPIO.setup(PRESET_DOWN, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
GPIO.add_event_detect(PRESET_DOWN,GPIO.RISING,callback=change_preset)

message = input("Running preset switcher... Press ENTER to quit.\n\n")

GPIO.cleanup()