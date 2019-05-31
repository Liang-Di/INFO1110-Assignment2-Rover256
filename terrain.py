class Tile:

	def __init__(self, type, high_elevation, low_elevation):
		"""
		Initialises the terrain tile and attributes
		"""
		self.type = type
		self.high_elevation = high_elevation
		self.low_elevation = low_elevation
		self.occupant = 0  # use 0 to initilize tile which 
							# means it has not been explored.
		if type == "plains":  # initialize the shade
			self.terrain = " "
		else:
			self.terrain = "#"


	def is_shaded(self):
		"""
		Returns True if the terrain tile is shaded, otherwise False
		"""
		if self.terrain == "#":
			return True
		return False

	def is_slope(self):
		"""
		Returns True if the terrain tile is slope, otherwise False
		"""
		if self.high_elevation != self.low_elevation:
			return True
		return False

	def elevation(self, rover):
		"""
		Returns a symbol to show the terrain object
		"""
		current_tile = rover.planet.tiles[rover.y][rover.x]
		#current_tile is slope
		if current_tile.is_slope():
			#self is slope current_tile is slope
			if self.is_slope():
				if current_tile.high_elevation == self.low_elevation:
					return "/"
				if current_tile.low_elevation == self.high_elevation:
					return "\\"
				if self.high_elevation < current_tile.low_elevation:
					return "-"
				if self.low_elevation > current_tile.high_elevation:
					return "+"
				if self.low_elevation == current_tile.low_elevation\
					and self.high_elevation == current_tile.high_elevation:
					return " "
			#self is flat current_tile is slope
			else:
				if self.low_elevation > current_tile.high_elevation:
					return "+"
				if self.low_elevation < current_tile.low_elevation:
					return "-"
				return " "


		else:  #current_tile is flat
			#self is slope current_tile is flat
			if self.is_slope():
				if self.low_elevation == current_tile.low_elevation:
					return "/"
				if self.high_elevation == current_tile.low_elevation:
					return "\\"
				if self.low_elevation > current_tile.low_elevation:
					return "+"
				if self.high_elevation < current_tile.low_elevation:
					return "-"
			#self is flat current_tile is flat
			else:
				if self.low_elevation > current_tile.low_elevation:
					return "+"
				if self.high_elevation < current_tile.low_elevation:
					return "-"
			return " "


	def set_occupant(self):
		"""
		Sets the occupant on the terrain tile
		If one tile has been explored, use 1 to set occupant.
		Otherwise use 0 which means it has not been explored.
		"""
		self.occupant = 1


	def get_occupant(self):
		"""
		Gets the entity on the terrain tile
		If nothing is on this tile, it should return None
		"""
		return self.occupant

