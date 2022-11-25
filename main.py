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
	#print(" " * 5, "\033[s\b", "Choose the next block to place", end="\033[u\033[B") is another way of doing it with cursor save position reset position
	print(" " * 5, "Choose the next block to place", end=f"\033[{len('Choose the next block to place')}D\033[B")

	#print the three randomly chosen blocks (should their scale be changed? cuz there is one block in the diamond map that looks like really big)

	counter = 0
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
		
		#be carefull even or odd number of len of block[0]and behaviour of //
		counter += 1
		print(' ' * ((len(block[0]))//2), counter, end=f"\033[{(len(block[0])+2)//2 +1}D")

		print(f"\033[{len(block) + 2}A\033[{len(block[0])+2}C", end='     ')

	print("\033[100B\033[100D", end='') #put the cursor to the bottom of the terminal


block_list = [ [[2, 0], [2, 0], [2, 2]], [[0, 2], [0, 2], [2, 2]], [[0, 2, 0], [0, 2, 0], [0, 2, 0]]]
map = read_grid("diamond.txt")
prompt = ">>> "
block_selected = False #boolean representing whether a block is selected or not
game = True #boolean representing whether the game is ongoing or not

while game:
	random_blocks = [block_list[0], block_list[1], block_list[2]]
	print_grid(map)
	print_blocks(random_blocks)

	#Get user input
	print("\033[2K", end='')
	user_input = input(prompt)
	print("\033[T", end='') #Scrolls up a line, eliminating the newline created by input
	if prompt != ">>> ":
		prompt = ">>> "

	#Use user input
		#We first check if the user entered a command
		#Otherwise we check if he entered coordinates
		#Otherwise we check if the user enter a number
		#it's maybe better to put this whole thing in a function
	if user_input == "Stop playing":
		game = False
	elif user_input == "pause":
		prompt = "Game paused (type 'resume' to continue) >>> "
		#put the game on pause
	elif user_input == "save":
		pass
		#save the current state of the game in a file
	elif user_input == "unselect":
		block_selected = False
	elif block_selected == True:
		#check if the input can be converted to coordinates i, j, that is the input is of the form "i, j"
		#if it can check if the coordinates are valid
		#if it can't prompt user to enter a valid command or coordinates or unselect
		"""
		if valid_position(user_input):
			pass
			#place block at coordinates
			block_selected = False
		else:
			prompt = "Enter valid coordinates or 'unselect' to unselect block >>> "
		#The coordinates are invalid as long as for one cell, the sum of the block cell and the map cell is not equal to 3.
		#if yes, place block
		"""
	else:
		try:
			user_input = int(user_input)
		except ValueError:
			prompt = "Enter the number of a block or a valid command >>> "
		else:
			if user_input > 0 and user_input <= len(random_blocks):
				block_selected = True
				prompt = "Enter the coordinates to place the block >>> "
			else:
				prompt = "Enter a valid block number >>> "

	print(f"\033[{len(map) + 2}A", end="") #put the cursor back to the top left corner of screen (where we start drawing the map)

print("\033[100B")