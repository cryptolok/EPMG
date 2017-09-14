#!/usr/bin/env python

try:
# Python 2
	from Tkinter import Tk as gui
except:
# Python 3
	from tkinter import Tk as gui
#TODO Android and iOS won't have copy to clipboard
from hashlib import pbkdf2_hmac as pbkdf
from base64 import b64encode
from getpass import getpass

print ('')
print ('                         _dP"9b_')
print ('                       _dP"   "9b_')
print ('                     _dP"       "9b_')
print ('                   _dP"           "9b_')
print ('       8888888888888888888     8888888888888888888')
print ('       88      _dP"     88     88     "9b_      88')
print ('       88      "9b_     88     88     _dP"      88')
print ('       88  _      9b_   88     88   _dP"     _  88')
print ('       88_d8b_     "9b_ 88     88 _dP"     _d8b_88')
print ('       88P" "9b_     "9b88     8_dP"     _dP" "988')
print ('     _d88     "9b_     "9P     9P"     _dP"     88b_')
print ('   _dP"88       "9b_                 _dP"       88"9b_')
print (' _dP"  8888888888888b               dP"88888888888  "9b_')
print ('_dP"                                                   "9b_')
print ('"9b_                                                   _dP"')
print (' "9b_  8888888888888P             9b_8888888888888  _dP"')
print ('   "9b_88       _dP"               "9b_         88_dP"')
print ('     "988     _dP"                   "9b_       88P"')
print ('       88b_ _dP"       _dP     8d_     "9b_   _d88')
print ('       88"98P"       _dP"8     889b_     "9b_dP"88')
print ('       88          _dP" 88     88 "9b_          88')
print ('       88        _dP"   88     88   "9b_        88')
print ('       88       9b_     88     88     _dP       88')
print ('       8888888888888888888     8888888888888888888')
print ('                   "9b_           _dP"')
print ('                     "9b_       _dP"')
print ('                       "9b_   _dP"')
print ('                         "9b_dP"')
print ('                            "')
print ('')
print ('	   ENTROPIC PASSWORD MANAGER GENERATOR')
print ('')

iterations=10**6
service=''
login=''
password=''
compromises=''
show='SHOW'
# needed for Android/iOS exception

try:
# P2
	service=raw_input('ENTER SERVICE/WEBSITE/APPLICATION/FILENAME (can be blank) : ')
except:
# P3
	service=input('ENTER SERVICE/WEBSITE/APPLICATION/FILENAME (can be blank) : ')
print
#TODO hardcode known password policies or/and permit choice
try:
	login=raw_input('ENTER LOGIN/ID/USERNAME/EMAIL (may be blank) : ')
except:
	login=input('ENTER LOGIN/ID/USERNAME/EMAIL (may be blank) : ')
print
password=getpass('ENTER MASTER-PASSWORD/KEY/PASSPHRASE : ')
# no prompt for master-password of course
print
if not password:
	print('!!! PASSWORD CAN BUT NOT SUPPOSE TO BE BLANK !!!')
	print
try:
	compromises=raw_input('HOW MANY TIMES WAS THE GENERATED PASSWORD COMPROMISED (blank for none) : ')
except:
	compromises=input('HOW MANY TIMES WAS THE GENERATED PASSWORD COMPROMISED (blank for none) : ')
print
if compromises:
	compromises=str(int(compromises))

print('SECURE GENERATION...')
print
try:
# P2
	hash=pbkdf('sha512', service+login, password+compromises, iterations)
	encoded=b64encode(hash)
except:
# P3
	hash=pbkdf('sha512', (service+login).encode("ascii"), (password+compromises).encode("ascii"), iterations)
	encoded=str(b64encode(hash))[2:]
password=encoded[:16]+'/0'

try:
# PC will propose to show or to copy the password
	buffer = gui()
	buffer.withdraw()
	buffer.clipboard_clear()
	buffer.clipboard_append(password)
	buffer.update()
	try:
		show=raw_input('PASSWORD COPIED TO CLIPBOARD (Ctrl+V to paste it into field form), ENTER TO CLEAN OR "SHOW" TO SEE : ')
	except:
		show=input('PASSWORD COPIED TO CLIPBOARD (Ctrl+V to paste it into field form), ENTER TO CLEAN OR "SHOW" TO SEE : ')
	print
except:
# mobiles will only prompt the password
	pass
if show == 'SHOW':
	print('PASSWORD : '+password)
	print
try:
# Windows cleaning
	buffer.clipboard_clear()
	buffer.clipboard_append('000000000000000000')
	buffer.update()
	buffer.destroy()
except:
	pass

print('CLEANED (some traces may still be in memory)')
print
