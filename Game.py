import time
import os
import pynput
import random

def draw():
	for y in range(15):
		result = ' '
		for x in range(30):
			char = ' '
			for item in snake:
				if item['x'] == x and item['y'] == y:
					char = 'i'
			if x == food['x'] and y == food['y']:
				char = 'F'
			result += char
		print(result)

def press_instruction(key):
    global direction
    if key == pynput.keyboard.KeyCode.from_char('w'):
        direction = 1
    if key == pynput.keyboard.KeyCode.from_char('s'):
        direction = 2
    if key == pynput.keyboard.KeyCode.from_char('d'):
        direction = 3
    if key == pynput.keyboard.KeyCode.from_char('a'):
        direction = 4
    
def realase_instruction(key):
    print('Realease', key)
    
pynput.keyboard.Listener(
    on_press = press_instruction,
    on_release = realase_instruction
).start()


while True:
	os.system('cls')
	move()
	draw()
	time.sleep(0.3)
