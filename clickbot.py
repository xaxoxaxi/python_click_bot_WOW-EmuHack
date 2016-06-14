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

def jump_after_port(alphabet_key):
	'''
	Jump after porting !!!
	'''
	user32.keybd_event(alphabet[alphabet_key], 0,0,0)
	time.sleep(.05)
	user32.keybd_event(alphabet[alphabet_key], 0,2,0)

def turn_arround_a(alphabet_key):
	'''
	Constant pressed button:
	-when the value is (... 0,0,0) the button is constantly pressed
	-respectively with value (... 0,2,0) button is realeased
	'''
	user32.keybd_event(alphabet[alphabet_key], 0,0,0)

def release_spirit(alphabet_key):
	'''
	Press key to release spirit
	'''
	for i in range(3):
		user32.keybd_event(alphabet[alphabet_key], 0,0,0)
		time.sleep(.05)
		user32.keybd_event(alphabet[alphabet_key], 0,2,0)

def pvp_port(alphabet_key):
	'''
	Port to player's location
	'''
	user32.keybd_event(alphabet[alphabet_key], 0,0,0)
	time.sleep(.05)
	user32.keybd_event(alphabet[alphabet_key], 0,2,0)

def sit_down(alphabet_key):
	'''
	spams sit down button to ensure at least 1 critical hit
	'''
	for i in range(2):
		user32.keybd_event(alphabet[alphabet_key], 0,0,0)
		time.sleep(.02)
		user32.keybd_event(alphabet[alphabet_key], 0,2,0)
	
def underground_port(alphabet_key):
	'''
	port underground to fall and muerta
	'''
	user32.keybd_event(alphabet[alphabet_key], 0,0,0)
	time.sleep(.05)
	user32.keybd_event(alphabet[alphabet_key], 0,2,0)
	
def spam_release_spirit(alphabet_key):
	user32.keybd_event(alphabet[alphabet_key], 0,0,0)
time.sleep(2) #Default sleep time before the script starts working!

#spam_release_spirit('c')
while True:
	time.sleep(0.35)
	pvp_port('numpad_4')
	time.sleep(0.5)
	jump_after_port('a')
	sit_down('x')
	#turn_arround_a('d')
	time.sleep(1.5)  # set delay time to kill
	#release_spirit('c')
	time.sleep(0.35)
	underground_port('numpad_5')
	#time.sleep(0.5)
	jump_after_port('a')
	time.sleep(1)
