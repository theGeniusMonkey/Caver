from time import *

inventory = []
gold_amount = {"Gold": 50}

inp = input("Welcome to Caver! You wake up on a field, with nothing but a square made of concrete to the north. ").lower()

def cave_entrance(wow):
	if wow == "touch stone" or wow == "touch" or wow == "touch it":
		print("You reach out and lay your hand on the stone. It disintegrates and you fall in.")
		print("CAVE ENTRANCE")
		wat = input("You see a corridor to the east. To the north you see a wooden door that is slightly ajar. ").lower()
	elif wow == "g" or wow == "gold":
		print(gold_amount)
		new_wow = input("").lower()
		cave_entrance(new_wow)
	elif wow == "i" or wow == "inventory":
		new_wow = input("You have nothing in your inventory. ").lower()
		cave_entrance(new_wow)
	elif wow == "l" or wow == "look":
		new_wow = input("You look at your surroundings and see an open field. Directly in front of you is the concrete square, with \'DO NOT TOUCH\' written on it. ").lower()
		cave_entrance(new_wow)
	else:
		new_wow = input("I don\'t understand. ").lower()
		cave_entrance(new_wow)

def welcome(w):
	if w == "go north" or w == "north" or w == "n":
		wow = input("You approach the square. Upon closer inspection there is a small indentation in the center, and has the words \'DO NOT TOUCH\' engraved in it. ").lower()
		cave_entrance(wow)
	elif w == "go east" or w == "go west" or w == "go south" or w == "east" or w == "west" or w == "south" or w == "e" or w == "w" or w == "s":
		new_inp = input("You walk for what seems to be 5 miles, but you have not moved an inch. ").lower()
		welcome(new_inp)
	elif w == "g" or w == "gold":
		print(gold_amount)
		new_inp = input("").lower()
		welcome(new_inp)
	elif w == "i" or w == "inventory":
		new_inp = input("You have nothing in your inventory. ").lower()
		welcome(new_inp)
	elif w == "l" or w == "look":
		new_inp = input("You look around for something useful. All you see is the open field and the concrete square to the north. ").lower()
		welcome(new_inp)
	else:
		new_inp = input("I don\'t understand. ").lower()
		welcome(new_inp)

welcome(inp)
