from time import sleep
import random
import sys
import os



def homescreen():
	start = False

	while start == False:
		path = False
		print("\033[100D\033[100A", end='') #Position the cursor in top left corner of screen
		print("\033[2J", end='') #Clear the screen
		print("_|_|_|              _|_|_|_|_|            _|                _|\n\
_|    _|  _|    _|      _|      _|_|    _|_|_|_|  _|  _|_|        _|_|_|\n\
_|_|_|    _|    _|      _|    _|_|_|_|    _|      _|_|      _|  _|_|\n\
_|        _|    _|      _|    _|          _|      _|        _|      _|_|\n\
_|          _|_|_|      _|      _|_|_|      _|_|  _|        _|  _|_|_|\n\
                _|\n\
            _|_|\n\n\n")
		user_input = input("Press 1 to start playing, 2 to play from a saved game and 3 to display the rules")
		while not(user_input == "1" or user_input == "2" or user_input == "3"):
			user_input = input("Press 1 to start playing, 2 to play from a saved game and 3 to display the rules")
		
		if user_input == "1":
			start = True
		elif user_input == "2": #Ask for the path to the file of the game to restore
			print("\033[100D\033[100A", end='') #Position the cursor in top left corner of screen
			print("\033[2J", end='') #Clear the screen
			path = input("Enter the name of the file containing the saved game or 'q' to go back to homescreen")
			while not(path == "q") and (len(path)<8 or not((path in os.listdir() and path[-8:] == "save.txt"))):
				path = input("Enter the name of the file containing the saved game or 'q' to go back to homescreen")
			if path != "q":
				start = True
		else: #display the rules
			print("\033[100D\033[100A", end='') #Position the cursor in top left corner of screen
			print("\033[2J", end='') #Clear the screen

			print("PyTetris is a game where you have to place blocks to compleat rows and columns.")
			print("There are different boards with different shapes. You can choose the size and shape of the board, \
		then you can choose between two policies: either you can choose from all available blocks, \
		either you can choose from a set of three randomly chosen blocks")
			print("To place a block, you must select it by typing in it's number, \
		then typing the coordinates where the bottom left cell of the block will be placed")
			print("Don't place a block on an already occupied cell or outside the board! You would loose a life if you do so.\
		The game ends when you loose your three lives.")
			print("Every time you clear a row or column, your score will be incremented by the amount of blocks cleared.")
			print("Have fun!")

			user_input = input("Press 'q' to go back to the homescreen")
			while user_input != "q":
				user_input = input("Press 'q' to go back to the homescreen")

	print("\033[100D\033[100A", end='') #Position the cursor in top left corner of screen
	print("\033[2J", end='') #Clear the screen
	return path

def menu():
	print("\033[2J", end='')

	shape = input("Choose the shape of the grid. Enter 'diamond', 'circle' or 'triangle' to choose between the diamond, circle and triangle grid")
	while not(shape == "diamond" or shape == "circle" or shape == "triangle"):
		shape = input("Choose the shape of the grid. Enter 'diamond', 'circle' or 'triangle' to choose between the diamond, circle and triangle grid")

	size = 0
	while type(size) == str or size < 1 or size%2 == 0:
		size = input("Choose the width of the grid. The width must be an odd number so as to preserve the symetry of the grids")
		try:
			size = int(size)
		except ValueError:
			print("The width is a number")

	policie = input("Choose whether you have access to all blocks in the game each turn or only a set of randomly selected blocks. Enter '1' to have access to all blocks, '2' for randomly chosen blocks")
	while not(policie == "1" or policie == "2"):
		policie = input("Choose whether you have access to all blocks in the game each turn or only a set of randomly selected blocks. Enter '1' to have access to all blocks, '2' for randomly chosen blocks")

	print("\033[100D\033[100A", end='') #Position the cursor in top left corner of screen
	return shape, size, policie

def generate_grid(shape, size):
	if shape == "diamond":
		grid = [[] for x in range(size)]
		for i in range(0, size//2):
			for j in range(0, (size-i*2)//2):
				grid[i].append(0)
			for j in range(0, 1+i*2):
				grid[i].append(1)
			for j in range(0, (size-i*2)//2):
				grid[i].append(0)
		for i in range(0, size//2+1):
			for j in range(0, i):
				grid[size//2+i].append(0)
			for j in range(0, size-i*2):
				grid[size//2+i].append(1)
			for j in range(0, i):
				grid[size//2+i].append(0)
		return grid

	elif shape == "triangle":
		grid = [[] for x in range((size+1)//2)]
		for i in range(0, (size+1)//2):
			for j in range(0, (size-1)//2-i):
				grid[i].append(0)
			for j in range(0, 1+i*2):
				grid[i].append(1)
			for j in range(0, (size-1)//2-i):
				grid[i].append(0)
		return grid

	else:
		if size == 1:
			grid = [[1]]
		elif size == 3:
			grid = [[0,1,0], [1,1,1], [0,1,0]]
		elif size == 5:
			grid = [[0,1,1,1,0], [1,1,1,1,1], [1,1,1,1,1], [1,1,1,1,1], [0,1,1,1,0]]
		elif size == 7:
			grid = [[0,0,1,1,1,0,0], [0,1,1,1,1,1,0], [1,1,1,1,1,1,1], [1,1,1,1,1,1,1], [1,1,1,1,1,1,1], [0,1,1,1,1,1,0], [0,0,1,1,1,0,0]]
		else:
			grid = [[] for x in range(size)]
			grid[0] = [0,0,0] + [1 for x in range(size-6)] + [0,0,0]
			grid[1] = [0,0] + [1 for x in range(size-4)] + [0,0]
			grid[2] = [0] + [1 for x in range(size-2)] + [0]
			for i in range(3, size-3):
				grid[i] = [1 for x in range(size)]
			grid[size-3] = [0] + [1 for x in range(size-2)] + [0]
			grid[size-2] = [0,0] + [1 for x in range(size-4)] + [0,0]
			grid[size-1] = [0,0,0] + [1 for x in range(size-6)] + [0,0,0]

		return grid

def read_game_info(path):
	with open(path, 'r') as file:
		lines = file.readlines()
		shape = lines[0][:len(lines[0])-1]
		if lines[1] == "\n":
			random_blocks = []
		else:
			random_blocks = [ [[int(cell) for cell in line.split(',')] for line in block.split(':')] for block in lines[1][:len(lines[1])-1].split(';')]
		score = int(lines[2][:len(lines[2])-1])
		lives = int(lines[3][:len(lines[3])-1])
	return shape, random_blocks, score, lives

def read_grid(path):
	""" Returns a grid matrix of integers representing the content of the cell. The grid file has return characters at the end of each line,
	so i take each line without the last character (line[:len(line)-1])."""
	
	with open(path, 'r') as file:
		grid = [[int(x) for x in line[:len(line)-1].split(' ')] for line in file.readlines()[4:]]
	return grid

def save_game_info(path, shape, random_blocks, score, lives):
	with open(path, 'w') as file:
		file.write(shape + "\n")
		for i in range(len(random_blocks)):
			for j in range(len(random_blocks[i])):
				for h in range(len(random_blocks[i][j])):
					file.write(str(random_blocks[i][j][h]))
					if h != len(random_blocks[i][j])-1:
						file.write(",")
				if j != len(random_blocks[i])-1:
					file.write(":")
			if i != len(random_blocks)-1:
				file.write(";")
		file.write("\n")

		file.write(str(score) + "\n")
		file.write(str(lives) + "\n")

def save_grid(path, grid):
	with open(path, 'a') as file:
		for line in grid:
			for i in range(len(line)):
				file.write(str(line[i]))
				if i != len(line)-1:
					file.write(" ")
			file.write("\n")

def print_grid(grid):
	print('   ', end='')
	for i in range(len(grid[0])):
		print("abcdefghijklmnopqrstuvwxyz"[i%26] + ' ', end='')
	print("\n", end='')

	#print the grid
	print(' ', end='')
	for i in range(len(grid[0]) + 2):
		print('- ', end='')
	print("\n", end='')

	for row in range(len(grid)):
		print("ABCDEFGHIJKLMNOPQRSTUVWXYZ"[row%26], end='')
		print('| ', end= '')
		for cell in grid[row]:
			if cell == 0:
				print('  ', end='')
			elif cell == 1:
				print('• ', end='')
			else:
				print('▩ ', end='')
		print('|')

	print(' ', end='')
	for i in range(len(grid[0]) + 2):
		print('- ', end='')
	print("\n", end='')

	print("\033[100D\033[100A", end='') #Position the cursor in top left corner of screen

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

def print_blocks(blocks, page, NB_BLOCKS_PER_PAGE, selected_block):
	#print the blocks to be chosen from

	for i in range(len(blocks)):
		if selected_block != None and i+1+(page-1)*NB_BLOCKS_PER_PAGE == selected_block+1:
			print("\033[38;2;250;48;48m", end='')
		print('-' * (len(blocks[i][0])+2), end=f"\033[{len(blocks[i][0])+2}D\033[B")
		
		for line in blocks[i]:
			if selected_block != None and i+1+(page-1)*NB_BLOCKS_PER_PAGE == selected_block+1:
				print("\033[38;2;250;48;48m", end='')
			print('|', end='')
			print("\033[38;2;255;255;255m", end='')
			for cell in line:
				if cell == 0:
					print(' ', end='')
				else:
					print('▩', end='')
			if selected_block != None and i+1+(page-1)*NB_BLOCKS_PER_PAGE == selected_block+1:
				print("\033[38;2;250;48;48m", end='')
			print('|', end=f"\033[{len(line)+2}D\033[B")

		print('-' * (len(blocks[i][0])+2), end=f"\033[{len(blocks[i][0])+2}D\033[B")		
		print("\033[38;2;255;255;255m", end='')

		if i%5 == 0:
			print("\0337", end='') #saves cursor position (might not work on terminals other than xterm)

		#be carefull even or odd number of len of block[0]and behaviour of //
		print(' ' * ((len(blocks[i][0]))//2), i+1+(page-1)*NB_BLOCKS_PER_PAGE, end=f"\033[{(len(blocks[i][0])+2)//2 +1}D")

		if (i+1)%5 == 0:
			print("\0338\033[3B", end='') #Restores cursor position and moves it three lines down.
		else:
			print(f"\033[{len(blocks[i]) + 2}A\033[{len(blocks[i][0])+2}C", end='     ')

	print("\033[100D\033[100A", end='') #Position the cursor in top left corner of screen

def rotate(block, dir):
    #clockwise if dir = True
    rotated_block = []

    if dir == True:
        for i in range(len(block[0])):
            rotated_block.append([block[j][i] for j in range(len(block)-1, -1, -1)])
    else:
        for i in range(len(block[0])-1, -1, -1):
            rotated_block.append([line[i] for line in block])

    return rotated_block

def is_input_coordinates(user_input, gridwidth, gridheight):
	input = user_input.split(',')
	columns = "abcdefghijklmnopqrstuvwxyz"
	rows = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
	if len(input) != 2:
		return False

	if not(input[0] == input[0][0]*len(input[0])): #check if the first part of the input is constituted of the same character
		return False
	if not(input[0][0] in columns[:gridwidth]) or (len(input[0])>1 and not(input[0][0] in columns[:gridwidth%26])): #check if input is on the board
		return False

	if not(input[1] == input[1][0]*len(input[1])): #check if the second part of the input is constituted of the same character
		return False
	if not(input[1][0] in rows[:gridheight]) or (len(input[1])>1 and not(input[1][0] in rows[:gridheight%26])): #check if input is on the board
		return False

	return True

def convert_input_coordinates(user_input):
	input = user_input.split(',')
	if len(input[1]) == 1:
		i = "ABCDEFGHIJKLMNOPQRSTUVWXYZ".index(input[1])
	else:
		i = "ABCDEFGHIJKLMNOPQRSTUVWXYZ".index(input[1][0]) + len(grid)//27*26
	if len(input[0]) == 1:
		j = "abcdefghijklmnopqrstuvwxyz".index(input[0])
	else:
		j = "abcdefghijklmnopqrstuvwxyz".index(input[0][0]) + len(grid[0])//27*26
	return i, j


def valid_position(grid, block, i, j):
	for a in range(len(block)):
		for b in range(len(block[0])):
			if block[a][b] == 2:
				if (i-(len(block)-a-1) < 0 or j+b > len(grid[0])-1): #This means the block would be placed out of bounds
					return False
				if grid[i-(len(block)-a-1)][j+b] == 0 or grid[i-(len(block) -a -1)][j+b] + block[a][b] == 4: #This means the block would be placed on an invalid cell or an already occupied cell
					return False
	return True

def emplace_block(grid, block, i, j):
	for a in range(len(block)):
		for b in range(len(block[0])):
			if block[a][b] == 2:
				grid[i-(len(block) -a -1)][j+b] = block[a][b]


def row_flash(grid, i, first_square_of_line, last_square_of_line):
	print(f"\033[{1+len(grid)-i}A\033[{3+first_square_of_line*2}C", end='')
	for h in range(4): #4 is the number of times the row will flash.
		if h%2 == 0:
			print("\033[7m", end='')
		else:
			print("\033[0m", end='')
		for j in range(first_square_of_line, last_square_of_line+1):
			print('▩', end="\033[C")
		print(f"\033[{(last_square_of_line+1-first_square_of_line)*2}D", end='')
		sys.stdout.flush()
		sleep(0.5)
	print("\033[100D\033[100A", end='') #Position the cursor in top left corner of screen

def col_flash(grid, j):
	print(f"\033[{1+len(grid)}A\033[{3+j*2}C", end='')
	for h in range(4): #4 is the number of times the column will flash
		if h%2 == 0:
			print("\033[7m", end='')
		else:
			print("\033[0m", end='')

		for i in range(len(grid)):
			if grid[i][j] == 2:
				print('▩', end='')
				print("\033[D\033[B", end='')
			else:
				print("\033[B", end='')
		sys.stdout.flush()
		sleep(0.5)
		print(f"\033[{len(grid)}A", end='')
	print("\033[100D\033[100B", end='')

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

	#refresh the display of the grid so that it shows that the blocks have fallen
	print_grid(grid)
	sys.stdout.flush()
	print(f"\033[{len(grid) + 3}B", end='')

	return nb_cleared_blocks


def col_clear(grid, j):
	nb_cleared_blocks = 0
	col_flash(grid, j)

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


def main():
	NB_BLOCKS_PER_PAGE = 10
	UNIVERSAL_BLOCK_LIST = [ [[0,0,0,0,0], [0,0,0,0,0], [0,0,0,0,0], [2,0,0,0,0], [2,2,0,0,0]], 
	[[0,0,0,0,0], [0,0,0,0,0], [0,0,0,0,0], [0,2,0,0,0], [2,2,0,0,0]], 
	[[0,0,0,0,0], [0,0,0,0,0], [0,0,0,0,0], [2,0,0,0,0], [2,2,2,0,0]], 
	[[0,0,0,0,0], [0,0,0,0,0], [2,2,0,0,0], [0,2,0,0,0], [0,2,0,0,0]], 
	[[0,0,0,0,0], [0,0,0,0,0], [2,0,0,0,0], [2,2,0,0,0], [2,0,0,0,0]], 
	[[0,0,0,0,0], [0,0,0,0,0], [0,0,0,0,0], [0,2,0,0,0], [2,2,2,0,0]], 
	[[0,0,0,0,0], [0,0,0,0,0], [0,0,0,0,0], [2,2,0,0,0], [0,2,2,0,0]], 
	[[0,0,0,0,0], [0,0,0,0,0], [2,0,0,0,0], [2,2,0,0,0], [0,2,0,0,0]], 
	[[0,0,0,0,0], [2,0,0,0,0], [2,0,0,0,0], [2,0,0,0,0], [2,0,0,0,0]], 
	[[0,0,0,0,0], [0,0,0,0,0], [0,0,0,0,0], [2,2,0,0,0], [2,2,0,0,0]], 
	[[0,0,0,0,0], [0,0,0,0,0], [0,0,0,0,0], [2,2,0,0,0], [0,2,0,0,0]], 
	[[0,0,0,0,0], [0,0,0,0,0], [0,0,0,0,0], [2,2,0,0,0], [2,0,0,0,0]], 
	[[0,0,0,0,0], [0,0,0,0,0], [0,0,0,0,0], [0,0,2,0,0], [2,2,2,0,0]], 
	[[0,0,0,0,0], [0,0,0,0,0], [2,0,0,0,0], [2,0,0,0,0], [2,2,0,0,0]], 
	[[0,0,0,0,0], [0,0,0,0,0], [0,2,0,0,0], [2,2,0,0,0], [0,2,0,0,0]], 
	[[0,0,0,0,0], [0,0,0,0,0], [0,0,0,0,0], [2,2,2,0,0], [0,2,0,0,0]], 
	[[0,0,0,0,0], [0,0,0,0,0], [0,0,0,0,0], [0,2,2,0,0], [2,2,0,0,0]], 
	[[0,0,0,0,0], [0,0,0,0,0], [0,2,0,0,0], [2,2,0,0,0], [2,0,0,0,0]], 
	[[0,0,0,0,0], [0,0,0,0,0], [0,0,0,0,0], [0,0,0,0,0], [2,2,2,2,0]], 
	[[0,0,0,0,0], [0,0,0,0,0], [0,0,0,0,0], [0,0,0,0,0], [2,0,0,0,0]], 
	[[0,0,0,0,0], [2,2,2,2,0], [2,2,2,2,0], [2,2,2,2,0], [2,2,2,2,0]],
	[[0,0,0,0,0], [0,2,2,0,0], [2,2,2,2,0], [2,2,2,2,0], [0,2,2,0,0]], 
	[[0,0,0,0,0], [2,0,0,2,0], [2,0,0,2,0], [2,0,0,2,0], [2,2,2,2,0]], 
	[[0,0,0,0,0], [2,2,2,2,0], [0,0,0,2,0], [0,0,0,2,0], [0,0,0,2,0]], 
	[[0,0,0,0,0], [0,0,0,0,0], [0,0,0,0,0], [2,2,2,2,0], [2,2,2,0,0]], 
	[[0,0,0,0,0], [2,2,2,0,0], [0,0,2,0,0], [0,0,2,0,0], [2,2,2,0,0]], 
	[[0,0,0,0,0], [2,2,0,0,0], [2,2,0,0,0], [2,2,0,0,0], [2,2,0,0,0]], 
	[[0,0,0,0,0], [0,0,0,0,0], [0,0,0,0,0], [2,2,2,2,0], [2,2,2,2,0]], 
	[[2,0,0,0,0], [2,0,0,0,0], [2,0,0,0,0], [2,0,0,0,0], [2,0,0,0,0]], 
	[[0,0,0,0,0], [2,2,2,2,2], [2,0,0,0,2], [0,0,0,0,0], [2,2,2,2,2]], 
	[[0,0,0,0,0], [2,0,0,0,0], [2,0,0,0,0], [2,0,0,0,2], [2,2,2,2,2]], 
	[[0,0,0,0,0], [0,0,2,2,0], [0,2,2,0,0], [2,2,0,0,0], [2,0,0,0,0]],
	[[0,0,0,0,0], [2,2,0,0,0], [0,2,2,0,0], [0,0,2,2,0], [0,0,0,2,0]], 
	[[0,0,0,0,0], [2,2,2,2,0], [0,2,2,0,0], [0,2,2,0,0], [0,2,2,0,0]], 
	[[0,0,0,0,0], [2,0,0,2,0], [0,2,2,0,0], [0,2,2,0,0], [2,0,0,2,0]], 
	[[0,0,0,0,0], [0,0,0,0,0], [2,2,2,2,2], [0,2,2,2,0], [0,0,2,0,0]], 
	[[0,0,0,0,0], [2,0,0,0,0], [2,2,0,0,0], [0,2,2,0,0], [0,0,2,2,0]], 
	[[0,0,0,0,0], [0,0,0,2,0], [0,0,2,2,0], [0,2,2,0,0], [2,2,0,0,0]], 
	[[0,0,0,0,0], [0,0,0,0,0], [0,0,0,2,0], [2,2,2,2,0], [0,0,0,2,0]], 
	[[0,0,0,0,0], [0,0,0,0,0], [0,0,0,0,0], [2,2,2,2,0], [0,0,0,2,0]], 
	[[0,0,0,0,0], [2,2,0,0,0], [0,2,0,0,0], [0,2,0,0,0], [0,2,0,0,0]], 
	[[0,0,0,0,0], [2,0,0,0,0], [2,0,0,0,0], [2,0,0,0,0], [2,2,0,0,0]], 
	[[0,0,0,0,0], [0,0,0,0,0], [2,0,0,0,0], [2,2,2,0,0], [0,0,2,0,0]], 
	[[0,0,0,0,0], [0,0,0,0,0], [2,2,0,0,0], [0,2,0,0,0], [0,2,2,2,0]], 
	[[0,0,0,0,0], [0,0,0,0,0], [0,0,2,0,0], [2,2,2,0,0], [2,0,0,0,0]], 
	[[0,0,0,0,0], [0,0,0,0,0], [0,2,2,0,0], [0,2,0,0,0], [2,2,0,0,0]], 
	[[0,0,0,0,0], [0,0,0,0,0], [0,0,2,0,0], [0,2,0,0,0], [2,0,0,0,0]], 
	[[0,0,0,0,0], [0,0,0,0,0], [2,0,0,0,0], [0,2,0,0,0], [0,0,2,0,0]], 
	[[0,0,0,0,0], [0,0,0,0,0], [2,0,0,0,0], [2,0,0,0,0], [2,0,0,0,0]], 
	[[0,0,0,0,0], [0,0,0,0,0], [0,0,0,0,0], [0,0,0,0,0], [2,2,2,0,0]], 
	[[0,0,0,0,0], [0,0,0,0,0], [0,0,0,0,0], [2,0,0,0,0], [2,0,0,0,0]], 
	[[0,0,0,0,0], [0,0,0,0,0], [0,2,0,0,0], [2,2,2,0,0], [0,2,0,0,0]], 
	[[0,0,0,0,0], [0,0,0,0,0], [0,0,0,0,0], [0,0,0,0,0], [2,2,0,0,0]] ]
	CIRCLE_BLOCK_LIST = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30]
	DIAMOND_BLOCK_LIST = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 31, 32, 33, 34, 35, 20, 36, 37, 28, 38, 39, 40, 41]
	TRIANGLE_BLOCK_LIST = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 42, 43, 44, 45, 46, 47, 48, 49, 50, 51, 52]

	prompt = ">>> "
	selected_block = None #variable containing the index of the block selected by the user out of the available_blocks list or None if no block is selected
	page = 1 #this represents the blocks to be displayed from the blocks the user can choose from
	game = True
	print("\033[?1049h", end='') #Enter alternative screen buffer (this is for instance what vim uses to create a new text editing window inside the terminal)

	path_game_to_restore = homescreen()
	if path_game_to_restore == False:
		score = 0
		lives = 3
		shape, size, policie = menu()
		grid = generate_grid(shape, size)
		if shape == "circle":
			available_blocks = [UNIVERSAL_BLOCK_LIST[x] for x in CIRCLE_BLOCK_LIST]
		elif shape == "diamond":
			available_blocks = [UNIVERSAL_BLOCK_LIST[x] for x in DIAMOND_BLOCK_LIST]
		else:
			available_blocks = [UNIVERSAL_BLOCK_LIST[x] for x in TRIANGLE_BLOCK_LIST]
		if policie == "2":
			available_blocks = random.choices(available_blocks, k=3)
	else:
		shape, random_blocks, score, lives = read_game_info(path_game_to_restore)
		grid = read_grid(path_game_to_restore)
		if random_blocks == []:
			policie = "1"
			if shape == "circle":
				available_blocks = [UNIVERSAL_BLOCK_LIST[x] for x in CIRCLE_BLOCK_LIST]
			elif shape == "diamond":
				available_blocks = [UNIVERSAL_BLOCK_LIST[x] for x in DIAMOND_BLOCK_LIST]
			else:
				available_blocks = [UNIVERSAL_BLOCK_LIST[x] for x in TRIANGLE_BLOCK_LIST]
		else:
			policie = "2"
			available_blocks = random_blocks



	while game:
		print("\033[2J", end='') #Clear the screen
		
		print_grid(grid)
		print(f"\033[{len(grid[0])*2 + 4}C", end='')
		print_score_lives(score, lives)
		print_blocks(available_blocks[(page-1)*NB_BLOCKS_PER_PAGE:page*NB_BLOCKS_PER_PAGE], page, NB_BLOCKS_PER_PAGE, selected_block)
		print(f"\033[{len(grid) + 3}B", end='') #Position the cursor at the line under the map

		if lives == 0:
			game = False
			break

		#Get user input
		user_input = input(prompt)
		if prompt != ">>> ":
			prompt = ">>> "


		if user_input == "q":
			game = False

		elif user_input == "save":
			if policie == "1":
				number_of_saves = 0
				for file in os.listdir():
					if len(file)>=8 and file[-8:] == "save.txt":
						number_of_saves += 1
				path = "#" + str(number_of_saves) + shape + "save.txt"
				save_game_info(path, shape, [], score, lives)
				save_grid(path, grid)
			else:
				number_of_saves = 0
				for file in os.listdir():
					if len(file)>=8 and file[-8:] == "save.txt":
						number_of_saves += 1
				path = "#" + str(number_of_saves) + shape + "save.txt"
				save_game_info(path, shape, available_blocks, score, lives)
				save_grid(path, grid)
			prompt = "Game saved as " + path + " >>> "

		elif user_input == "unselect":
			selected_block = None

		elif selected_block != None:
			if user_input == "l":
				available_blocks[selected_block] = rotate(available_blocks[selected_block], True)
			elif user_input == "h":
				available_blocks[selected_block] = rotate(available_blocks[selected_block], False)

			elif is_input_coordinates(user_input, len(grid[0]), len(grid)):
				#Transform the coordinates from string to numbers	
				i, j = convert_input_coordinates(user_input)

				if valid_position(grid, available_blocks[selected_block], i, j):
					emplace_block(grid, available_blocks[selected_block], i, j)
					#refresh the display of the grid so that the user can see the blocks he placed appear
					print("\033[100D\033[100A", end='')
					print_grid(grid)
					sys.stdout.flush()
					print(f"\033[{len(grid) + 3}B", end='')
					score = reset_full_lines_columns(grid, score)
					if policie == "2":
						if shape == "circle":
							available_blocks[selected_block] = random.choice([UNIVERSAL_BLOCK_LIST[x] for x in CIRCLE_BLOCK_LIST])
						elif shape == "diamond":
							available_blocks[selected_block] = random.choice([UNIVERSAL_BLOCK_LIST[x] for x in DIAMOND_BLOCK_LIST])
						else:
							available_blocks[selected_block] = random.choice([UNIVERSAL_BLOCK_LIST[x] for x in TRIANGLE_BLOCK_LIST])
					selected_block = None
				else:
					prompt = "Invalid position to place the block! You loose a life >>> "
					lives -= 1
					selected_block = None
			else:
				prompt = "Enter coordinates to place the block (or type 'unselect' to unselect the block) >>> "

		elif user_input == "h":
			if page > 1:
				page = page - 1
		elif user_input == "l":
			if page < (len(available_blocks)//NB_BLOCKS_PER_PAGE + (len(available_blocks)%NB_BLOCKS_PER_PAGE > 0)): #If the page number is inferior to the number of blocks divided by the nb of blocks per page th whole rounded up.
				page = page + 1

		else:
			try:
				user_input = int(user_input)
			except ValueError:
				prompt = "Enter the number of a block or a valid command >>> "
			else:
				if user_input > 0 and user_input <= len(available_blocks):
					selected_block = user_input-1
					prompt = "Enter the coordinates to place the block (or type 'unselect' to unselect the block) >>> "
				else:
					prompt = "Enter a valid block number >>> "



		print("\033[100D\033[100A", end='')

	print("\033[?1049l") #Quit alternative screen buffer
	print("Your final score was:", score)



if __name__ == "__main__":
	main()