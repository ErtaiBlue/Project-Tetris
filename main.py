from time import sleep
import random
import sys
import os



def homescreen():
	"""Displays the homescreen and presents a choice to the user.
	He can type 1 to start the game immediately, 2 to restore a saved game and 3 to display the rules.
	Returns 'path', string representing the path to the file of the game to restore.
	If the user did not choose to restore a game from a save, path is equal to False.
	"""

	start = False

	while start == False:
		path = False
		print("\033[100D\033[100A", end='') #Position the cursor in top left corner of screen
		print("\033[2J", end='') #Clear the screen
		print(" __        __   _                            _          ____       _____    _        _     _\n\
 \\ \\      / /__| | ___ ___  _ __ ___   ___  | |_ ___   |  _ \\ _   |_   _|__| |_ _ __(_)___| |\n\
  \\ \\ /\\ / / _ \\ |/ __/ _ \\| '_ ` _ \\ / _ \\ | __/ _ \\  | |_) | | | || |/ _ \\ __| '__| / __| |\n\
   \\ V  V /  __/ | (_| (_) | | | | | |  __/ | || (_) | |  __/| |_| || |  __/ |_| |  | \\__ \\_|\n\
    \\_/\\_/ \\___|_|\\___\\___/|_| |_| |_|\\___|  \\__\\___/  |_|    \\__, ||_|\\___|\\__|_|  |_|___(_)\n\
                                                              |___/\n\n\n")
		user_input = input("Press 1 to start playing, 2 to play from a saved game and 3 to display the rules >>> ")
		while not(user_input == "1" or user_input == "2" or user_input == "3"):
			print("\033[100D\033[A\033[2K", end='') #Goes up a line and clears the line
			user_input = input("Press 1 to start playing, 2 to play from a saved game and 3 to display the rules >>> ")
		
		if user_input == "1":
			start = True
		elif user_input == "2": #Ask for the path to the file of the game to restore
			print("\033[100D\033[100A", end='') #Position the cursor in top left corner of screen
			print("\033[2J", end='') #Clear the screen
			print("  ____           _                                                 __\n\
 |  _ \\ ___  ___| |_ ___  _ __ ___    __ _  __ _ _ __ ___   ___   / _|_ __ ___  _ __ ___    ___  __ ___   _____ \n\
 | |_) / _ \\/ __| __/ _ \\| '__/ _ \\  / _` |/ _` | '_ ` _ \\ / _ \\ | |_| '__/ _ \\| '_ ` _ \\  / __|/ _` \\ \\ / / _ \\\n\
 |  _ <  __/\\__ \\ || (_) | | |  __/ | (_| | (_| | | | | | |  __/ |  _| | | (_) | | | | | | \\__ \\ (_| |\\ V /  __/\n\
 |_| \\_\\___||___/\\__\\___/|_|  \\___|  \\__, |\\__,_|_| |_| |_|\\___| |_| |_|  \\___/|_| |_| |_| |___/\\__,_| \\_/ \\___|\n\
                                     |___/\n\n\n")
			path = input("Enter the name of the file containing the saved game or 'q' to go back to homescreen >>> ")
			while not(path == "q") and (len(path)<8 or not((path in os.listdir() and path[-8:] == "save.txt"))): #We secure the input by checking if the end of the input is 'save.txt' as all saves are named this way.
				print("\033[100D\033[A\033[2K", end='') #Goes up a line and clears the line
				path = input("Enter the name of the file containing the saved game or 'q' to go back to homescreen >>> ")
			if path != "q":
				start = True
		else: #display the rules
			print("\033[100D\033[100A", end='') #Position the cursor in top left corner of screen
			print("\033[2J", end='') #Clear the screen

			print(" ____        _\n\
|  _ \\ _   _| | ___  ___ \n\
| |_) | | | | |/ _ \\/ __|\n\
|  _ <| |_| | |  __/\\__ \\\n\
|_| \\_\\__,__|_|\\___||___/\n\n\n")
			print("PyTetris is a game where you have to place blocks to compleat rows and columns.")
			print("There are different boards with different shapes. You can choose the size and shape of the board, \
then you can choose between two policies: either you can choose from all available blocks, \
either you can choose from a set of three randomly chosen blocks.")
			print("If you choose the first policie, you can naviguate between all the available blocks \
by pressing 'l' to go to the next page of blocks or 'h' to go to the previous page of blocks.")
			print("To place a block, you must first select it by typing in it's number.")
			print("You can then rotate the block using 'l' for clockwise and 'h' for counterclockwise.")
			print("Once the block is in the correct rotation, place it by typing the coordinates \
where the bottom left cell of the block will be placed: type in the letter of the columns then \
the letter of the row separated by a comma like so: 'a,B'")
			print("If you chose a big size for the grid such that there are more rows or columns than letters in the alphabet, \
to place a block on column 27 and row 1 for example type: 'aa,A'")
			print("Don't place a block on an already occupied cell or outside the board! You would loose a life if you do so. \
The game ends when you loose your three lives.")
			print("Every time you clear a row or column, your score will be incremented by the amount of blocks cleared.")
			print("You can save a game state by typing 'save'. Then, if you want to come back to this game state, quit the game, relaunch it \
and choose '2' in the homescreen. Then type in the name of the file containing the save.")
			print("Have fun!. Once you have finished, you can exit by typing: 'q'")

			user_input = input("Press 'q' to go back to the homescreen >>> ")
			while user_input != "q":
				print("\033[100D\033[A\033[2K", end='') #Goes up a line and clears the line
				user_input = input("Press 'q' to go back to the homescreen >>> ")

	print("\033[100D\033[100A", end='') #Position the cursor in top left corner of screen
	print("\033[2J", end='') #Clear the screen
	return path

def menu():
	"""
	Displays a menu where the user is prompted to setup their game.
	Returns shape, size, policie.
	shape a string representing the shape of the grid, either diamond, circle or triangle.
	size and int representing the width of the grid.
	policie a string, "1" for access to all blocks, "2" for randomly chosen blocks.
	"""

	print("\033[2J", end='') #Clear the screen
	print("  ____       _\n\
 / ___|  ___| |_ _   _ _ __\n\
 \\___ \\ / _ \\ __| | | | '_ \\ \n\
  ___) |  __/ |_| |_| | |_) |\n\
 |____/ \\___|\\__|\\__,_| .__/ \n\
                      |_|\n\n\n")

	shape = input("Choose the shape of the grid. Enter 'diamond', 'circle' or 'triangle' to choose between the diamond, circle and triangle grid >>> ")
	while not(shape == "diamond" or shape == "circle" or shape == "triangle"):
		print("\033[100D\033[A\033[2K", end='') #Goes up a line and clears the line
		shape = input("Choose the shape of the grid. Enter 'diamond', 'circle' or 'triangle' to choose between the diamond, circle and triangle grid >>> ")

	size = input("Choose the width of the grid. The width must be an odd number so as to preserve the symetry of the grids >>> ")
	try:
		size = int(size)
	except ValueError:
		pass
	while type(size) == str or size < 1 or size%2 == 0:
		print("\033[100D\033[A\033[2K", end='') #Goes up a line and clears the line
		size = input("Choose the width of the grid. The width must be an odd number so as to preserve the symetry of the grids >>> ")
		try:
			size = int(size)
		except ValueError:
			pass

	policie = input("Choose whether you have access to all blocks in the game each turn or only a set of randomly selected blocks.\nEnter '1' to have access to all blocks, '2' for randomly chosen blocks >>> ")
	while not(policie == "1" or policie == "2"):
		print("\033[100D\033[A\033[2K", end='') #Goes up a line and clears the line
		print("\033[A\033[2K", end='')
		policie = input("Choose whether you have access to all blocks in the game each turn or only a set of randomly selected blocks.\nEnter '1' to have access to all blocks, '2' for randomly chosen blocks >>> ")

	print("\033[100D\033[100A", end='') #Position the cursor in top left corner of screen
	return shape, size, policie

def generate_grid(shape, size):
	"""
	Generates a grid of given shape and size
	Returns grid a 2D matrix.
	"""

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
	"""
	Reads the first four lines of a save file.
	In the first line is written the shape of the grid.
	In the second line is written the random blocks that were available to the user. This line is empty if the policie was "1", that is the user had access to all blocks
	In the third line is written the score
	In the fourth line is written the lives
	All the lines end with a \n, this is why we don't take the last character of a line [:len(lines[0])-1])
	Returns shape a string, random_blocks a list (empty if the second line was empty), score an int and lives an int.
	"""

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
	"""
	Reads all the lines of a save file starting from the 5th line. This is were the grid matrix is written.
	All the lines end with a \n, this is why we don't take the last character of a line: line[:len(line)-1]
	Returns grid a 2D matrix.
	"""
	
	with open(path, 'r') as file:
		grid = [[int(x) for x in line[:len(line)-1].split(' ')] for line in file.readlines()[4:]]
	return grid

def save_game_info(path, shape, random_blocks, score, lives):
	"""
	Writes the game information in the file specified by path.
	In the first line is written the shape of the grid.
	In the second line is written the random blocks that were available to the user. This line is empty if the policie was "1", that is the user had access to all blocks
	The block matrixes are written like so: values of cells are separated by a comma, lines are separated by : the blocks are separated by ;
	In the third line is written the score
	In the fourth line is written the lives
	"""

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
	"""
	Writes the grid at the end of the file specified by path.
	Values are separated by a space. Each row of the grid is written on a line.
	"""

	with open(path, 'a') as file:
		for line in grid:
			for i in range(len(line)):
				file.write(str(line[i]))
				if i != len(line)-1:
					file.write(" ")
			file.write("\n")

def print_grid(grid):
	"""
	Displays the grid on the screen.
	Once done, positions the cursor at the top left of the screen
	"""

	print('   ', end='')
	for i in range(len(grid[0])):
		print("abcdefghijklmnopqrstuvwxyz"[i%26] + ' ', end='')
	print("\n", end='')

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
	"""
	Displays the score and the lives on the screen.
	Once done, positions the cursor 3 lines below the score
	"""

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
	print(f"\033[{9+len(str(score))+2+5+9+3+2}D\033[3B", end='') #reposition the cursor 3 lines below the score

def print_blocks(blocks, page, NB_BLOCKS_PER_PAGE, selected_block):
	"""
	Displays the blocks that the user can choose from. The parameter blocks contains a list of all blocks to be displayed
	The parameters page and NB_BLOCKS_PER_PAGE are used to write the correct number underneath each block.
	The blocks are displayed in lines of 5 blocks
	The selected block is displayed in red
	Once done, cursor is reset to the top left corner of the screen
	"""

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

		if i%5 == 0: #The 5 is the number of blocks per line
			print("\0337", end='') #saves cursor position (might not work on terminals other than xterm)

		#be carefull even or odd number of len of block[0]and behaviour of //
		print(' ' * ((len(blocks[i][0]))//2), i+1+(page-1)*NB_BLOCKS_PER_PAGE, end=f"\033[{(len(blocks[i][0])+2)//2 +1}D")

		if (i+1)%5 == 0: #The 5 is the number of blocks per line
			print("\0338\033[3B", end='') #Restores cursor position (might not work on terminals other than xterm) and moves it three lines down.
		else:
			print(f"\033[{len(blocks[i]) + 2}A\033[{len(blocks[i][0])+2}C", end='     ')

	print("\033[100D\033[100A", end='') #Position the cursor in top left corner of screen

def rotate(block, dir):
	"""
	Returns a matrix which corresponds to the block passed in parameter rotated clockwise if dir == True and counterclockwise if dir == False
	"""
	
	rotated_block = []
	
	if dir == True:
		for i in range(len(block[0])):
			rotated_block.append([block[j][i] for j in range(len(block)-1, -1, -1)])
	else:
		for i in range(len(block[0])-1, -1, -1):
			rotated_block.append([line[i] for line in block])

	return rotated_block

def is_input_coordinates(user_input, gridwidth, gridheight):
	"""
	Checks if the string user_input is of the format of coordinates that is [letter corresponding to column],[letter corresponding to row]
	Returns True if yes, False if no.
	"""

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

def convert_input_coordinates(user_input, gridheight, gridwidth):
	"""
	Converts the string user_input to two integer coordinates i, j the indexes of the row and column corresponding to the letters the user entered
	We have to keep in mind that the user first enters the letter of the column, then the letter of the row.
	"""

	input = user_input.split(',')
	if len(input[1]) == 1:
		i = "ABCDEFGHIJKLMNOPQRSTUVWXYZ".index(input[1])
	else:
		i = "ABCDEFGHIJKLMNOPQRSTUVWXYZ".index(input[1][0]) + gridheight//27*26
	if len(input[0]) == 1:
		j = "abcdefghijklmnopqrstuvwxyz".index(input[0])
	else:
		j = "abcdefghijklmnopqrstuvwxyz".index(input[0][0]) + gridwidth//27*26
	return i, j


def valid_position(grid, block, i, j):
	"""
	Checks if the coordinates i,j are a valid position to place the block passed in parameter.
	We have to check that the block would not be placed out of bounds or placed on top of an invalid cell or already occupied cell.
	Returns True if the coordinates i,j are a valid position for the block, False if not.
	"""

	for a in range(len(block)):
		for b in range(len(block[0])):
			if block[a][b] == 2:
				if (i-(len(block)-a-1) < 0 or j+b > len(grid[0])-1): #This means the block would be placed out of bounds
					return False
				if grid[i-(len(block)-a-1)][j+b] == 0 or grid[i-(len(block) -a -1)][j+b] + block[a][b] == 4: #This means the block would be placed on an invalid cell or an already occupied cell
					return False
	return True

def emplace_block(grid, block, i, j):
	"""
	Modifies the grid to place the block at the coordinates i,j
	"""

	for a in range(len(block)):
		for b in range(len(block[0])):
			if block[a][b] == 2:
				grid[i-(len(block) -a -1)][j+b] = block[a][b]


def row_flash(grid, i, first_square_of_line, last_square_of_line):
	"""
	Makes the blocks in the row i flash starting from the first_square_line and ending a last_square_of_line
	To make the row flash, we display the row a few times switching from inverted colors to normal colors with a little delay.
	Once done, the cursor is reset to the top left corner of the screen
	"""

	print(f"\033[{2+i}B\033[{3+first_square_of_line*2}C", end='') #position the cursor at first_square_of_line
	for h in range(4): #4 is the number of times the row will flash. It has to be even or else the terminal would stay in inverse video mode.
		if h%2 == 0:
			print("\033[7m", end='') #Makes the terminal go in reverse video mode, everything printed in this mode has its colors inverted.
		else:
			print("\033[0m", end='') #Resets the terminal mode to normal
		for j in range(first_square_of_line, last_square_of_line+1):
			print('▩', end="\033[C")
		print(f"\033[{(last_square_of_line+1-first_square_of_line)*2}D", end='')
		sys.stdout.flush()
		sleep(0.5)
	print("\033[100D\033[100A", end='') #Position the cursor in top left corner of screen

def col_flash(grid, j):
	"""
	Makes the blocks in the column j flash.
	To make the row flash, we display the column a few times switching from inverted colors to normal colors with a little delay.
	Once done, the cursor is reset to the top left corner of the screen
	"""

	print(f"\033[2B\033[{3+j*2}C", end='')
	for h in range(4): #4 is the number of times the column will flash. It has to be even or else the terminal would stay in inverse video mode.
		if h%2 == 0:
			print("\033[7m", end='') #Makes the terminal go in reverse video mode, everything printed in this mode has its colors inverted.
		else:
			print("\033[0m", end='') #Resets the terminal mode to normal

		for i in range(len(grid)):
			if grid[i][j] == 2:
				print('▩', end='')
				print("\033[D\033[B", end='')
			else:
				print("\033[B", end='')
		sys.stdout.flush()
		sleep(0.5)
		print(f"\033[{len(grid)}A", end='')

	print("\033[100D\033[100A", end='')

def row_state(grid, i):
	"""
	Checks if the row i is full and needs to be cleared.
	Returns True if the row is full, False if not.
	"""

	for cell in grid[i]:
		if cell == 1:
			return False
	return True

def col_state(grid, j):
	"""
	Checks if the column j is full and needs to be cleared.
	Returns True if the column is full, False if not.
	"""

	for line in grid:
		if line[j] == 1:
			return False
	return True

def row_clear(grid, i):
	"""
	Modifies the grid to clear the row i.
	The row to be cleared is first flashed, then the row is cleared, 
	then we make the blocks on top of the cleared blocks fall down and we refresh the display so the user can see the blocks fell.
	Returns the number of cleared blocks. This is needed to increment the score accordingly.
	"""

	#find what is the index of the first square of the line and the last square of the line. This is needed to flash the right blocks, and make the correct blocks fall down
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

	return nb_cleared_blocks


def col_clear(grid, j):
	"""
	Modifies the grid to clear the column j.
	The column to be cleared is first flashed, then the column is cleared.
	Returns the number of cleared blocks. This is needed to increment the score accordingly.
	"""

	nb_cleared_blocks = 0
	col_flash(grid, j)

	for line in grid:
		if line[j] == 2:
			line[j] = 1
			nb_cleared_blocks += 1
	return nb_cleared_blocks


def reset_full_lines_columns(grid, score):
	"""
	Resets all full lines and columns in the grid and returns the new score.
	"""

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
		print(f"\033[{len(grid[0])*2 + 4}C", end='') #Move the cursor to where the score should start being displayed
		print_score_lives(score, lives)
		print_blocks(available_blocks[(page-1)*NB_BLOCKS_PER_PAGE:page*NB_BLOCKS_PER_PAGE], page, NB_BLOCKS_PER_PAGE, selected_block)

		if lives == 0:
			game = False
			break

		#Get user input
		print("\033[100B\033[A", end='') #position the cursor at the line above the bottom line of the terminal
		user_input = input(prompt)
		if prompt != ">>> ":
			prompt = ">>> "
		print("\033[100D\033[100A", end='') #reset the position of the cursor to the top left of the terminal


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
				i, j = convert_input_coordinates(user_input, len(grid), len(grid[0]))

				if valid_position(grid, available_blocks[selected_block], i, j):
					emplace_block(grid, available_blocks[selected_block], i, j)
					#refresh the display of the grid so that the user can see the blocks he placed appear
					print_grid(grid)
					sys.stdout.flush()
					score = reset_full_lines_columns(grid, score)
					#if the game mode is random blocks, replace the block the user just placed with a new randomly chosen block
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