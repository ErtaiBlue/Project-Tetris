from time import sleep
import sys

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

def print_score_lives(score, lives):
	#print the score
	print(" " * 5, end='')
	print("#" * (9+len(str(score))+2), end=f"\033[{9+len(str(score))+2}D\033[B")
	print("# Score: ", score, " #", sep='', end=f"\033[{9+len(str(score))+2}D\033[B")
	print("#" * (9+len(str(score))+2),sep='', end='\033[2A')

	#print the lives
	print(" " * 5, end='')
	print("#" * (9+3+2), end=f"\033[{9+3+2}D\033[B")
	print("# Lives: ", "❤"*lives, " "*(3-lives), " #", sep='', end=f"\033[{9+3+2}D\033[B")
	print("#" * (9+3+2), end='')
	print(f"\033[{9+len(str(score))+2+5+9+3+2}D\033[3B", end='') #reposition the cursor

def print_blocks(blocks):
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


def row_flash(grid, i, first_square_of_line, last_square_of_line):
	print(f"\033[{2+len(map)-i}A\033[{2+first_square_of_line}C", end='')
	for h in range(4):
		if h%2 == 0:
			print("\033[7m", end='')
		else:
			print("\033[0m", end='')
		for j in range(first_square_of_line, last_square_of_line+1):
			if grid[i][j] == 0:
				print(' ', end='')
			elif grid[i][j] == 1:
				print('•', end='')
			else:
				print('▩', end='')
		print(f"\033[{last_square_of_line-first_square_of_line}D", end='')
		sleep(0.3)
	print("\033[100D\033[100B", end='')

def col_flash(grid, j):
	pass

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
	nb_cleared_blocks = 0
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

	row_flash(grid, i, first_square_of_line, last_square_of_line)
	for j in range(first_square_of_line, last_square_of_line+1):
		grid[i][j] = 1
	nb_cleared_blocks += last_square_of_line+1 - first_square_of_line

	#make the blocks on top fall down
	for a in range(i, 0, -1):
		for b in range(first_square_of_line, last_square_of_line+1):
			if grid[a-1][b] == 1 or grid[a-1][b] == 2:
				grid[a][b] = grid[a-1][b]
			elif grid[a][b] != 0:
				grid[a][b] = 1
	for b in range(first_square_of_line, last_square_of_line+1):
		if grid[0][b] == 2:
			grid[0][b] = 1

	return nb_cleared_blocks


def col_clear(grid, j):
	nb_cleared_blocks = 0
	for line in grid:
		if line[j] == 2:
			line[j] = 1
			nb_cleared_blocks += 1
	return nb_cleared_blocks


def reset_full_lines_columns(grid, score):
	for i in range(len(grid)-1, -1, -1):
		while row_state(grid, i):
			score += row_clear(grid, i)
	for j in range(len(grid[0])):
		if col_state(grid, j):
			score += col_clear(grid, j)
	return score



block_list = [ [[2, 0], [2, 0], [2, 2]], [[0, 2], [0, 2], [2, 2]], [[0, 2, 0], [0, 2, 0], [0, 2, 0]], [[2]]]
map = read_grid("diamond.txt")
prompt = ">>> "
selected_block = None #variable containing the index of the block selected by the user out of the reandom_blocks list
score = 0
lives = 3
game = True #boolean representing whether the game is ongoing or not

while game:
	print("\033[0J", end='') #Clear the screen
	random_blocks = [block_list[0], block_list[1], block_list[2], block_list[3]]
	print_grid(map)
	print_score_lives(score, lives)
	print_blocks(random_blocks)

	if lives == 0:
		game = False
		break

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
	if user_input == "q":
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
				score = reset_full_lines_columns(map, score)
				selected_block = None
			else:
				prompt = "Invalid position to place the block! You loose a life >>> "
				lives -= 1
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

	print(f"\033[{len(map) + 3}A", end='') #put the cursor back to the top left corner of screen (where we start drawing the map)

print("\033[100B")