import unittest
from ex47_unittest.game import Room
from ex47_unittest.game import Weapon

#Execute this file into PowerShell to test whether the test cases were successful. 
#python tests/test_ex47_unittest.py 
class TestRoom(unittest.TestCase):
	
	def test_room(self):
		gold = Room("GoldRoom",
				"""This room has gold in it you can grab.
				There's a door to the north.""")
		self.assertEqual(gold.name, "GoldRoom")
		self.assertEqual(gold.paths, {})

	def test_room_paths(self):
		center = Room("Center", "Test room in the center.")
		north = Room("North", "Test room in the north.")
		south = Room("South", "Test room in the south.")	
		
		center.add_paths({'north': north, 'south': south})
		self.assertEqual(center.go('north'), north)
		self.assertEqual(center.go('south'), south)
	
	def test_map(self):
		start = Room("Start", "You can go west and down a hole.")
		west = Room("Trees", "There are trees here, you can go east.")
		down = Room("Dungeon", "It's dark down there, you can go up.")
		
		start.add_paths({'west': west, 'down': down})
		west.add_paths({'east': start})
		down.add_paths({'up': start})
		
		self.assertEqual(start.go('west'), west)
		self.assertEqual(start.go('west').go('east'), start)
		self.assertEqual(start.go('down').go('up'), start)
		
		
	def test_weapon(self):
		sword = Weapon("sword", 1)
		self.assertEqual(sword.name, "sword")
		self.assertEqual(sword.paths, {})
		self.assertEqual(sword.level, 1)
		
		
	def test_weapon_paths(self):
		novice_weapon = Weapon("backpack", 0)
		sword = Weapon("sword", 1)
		dagger = Weapon("dagger", 1)
		
		novice_weapon.add_paths({'sword': sword, 'dagger': dagger})
		
		"""Testing without a return"""
		self.assertEqual(novice_weapon.paths, ({'sword': sword, 'dagger': dagger}))
		
		"""Testing with a return"""
		self.assertEqual(novice_weapon.equip('sword'), sword)

	def test_weapon_swap(self):
		weapon1 = Weapon("sword", 1)
		weapon2 = Weapon("dagger", 1)
		
		weapon1.add_paths({weapon2: "sword"})
		self.assertEqual(weapon1.equip(weapon2), "sword")
		
		weapon2.add_paths({"dagger": weapon1})
		self.assertEqual(weapon2.equip("dagger"), weapon1)
		
		weapon1.add_paths({weapon1: weapon2})
		self.assertEqual(weapon1.equip(weapon1), weapon2)
		
if __name__ == '__main__':
	unittest.main()

