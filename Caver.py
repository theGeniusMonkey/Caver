inventory = []
gold_amount = {"Gold": 50}

inp = input("Welcome to Caver! You wake up on a field, with nothing but a square made of concrete to the north. ").lower()

def cave_entrance(wow):
	if wow == "touch stone" or wow == "touch" or wow == "touch it":
		print("You reach out and lay your hand on the stone. It disintegrates and you fall in.")
		print("CAVE ENTRANCE")
		print("You see a corridor to the east. To the north you see a wooden door that is slightly ajar.")
		dor = input("").lower()
		explore_one(dor)
	elif wow == "g" or wow == "gold":
		print(gold_amount)
		new_wow = input("").lower()
		cave_entrance(new_wow)
	elif wow == "i" or wow == "inventory":
		print("You have nothing in your inventory.")
		new_wow = input("").lower()
		cave_entrance(new_wow)
	elif wow == "l" or wow == "look":
		print("You look at your surroundings and see an open field. Directly in front of you is the concrete square, with \'DO NOT TOUCH\' written on it.")
		new_wow = input("").lower()
		cave_entrance(new_wow)
	elif wow == "inspect" or wow == "examine":
		print("You look more closely at the stone. There's nothing interesting about it except the \'DO NOT TOUCH\' engraving.")
		new_wow = input("").lower()
		cave_entrance(new_wow)
	else:
		print("I don\'t understand. ")
		new_wow = input("").lower()
		cave_entrance(new_wow)

def welcome(w):
	if w == "go north" or w == "north" or w == "n":
		print("You approach the square. Upon closer inspection there is a small indentation in the center, and has the words \'DO NOT TOUCH\' engraved in it. ")
		wow = input("").lower()
		cave_entrance(wow)
	elif w == "go east" or w == "go west" or w == "go south" or w == "east" or w == "west" or w == "south" or w == "e" or w == "w" or w == "s":
		print("You walk for what seems to be 5 miles, but you have not moved an inch. ")
		new_inp = input("").lower()
		welcome(new_inp)
	elif w == "g" or w == "gold":
		print(gold_amount)
		new_inp = input("").lower()
		welcome(new_inp)
	elif w == "i" or w == "inventory":
		print("You have nothing in your inventory.")
		new_inp = input("").lower()
		welcome(new_inp)
	elif w == "l" or w == "look":
		print("You look around for something useful. All you see is the open field and the concrete square to the north.")
		new_inp = input("").lower()
		welcome(new_inp)
	else:
		print("I don\'t understand.")
		new_inp = input("").lower()
		welcome(new_inp)

welcome(inp)
