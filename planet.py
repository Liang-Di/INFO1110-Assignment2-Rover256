class Planet:
	def __init__(self, name, width, height, num_tile):
		"""
		Initialise the planet object
		"""
		self.name = name
		self.width = width
		self.height = height
		self.num_tile = num_tile
		self.tiles = {}

	def add_tile(self, i, tiles):
		"""
		Let the tiles fill the planet, each tile has an
		coordinate so we can get an initial map
		"""
		self.tiles[i] = tiles

