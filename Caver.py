#Creates a list that is the players inventory. Starts empty.
inventory = []

#Creates a dict that is the players gold storage. Starts with none.
gold_amount = {"Gold": 0}

#Very first thing the player reads.
print("Welcome to Caver!")
print("You wake up on a field, with nothing but a square made of concrete to the north.")
print("(Use \'help\' to see commands)")
inp = input(">").lower()

def weapons(a):
	if a == "go to" or a == "go":
		print("Where do you want to go?")
		arm = input(">").lower()
		weapons(arm)

def explore_one(d):
	if d == "go east" or d == "east" or d == "e":
		print("You walk down the corridor a bit until you reach a dead end.")
		print("You turn around and walk back to the cave entrance.")
		print("")
		print("CAVE ENTRANCE")
		print("You see a corridor to the east.")
		print("To the north you see a wooden door that is slightly ajar.")
		dor = input(">").lower()
		explore_one(dor)
	elif d == "go north" or d == "north" or d == "n" or d == "open door" or d == "open":
		print("You open the door and walk through.")
		print("")
		print("ARMAMENTS ROOM")
		print("You enter a medium sized room to see four tables.")
		print("Each table has a label, and are labelled \'Table 1\' \'Table 2\' and so forth.")
		print("Underneath the labels is something written in small print.")
		print("Each table has a few weapons on them, and different amounts of gold.")
		weap = input(">").lower()
		weapons(weap)
	elif d == "go west" or d == "w" or d == "west" or d == "south" or d == "go south" or d == "s":
		print("There is a wall there.")
		dor = input(">").lower()
		explore_one(dor)
	elif d == "l" or d == "look":
		print("You see a corridor heading of to the east.")
		print("There is a door slightly ajar to the north.")
		dor = input(">").lower()
		explore_one(dor)
	elif d == "g" or d == "gold":
		print(gold_amount)
		dor = input(">").lower()
		explore_one(dor)
	elif d == "inspect" or d == "examine":
		print("What would you like to inspect?")
		dor = input(">").lower()
		explore_one(dor)
	elif d == "i" or d == "inventory":
		print("You have nothing in your inventory.")
		dor = input(">").lower()
		explore_one(dor)
	else:
		print("I don\'t understand.")
		dor = input(">").lower()
		explore_one(dor)

def cave_entrance(wow):
	if wow == "touch stone" or wow == "touch" or wow == "touch it":
		print("You reach out and lay your hand on the stone. It disintegrates and you fall in.")
		print("CAVE ENTRANCE")
		print("You see a corridor to the east.")
		print("To the north you see a wooden door that is slightly ajar.")
		dor = input(">").lower()
		explore_one(dor)
	elif wow == "g" or wow == "gold":
		print(gold_amount)
		new_wow = input(">").lower()
		cave_entrance(new_wow)
	elif wow == "i" or wow == "inventory":
		print("You have nothing in your inventory.")
		new_wow = input(">").lower()
		cave_entrance(new_wow)
	elif wow == "l" or wow == "look":
		print("You look at your surroundings and see an open field.")
		print("Directly in front of you is the concrete square, with \'DO NOT TOUCH\' written on it.")
		new_wow = input(">").lower()
		cave_entrance(new_wow)
	elif wow == "inspect" or wow == "examine":
		print("You look more closely at the stone.")
		print("There's nothing interesting about it except the \'DO NOT TOUCH\' engraving.")
		new_wow = input(">").lower()
		cave_entrance(new_wow)
	else:
		print("I don\'t understand.")
		new_wow = input(">").lower()
		cave_entrance(new_wow)

def welcome(w):
	if w == "go north" or w == "north" or w == "n":
		print("You approach the square.")
		print("Upon closer inspection there is a small indentation in the center.")
		print("It has the words \'DO NOT TOUCH\' engraved in it.")
		wow = input(">").lower()
		cave_entrance(wow)
	elif w == "go east" or w == "go west" or w == "go south" or w == "east" or w == "west" or w == "south" or w == "e" or w == "w" or w == "s":
		print("You walk for what seems to be 5 miles, but you have not moved an inch.")
		new_inp = input(">").lower()
		welcome(new_inp)
	elif w == "g" or w == "gold":
		print(gold_amount)
		new_inp = input(">").lower()
		welcome(new_inp)
	elif w == "i" or w == "inventory":
		print("You have nothing in your inventory.")
		new_inp = input(">").lower()
		welcome(new_inp)
	elif w == "l" or w == "look":
		print("You look around for something useful.")
		print("All you see is the open field and the concrete square to the north.")
		new_inp = input(">").lower()
		welcome(new_inp)
	elif w == "inspect" or w == "examine":
		print("There is nothing here to look at.")
		new_inp = input(">").lower()
		welcome(new_inp)
	elif w == "help" or w == "h" or w == "?":
		print("===COMMANDS===")
		print("\'l\'- Look at your surroundings.")
		print("\'i\'- Check your inventory.")
		print("\'g\'- Check how much gold you have.")
		print("\'n\', \'e\', \'s\', and \'w\'- North, East, South, and West, respectively.")
		print("\'examine\' or \'inspect\'- Look closely at something.")
		print("\'take\'- Takes a specified object.")
		print("\'open\'- Opens a specified object.")
		print("There are also commands not listed here, such as \'go to\' or \'touch\'...")
		print("You'll have to intuit those on your own.")
		new_inp = input(">").lower()
		welcome(new_inp)
	else:
		print("I don\'t understand.")
		new_inp = input(">").lower()
		welcome(new_inp)

#Passes the player's first input into the function welcome.
welcome(inp)
