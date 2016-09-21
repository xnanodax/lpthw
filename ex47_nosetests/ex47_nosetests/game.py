class Room(object):

    def __init__(self, name, description):
        self.name = name
        self.description = description
        self.paths = {}

    def go(self, direction):
        return self.paths.get(direction, None)

    def add_paths(self, paths):
        self.paths.update(paths)
		
class Weapon(object):
	
	def __init__(self, name, level):
		self.name = name
		self.paths = {}
		self.level = level
	
	def equip(self, weapon):
		"""This will receive the value of the added path"""
		return self.paths.get(weapon, None)
		
	def add_paths(self, paths):
		"""adding to the dictionary list of paths"""
		self.paths.update(paths)