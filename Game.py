import time
import os
import pynput
import random

snake = [
	{'x': 2, 'y':1}, 
	{'x': 3, 'y':1}, 
	{'x': 4, 'y':1},
	{'x': 4, 'y':2}
]

food = {'x':10, 'y': 2}

direction = 2

def move():
	new_head = snake[-1].copy()
	if direction == 1:
		new_head['y'] -= 1
	if direction == 2:
		new_head['y'] += 1
	if direction == 3:
		new_head['x'] += 1
	if direction == 4:
		new_head['x'] -= 1

	if new_head['x'] < 0 or new_head['x'] > 29 or new_head['y'] < 0	or new_head['y'] > 14:
		exit("Game over")

	for item in snake:
		if new_head['x'] == item['x'] and new_head['y'] == item['y']:
			exit("Game over")
		
	if new_head['x'] == food['x'] and new_head['y'] == food['y']:
		generate_food()
	else:
		snake.pop(0)

	snake.append(new_head)

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
