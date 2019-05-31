import os
from terrain import Tile
from rover import Rover
from planet import Planet

def load_level(filename):
	"""
	Loads the level and returns objects of your choosing
	"""
	f = open(filename, "r")
	l = f.read().splitlines()  # get the list which contains all lines of the file
	
	pointer1 = l.index("[planet]")
	planet_name = l[pointer1 + 1].split(",")[1]  # extract information about planet
	planet_width = int(l[pointer1 + 2].split(",")[1])
	planet_height = int(l[pointer1 + 3].split(",")[1])
	num_tile = planet_width * planet_height
	planet = Planet(planet_name, planet_width, planet_height, num_tile)
	
	rover_x, rover_y = int(l[pointer1 + 4].split(",")[1]), int(l[pointer1 + 4].split(",")[2])  # extract information about rover
	rover = Rover(rover_x, rover_y, planet)
	
	pointer = l.index("[tiles]") + 1  # create tiles on planet
	tiles = []
	i = 0
	j = 0
	for x in range(num_tile):
		T = l[pointer + x].split(",")
		if len(T) <= 2:
			T.append(T[1])
		tiles.append(Tile(T[0], int(T[1]), int(T[2])))
		i += 1
		if i == planet_width:
			planet.add_tile(j,tiles)
			i = 0
			j += 1
			tiles = []
			
	return planet, rover


def check(filename):
	"""
	Check the level file whether it is in correct form.
	"""
	try:  # check whether we can open the file
		f = open(filename, "r")
	except:
		print()
		print("Level file could not be found")
		print()
		return False
	
	l = f.read().splitlines()  # get all lines in a list
	pointer1 = l.index("[planet]")
	pointer2 = l.index("[tiles]")
	if "" in l[pointer1 : pointer1 + 5]:# check whether there is exactly 4 fields 
										# specified under the planet section
		print()
		print("Unable to load level file")
		print()
		return False
	
	planet_width = int(l[2].split(",")[1])
	planet_height = int(l[3].split(",")[1])
	if planet_width < 5 or planet_height < 5:  # check width and height values 
												# are greater than or equal to 5
		print()
		print("Unable to load level file")
		print()
		return False
	
	rover_x, rover_y = int(l[4].split(",")[1]), int(l[4].split(",")[2])
	if rover_x > planet_width or rover_y > planet_height:  # The rover’s coordinates 
									# are within the bounds of the planet’s dimensions
		print()
		print("Unable to load level file")
		print()
		return False
	
	if rover_x < 0 or rover_y < 0:  # check the rover’s coordinates 
									# specified are greater than or equal to 0
		print()
		print("Unable to load level file")
		print()
		return False
	num_tile = planet_width * planet_height
	
	if "" in l[pointer2 : pointer2 + num_tile] or\
		len(l[pointer2 : pointer2 + num_tile]) != num_tile :							
		 # check whether the number of tiles matches the dimensions of the planet
		print()
		print("Unable to load level file")
		print()
		return False
	
	for x in range(num_tile):  # check highest elevation is strictly greater
								# than lowest elevation for a tile
		T = l[pointer2 + x + 1].split(",")
		if len(T) == 3:
			if int(T[1]) < int(T[2]):
				print()
				print("Unable to load level file")
				print()
				return False
	return True

