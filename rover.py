class Rover:

	
	"""
	This is the core class which contains a lot of useful
	fuctions. In game menu, all fuctions can be found here.
	"""
	def __init__(self, x, y , planet):
		"""
		Initialises the rover.
		A rover has a coordinate x, y.
		And I give a rover a planet object, which can be used
		as the 'map' of the planet.
		"""
		self.x = x
		self.y = y
		self.planet = planet
		self.battery = 100
		

	def spherical(self, x, y):
		"""
		To make the planet be a spherical planet, I use this
		fuction to make each coordinate can be an exact point
		on the initial map.
		"""
		while x >= self.planet.width or x < 0 or y >= self.planet.height or y < 0:
			#change x if x is out of boundary
			if x >= self.planet.width:
				x -= (self.planet.width)
			elif x < 0:
				x += (self.planet.width)
			#change y if y is out of boundary
			if y >= self.planet.height:
				y -= (self.planet.height)
			elif y < 0:
				y += (self.planet.height)
		return x, y


	def can_move(self, next_x, next_y):
		"""
		Check whether the rover can move to next tile.
		Use a very easy way to check:
		If next tile's elevation is "+" or "-", then the rover
		can not get there.
		Other wise, the rover can get there, no matter the elevation
		is " " or "/" or "\".
		"""
		if self.battery == 0:
			if self.planet.tiles[next_y][next_x].is_shaded():
				return False
		if self.planet.tiles[next_y][next_x].elevation(self) == "+":
			return False
		if self.planet.tiles[next_y][next_x].elevation(self) == "-":
			return False
		return True


	def move(self, direction, cycles):
		"""
		Move the rover on the planet.
		Get the unit vector which point to the direction
		of your way. Use a loop to move step by step. Before
		move, check whether the rover can get there, if it can
		get there, change the coordinate of the rover.
		Example: if you want to move "E" direction, then
		'(1,0)' is your unit vector. You can add the rover's
		coordinate by this vector, which can only change your
		x number and keep the initial y number. And move the rover
		step by step.
		"""
		self.planet.tiles[self.y][self.x].set_occupant()  # set occupant to the initial tile
		if direction == "N":  # unit vector (0, -1)
			y_symbol = -1
			x_symbol = 0
		if direction == "S":  # unit vector (0, 1)
			y_symbol = 1
			x_symbol = 0
		if direction == "W":  # unit vector (-1, 0)
			x_symbol = -1
			y_symbol = 0
		if direction == "E":  # unit vector (1, 0)
			x_symbol = 1
			y_symbol = 0
		i = 0
		while i < int(cycles):
			next_x = self.x + x_symbol  # change x coordinate
			next_y = self.y + y_symbol  # change y coordinate
			next_x, next_y = self.spherical(next_x, next_y)  # get the next tile's coordinate
			if self.can_move(next_x, next_y):  # check whether rover can move
				#reduce battery
				if self.planet.tiles[next_y][next_x].is_shaded():
					self.battery -= 1
				self.x = next_x
				self.y = next_y
				tile = self.planet.tiles[next_y][next_x]
				tile.set_occupant()
				i += 1
			else:
				break


	def scan(self, type):
		"""
		Name each tile like this:
		|t00|t01|t02|t03|t04|
		|t10|t11|t12|t13|t14|
		|t20|t21| H |t23|t24|
		|t30|t31|t32|t33|t34|
		|t40|t41|t42|t43|t44|
		"""
		self.planet.tiles[self.y][self.x].set_occupant()  # set occupant to the initial tile
		t = {}  # create a dictionary which contains all tiles around the rover
		for i in range(5):
			t[i] = []
			for j in range(5):
				tile = self.planet.tiles\
						[self.spherical(self.x - 2 + j,self.y - 2 + i)[1]]\
						[self.spherical(self.x - 2 + j,self.y - 2 + i)[0]]
				t[i].append(tile)
				tile.set_occupant()
		if type == "shade":  # print each tile's shade type
			print("|{}|{}|{}|{}|{}|".format(t[0][0].terrain,
											t[0][1].terrain,
											t[0][2].terrain,
											t[0][3].terrain,
											t[0][4].terrain))
			print("|{}|{}|{}|{}|{}|".format(t[1][0].terrain,
											t[1][1].terrain,
											t[1][2].terrain,
											t[1][3].terrain,
											t[1][4].terrain))
			print("|{}|{}|H|{}|{}|".format(t[2][0].terrain,
											t[2][1].terrain,
											t[2][3].terrain,
											t[2][4].terrain))
			print("|{}|{}|{}|{}|{}|".format(t[3][0].terrain,
											t[3][1].terrain,
											t[3][2].terrain,
											t[3][3].terrain,
											t[3][4].terrain))
			print("|{}|{}|{}|{}|{}|".format(t[4][0].terrain,
											t[4][1].terrain,
											t[4][2].terrain,
											t[4][3].terrain,
											t[4][4].terrain))
			
		if type == "elevation":  # print each tile;s elevation's type
			print("|{}|{}|{}|{}|{}|".format(t[0][0].elevation(self),
											t[0][1].elevation(self),
											t[0][2].elevation(self),
											t[0][3].elevation(self),
											t[0][4].elevation(self)))
			print("|{}|{}|{}|{}|{}|".format(t[1][0].elevation(self),
											t[1][1].elevation(self),
											t[1][2].elevation(self),
											t[1][3].elevation(self),
											t[1][4].elevation(self)))
			print("|{}|{}|H|{}|{}|".format(t[2][0].elevation(self),
											t[2][1].elevation(self),
											t[2][3].elevation(self),
											t[2][4].elevation(self)))
			print("|{}|{}|{}|{}|{}|".format(t[3][0].elevation(self),
											t[3][1].elevation(self),
											t[3][2].elevation(self),
											t[3][3].elevation(self),
											t[3][4].elevation(self)))
			print("|{}|{}|{}|{}|{}|".format(t[4][0].elevation(self),
											t[4][1].elevation(self),
											t[4][2].elevation(self),
											t[4][3].elevation(self),
											t[4][4].elevation(self)))


	def statistic(self):
		"""
		Print the percentage of the planet that the rover has explored,
		and print the batery of the rover.
		"""
		self.planet.tiles[self.y][self.x].set_occupant()  # set occupant to the initial tile
		num_tile = self.planet.width * self.planet.height
		sum = 0
		for y in range(self.planet.height):
			for x in range(self.planet.width):
				tile = self.planet.tiles[y][x]
				if tile.occupant == 1:
					sum += 1
		percent = int((sum/num_tile)*100)
		print("Explored: {}%".format(percent))
		print("Battery: {}/100".format(self.battery))


	def finish(self):
		"""
		Print the percentage of the planet that the rover has explored,
		and exit the program.
		"""
		self.planet.tiles[self.y][self.x].set_occupant()  # set occupant to the initial tile
		num_tile = self.planet.width * self.planet.height
		sum = 0
		for y in range(self.planet.height):  # get the number of the tiles which have been explored
			for x in range(self.planet.width):
				tile = self.planet.tiles[y][x]
				if tile.occupant == 1:
					sum += 1
		percent = int((sum/num_tile)*100)
		print("You explored {}% of {}".format(percent, self.planet.name))


	def wait(self, cycles):
		"""
		The rover will wait for the specified cycles
		"""
		self.planet.tiles[self.y][self.x].set_occupant()  # set occupant to the initial tile
		if self.planet.tiles[self.y][self.x].is_shaded:  # in 'plain' the rover will recharge itself
			i = 0
			while i < int(cycles):
				if self.battery < 100:
					self.battery += 1
				i += 1

