from time import sleep

def read_grid(path):
	""" Returns a map matrix of integers representing the content of the cell. The map file has return characters at the end of each line,
	so i take each line without the last character (line[:len(line)-1]). This is why i added a return at the end of the diamond.txt file.
	Otherwise, the last number will not be added."""
	
	with open(path, 'r') as file:
		map = [[int(x) for x in line[:len(line)-1].split(' ')] for line in file.readlines()]
		return map

def print_grid(map):
	print('  ', "abcdefghijklmnopqrstuvwxyz"[:len(map[0])], ' ', sep='')
	#print the map
	print(' ', '-' * (len(map[0]) + 2), sep='')
	for row in range(len(map)):
		print("ABCDEFGHIJKLMNOPQRSTUVXYZ"[row], end='')
		print('|', end= '')
		for cell in map[row]:
			if cell == 0:
				print(' ', end='')
			elif cell == 1:
				print('•', end='')
			else:
				print('▩', end='')
		print('|')
	print(' ', '-' * (len(map[0]) + 2), sep='')

	print(f"\033[{len(map)+3}A", f"\033[{len(map[0]) + 3}C", end='') #Move the cursor to the original position from which we start drawing the map.


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

def is_input_coordinates(user_input, mapwidth, mapheight):
	input = user_input.split(',')
	columns = "abcdefghijklmnopqrstuvwxyz"
	rows = "ABCDEFGHIJKLMNOPQRSTUVXYZ"
	if len(input) != 2 or not(input[0] in columns[:mapwidth]) or not(input[1] in rows[:mapheight]):
		return False
	else:
		return True

def valid_position(grid, block, i, j):
	for a in range(len(block)):
		for b in range(len(block[0])):
			if block[a][b] == 2 and (i-(len(block) -a -1) < 0 or j+b > len(grid[0])-1): #this means the block would be placed out of bounds
				return False
			if ( grid[i-(len(block) -a -1)][j+b] == 0 and block[a][b] == 2 ) or grid[i-(len(block) -a -1)][j+b] + block[a][b] == 4: #This means the block would be placed on an invalid square or an already filled square
				return False
	return True

def emplace_block(grid, block, i, j):
	for a in range(len(block)):
		for b in range(len(block[0])):
			if block[a][b] == 2:
				grid[i-(len(block) -a -1)][j+b] = block[a][b]
			else:
				grid[i-(len(block) -a -1)][j+b] = grid[i-(len(block) -a -1)][j+b] + block[a][b]


def row_state(grid, i):
	for cell in grid[i]:
		if cell == 1:
			return False
	return True

def col_state(grid, j):
	for line in grid:
		if line[j] == 1:
			return False
	return True

def row_clear(grid, i):
	previous_cell = None
	first_square_of_line = None
	last_square_of_line = None
	for j in range(len(grid[i])):
		if grid[i][j] == 2 and first_square_of_line == None:
			first_square_of_line = j
		else:
			if previous_cell == 2:
				last_square_of_line = j-1
		previous_cell = grid[i][j]

	for j in range(first_square_of_line, last_square_of_line+1):
		grid[i][j] = 1


def col_clear(grid, j):
	pass

def reset_full_lines_columns(grid):
	for i in range(len(grid)-1, 0, -1):
		while row_state(grid, i):
			row_clear(grid, i)
	for j in range(len(grid[0])):
		if col_state(grid, j):
			col_clear(grid, j)



block_list = [ [[2, 0], [2, 0], [2, 2]], [[0, 2], [0, 2], [2, 2]], [[0, 2, 0], [0, 2, 0], [0, 2, 0]]]
map = read_grid("diamond.txt")
prompt = ">>> "
selected_block = None #variable containing the index of the block selected by the user out of the reandom_blocks list
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
		selected_block = None
	elif selected_block != None:
		if is_input_coordinates(user_input, len(map[0]), len(map)):
			#Transform the coordinates from string to numbers	
			coordinates = user_input.split(',')
			coordinates[0], coordinates[1] = "ABCDEFGHIJKLMNOPQRSTUVXYZ".index(coordinates[1]), "abcdefghijklmnopqrstuvwxyz".index(coordinates[0])

			if valid_position(map, random_blocks[selected_block], coordinates[0], coordinates[1]):
				emplace_block(map, random_blocks[selected_block], coordinates[0], coordinates[1])
				reset_full_lines_columns(map)
				selected_block = None
			else:
				prompt = "Invalid position to place the block! You loose a life >>> "
				selected_block = None
		else:
			prompt = "Hello, i am annoying"
			#prompt = "Enter coordinates to place the block (or type 'unselect' to unselect the block) >>> "
	else:
		try:
			user_input = int(user_input)
		except ValueError:
			prompt = "Enter the number of a block or a valid command >>> "
		else:
			if user_input > 0 and user_input <= len(random_blocks):
				selected_block = user_input-1
				prompt = "Enter the coordinates to place the block (or type 'unselect' to unselect the block) >>> "
			else:
				prompt = "Enter a valid block number >>> "

	print(f"\033[{len(map) + 3}A", end="") #put the cursor back to the top left corner of screen (where we start drawing the map)

print("\033[100B")