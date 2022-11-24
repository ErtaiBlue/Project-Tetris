from time import sleep

def read_grid(path):
	""" Returns a map matrix of integers representing the content of the cell. The map file has return characters at the end of each line,
	so i take each line without the last character (line[:len(line)-1]). This is why i added a return at the end of the diamond.txt file.
	Otherwise, the last number will not be added."""
	
	with open(path, 'r') as file:
		map = [[int(x) for x in line[:len(line)-1].split(' ')] for line in file.readlines()]
		return map

def print_grid(map):
	#print the map
	print('-' * (len(map[0]) + 2) )
	for line in map:
		print('|', end= '')
		for cell in line:
			if cell == 0:
				print(' ', end='')
			elif cell == 1:
				print('•', end='')
			else:
				print('▩', end='')
		print('|')
	print('-' * (len(map[0]) + 2))
	print(f"\033[{len(map)+2}A", f"\033[{len(map[0]) + 2}C", end='') #Move the cursor up len(map+2) lines, that it to the original position from which we start drawing the map.

def print_blocks(blocks):
	print(" " * 5, "Choose the next block to place", end=f"\033[{len('Choose the next block to place')}D\033[B")
	#print the three randomly chosen blocks (should their scale be changed? cuz there is one block in the diamond map that looks like really big)

	for block in blocks:
		print('-' * (len(block[0])+2), end=f"\033[{len(block[0])+2}D\033[B")
		
		for line in block:
			print('|', end='')
			for cell in line:
				if cell == 0:
					print(' ', end='')
				elif cell == 1:
					print('•', end='')
				else:
					print('▩', end='')
			print('|', end=f"\033[{len(line)+2}D\033[B")

		print('-' * (len(block[0])+2), end=f"\033[{len(block[0])+2}D\033[B")		

		print(f"\033[{len(block[0]) + 3}A\033[{len(block[0])+2}C", end='     ')

	print(f"\033[80B") #put the cursor to the bottom of the terminal


block_list = [ [[2, 0], [2, 0], [2, 2]], [[0, 2], [0, 2], [2, 2]]]
map = read_grid("diamond.txt")
game = True #boolean representing if the game is ongoing or not

while game:
	blocks = [block_list[0], block_list[1]]
	print_grid(map)
	print_blocks(blocks)

	#The coordinates are invalid as long as for one cell, the sum of the block cell and the map cell is not equal to 3.



	game = False