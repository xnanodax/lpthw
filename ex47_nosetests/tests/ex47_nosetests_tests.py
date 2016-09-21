from nose.tools import *
from ex47_nosetests.game import Room
from ex47_nosetests.game import Weapon
#just typing in import ex47_v1.game does not work!

def test_room():
	gold = Room("GoldRoom",
			"""This room has gold in it you can grab.
			There's a door to the north.""")
	assert_equal(gold.name, "GoldRoom")
	assert_equal(gold.paths, {})
	
def test_room_paths():
	center = Room("Center", "Test room in the center.")
	north = Room("North", "Test room in the north.")
	south = Room("South", "Test room in the south.")
	
	center.add_paths({'north': north, 'south': south})
	assert_equal(center.go('north'), north)
	assert_equal(center.go('south'), south)
	
def test_map():
	start = Room("Start", "You can go west and down a hole.")
	west = Room("Trees", "There are trees here, you can go east.")
	down = Room("Dungeon", "It's dark down there, you can go up.")
	
	start.add_paths({'west': west, 'down': down})
	west.add_paths({'east': start})
	down.add_paths({'up': start})
	
	assert_equal(start.go('west'), west)
	assert_equal(start.go('west').go('east'), start)
	assert_equal(start.go('down').go('up'), start)
	
def test_weapon():
	sword = Weapon("sword", 1)
	
	assert_equal(sword.name, "sword")
	assert_equal(sword.paths, {})
	assert_equal(sword.level, 1)
	
def test_weapon_paths():
	novice_weapon = Weapon("backpack", 0)
	sword = Weapon("sword", 1)
	dagger = Weapon("dagger", 1)
	
	novice_weapon.add_paths({'sword': sword, 'dagger': dagger})
	
	"""Testing without a return"""
	assert_equal(novice_weapon.paths, ({'sword': sword, 'dagger': dagger}))
	
	"""Testing with a return"""
	assert_equal(novice_weapon.equip('sword'), sword)
	
def test_weapon_swap():
	weapon1 = Weapon("sword", 1)
	weapon2 = Weapon("dagger", 1)
	
	weapon1.add_paths({weapon2: "sword"})
	assert_equal(weapon1.equip(weapon2), "sword")
	
	weapon2.add_paths({"dagger": weapon1})
	assert_equal(weapon2.equip("dagger"), weapon1)
	
	weapon1.add_paths({weapon1: weapon2})
	assert_equal(weapon1.equip(weapon1), weapon2)