#loads the content of the diamond.txt map into the diamond_map matrix. The diamon.txt file has return characters at the end of each line,
#so i take each line without the last character (line[:len(line)-1]). This is why i added a return at the end of the diamond.txt file.
#Otherwise, the last number will not be added in the diamond_map.

with open("diamond.txt", 'r') as file:
	diamond_map = [[int(x) for x in line[:len(line)-1].split(' ')] for line in file.readlines()]