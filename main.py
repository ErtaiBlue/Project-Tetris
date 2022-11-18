from time import sleep

def read_grid(path):
	""" Returns a map matrix of integers representing the content of the cell. The map file has return characters at the end of each line,
	so i take each line without the last character (line[:len(line)-1]). This is why i added a return at the end of the diamond.txt file.
	Otherwise, the last number will not be added."""
	
	with open(path, 'r') as file:
		map = [[int(x) for x in line[:len(line)-1].split(' ')] for line in file.readlines()]
		return map

def print_grid(map, blocks):
	#Maybe use escape characters to go back then print
	print('-' * (len(map[0]) + 2) )
	for line in map: #maybe use enumerate or something. Like we put each line to display on the side in a list. Keep in mind that the map could have different sizes.
		print('|', end= '')
		for cell in line:
			if cell == 0:
				print(' ', end='')
			elif cell == 1:
				print('•', end='')
			else:
				print('⬛', end='')
		print('|')
	print('-' * (len(map[0]) + 2) )

block_list = [ [[2, 0], [2, 0], [2, 2]], [[0, 2], [0, 2], [2, 2]]]
map = read_grid("diamond.txt")
game = True #boolean representing if the game is ongoing or not

while game:
	blocks = [0]
	print_grid(map, blocks)
	#also display the block
	#we represent the block as a matrix, 2 being there is a full cell, and 0 being empty.
	#to check if the coordinates are valid. Imagine we take the block and put it in the map matrix (we do this by putting the bottom left
	#cell of the block at the given coordinates).
	#The coordinates are invalid as long as for one cell, the sum of the block cell and the map cell is not equal to 3.
	coordinates = tuple(int(x) for x in input("Enter the coordinates to place the block, separated by a comma   ").split(','))
	#this is not the right way of doing this. I have to assert that the user input are of the right type and valid input.


	game = False