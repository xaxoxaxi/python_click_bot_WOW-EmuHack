import ctypes
import time
from keyboard_dict import VK_CODE

'''We've imported the keyboard code to safe space from keyboard_dict'''
alphabet = VK_CODE

#Examples:
#key 'numpad_4' is pvp_port
#key 'numpad_5' is underground_port
#key 'c' is to release spirit

user32 = ctypes.windll.user32

def spam_release_spirit(alphabet_key):
	user32.keybd_event(alphabet[alphabet_key], 0,0,0)
	time.sleep(.02)
	user32.keybd_event(alphabet[alphabet_key], 0,2,0)

def strafe_left(alphabet_key):
	'''
	Jump after porting !!!
	'''
	user32.keybd_event(alphabet[alphabet_key], 0,0,0)
	time.sleep(.05)
	user32.keybd_event(alphabet[alphabet_key], 0,2,0)
	
def strafe_right(alphabet_key):
	'''
	Jump after porting !!!
	'''
	user32.keybd_event(alphabet[alphabet_key], 0,0,0)
	time.sleep(.05)
	user32.keybd_event(alphabet[alphabet_key], 0,2,0)	
	
time.sleep(2) #Default sleep time before the script starts working!

#spam_release_spirit('c')

while True:
	spam_release_spirit('w')
	time.sleep(10)