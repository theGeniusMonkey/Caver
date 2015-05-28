from time import *

#Creates a list that is the players inventory. Starts empty.
inventory = []

#Creates a dict that is the players gold storage. Starts with none.
gold_amount = {"Gold": 0}

#Very first thing the player reads.
print("Welcome to...\n")
sleep(1)
print(" @@@@@@@   @@@@@@   @@@  @@@  @@@@@@@@  @@@@@@@ ")
sleep(.65)
print("@@@@@@@@  @@@@@@@@  @@@  @@@  @@@@@@@@  @@@@@@@@")
sleep(.65)
print("!@@       @@!  @@@  @@!  @@@  @@!       @@!  @@@")
sleep(.65)
print("!@!       !@!  @!@  !@!  @!@  !@!       !@!  @!@")
sleep(.65)
print("!@!       @!@!@!@!  @!@  !@!  @!!!:!    @!@!!@! ")
sleep(.65)
print("!!!       !!!@!!!!  !@!  !!!  !!!!!:    !!@!@!  ")
sleep(.65)
print(":!!       !!:  !!!  :!:  !!:  !!:       !!: :!! ")
sleep(.65)
print(":!:       :!:  !:!   ::!!:!   :!:       :!:  !:!")
sleep(.65)
print("'::: :::  ::   :::    ::::     :: ::::  ::   :::")
sleep(.65)
print(" :: :: :   :   : :     :      : :: ::   ':   : :")
sleep(.65)
print("\n\n")
print("You wake up on a field with nothing but a square made of concrete to the north.")
sleep(.65)
print("(Use \'help\' to see commands)")
user = input(">").lower()

#Function that states generic responses
def generic(user):
	if user == "g" or user == "gold":
		print(gold_amount)
		return True
	if user == "i" or user == "inventory":
		print("You have...")
		for item in inventory:
			print("-" + item)
		if len(inventory) == 0:
			print("nothing.")
		return True
	if user == "help" or user == "h" or user == "?":
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
		return True

def weapons(user):
	if user == "go to" or user == "go":
		print("Where do you want to go?")
		user = input(">").lower()
		if user == "table 1":
			items = { "inventory_items": ["steel chestpiece", "shiny warhammer"], "gold_coins": 2 }
			print("You walk up to table 1. You see:")
			for item in items["inventory_items"]:
				print(item)
			print(str(items["gold_coins"]) + " gold coins")
			take = input(">").lower()
			if take == "take":
				print("What item do you want to take?")
				item = input(">").lower()
				if item in items["inventory_items"]:  # Check if the item the user entered is in the provided list
					inventory.append(item)
				elif item == "gold" or item == "coins" or item == "gold coins":
					gold_amount["Gold"] += items["gold_coins"]
			else:
				if generic(take) == True:
					take = input(">").lower()
					weapons(take)
				else:
					print("I don\'t understand.")
					take = input(">").lower()
					weapons(take)
		elif user == "table 2":
			print("You walk up to table 2. You see:")
			items = { "inventory_items": ["valkyrie helmet", "ulfbehrt sword"], "gold_coins": 23}
			for item in items["inventory_items"]:
				print(item)
			print(str(items["gold_coins"]) + " gold coins")
			take = input(">").lower()
			if take == "take":
				print("What item do you want to take?")
				item = input(">").lower()
				if item in items["inventory_items"]:  # Check if the item the user entered is in the provided list
					inventory.append(item)
				elif item == "gold" or item == "coins" or item == "gold coins":
					gold_amount["Gold"] += items["gold_coins"]
			else:
				if generic(take) == True:
					take = input(">").lower()
					weapons(take)
				else:
					print("I don\'t understand.")
					take = input(">").lower()
					weapons(take)
		elif user == "table 3":
			print("You walk up to table 3. You see:")
			items = { "inventory_items": ["2 fire-resistant gauntlets", "battleaxe"], "gold_coins": 10}
			for item in items["inventory_items"]:
				print(item)
			print(str(items["gold_coins"]) + " gold coins")
			take = input(">").lower()
			if take == "take":
				print("What item do you want to take?")
				item = input(">").lower()
				if item in items["inventory_items"]:  # Check if the item the user entered is in the provided list
					inventory.append(item)
				elif item == "gold" or item == "coins" or item == "gold coins":
					gold_amount["Gold"] += items["gold_coins"]
			else:
				if generic(take) == True:
					take = input(">").lower()
					weapons(take)
				else:
					print("I don\'t understand.")
					take = input(">").lower()
					weapons(take)
		elif user == "table 4":
			print("You walk up to table 4. You see:")
			items = { "inventory_items": ["tin foil helmet", "fire scythe"], "gold_coins": 6}
			for item in items["inventory_items"]:
				print(item)
			print(str(items["gold_coins"]) + " gold coins")
			take = input(">").lower()
			if take == "take":
				print("What item do you want to take?")
				item = input(">").lower()
				if item in items["inventory_items"]:  # Check if the item the user entered is in the provided list
					inventory.append(item)
				elif item == "gold" or item == "coins" or item == "gold coins":
					gold_amount["Gold"] += items["gold_coins"]
			else:
				if generic(take) == True:
					take = input(">").lower()
					weapons(take)
				else:
					print("I don\'t understand.")
					take = input(">").lower()
					weapons(take)
		else:
			if generic(user) == True:
				user = input(">").lower()
				weapons(user)
			else:
				print("I don\'t understand.")
				user = input(">").lower()
				weapons(user)
	else:
		if generic(user) == True:
			user = input(">").lower()
			weapons(user)
		else:
			print("I don\'t understand.")
			user = input(">").lower()
			weapons(user)

def explore_one(user):
	if user == "go east" or user == "east" or user == "e":
		print("You walk down the corridor a bit until you reach a dead end.")
		print("You turn around and walk back to the cave entrance.")
		print("")
		print("CAVE ENTRANCE")
		print("You see a corridor to the east.")
		print("To the north you see a wooden door that is slightly ajar.")
		user = input(">").lower()
		explore_one(user)
	elif user == "go north" or user == "north" or user == "n" or user == "open door" or user == "open":
		print("You open the door and walk through.")
		print("")
		print("ARMAMENTS ROOM")
		print("You enter a medium sized room to see four tables.")
		print("Each table has a label, and are labelled \'Table 1\' \'Table 2\' and so forth.")
		print("Underneath the labels is something written in small print.")
		print("Each table has a few weapons on them, and different amounts of gold.")
		user = input(">").lower()
		weapons(user)
	elif user == "go west" or user == "w" or user == "west" or user == "south" or user == "go south" or user == "s":
		print("There is a wall there.")
		user = input(">").lower()
		explore_one(user)
	elif user == "l" or user == "look":
		print("You see a corridor heading of to the east.")
		print("There is a door slightly ajar to the north.")
		user = input(">").lower()
		explore_one(user)
	elif user == "g" or user == "gold":
		print(gold_amount)
		user = input(">").lower()
		explore_one(user)
	elif user == "inspect" or user == "examine":
		print("What would you like to inspect?")
		user = input(">").lower()
		explore_one(user)
	elif user == "i" or user == "inventory":
		print("You have nothing in your inventory.")
		user = input(">").lower()
		explore_one(user)
	else:
		if generic(user) == True:
			user = input(">").lower()
			explore_one(user)
		else:
			print("I don\'t understand.")
			user = input(">").lower()
			explore_one(user)

def cave_entrance(user):
	if user == "touch stone" or user == "touch" or user == "touch it":
		print("You reach out and lay your hand on the stone. It disintegrates and you fall in.")
		print("CAVE ENTRANCE")
		print("You see a corridor to the east.")
		print("To the north you see a wooden door that is slightly ajar.")
		user = input(">").lower()
		explore_one(user)
	elif user == "g" or user == "gold":
		print(gold_amount)
		user = input(">").lower()
		cave_entrance(user)
	elif user == "i" or user == "inventory":
		print("You have nothing in your inventory.")
		user = input(">").lower()
		cave_entrance(user)
	elif user == "l" or user == "look":
		print("You look at your surroundings and see an open field.")
		print("Directly in front of you is the concrete square, with \'DO NOT TOUCH\' written on it.")
		user = input(">").lower()
		cave_entrance(user)
	elif user == "inspect" or user == "examine":
		print("You look more closely at the stone.")
		print("There's nothing interesting about it except the \'DO NOT TOUCH\' engraving.")
		user = input(">").lower()
		cave_entrance(user)
	else:
		if generic(user) == True:
			user = input(">").lower()
			cave_entrance(user)
		else:
			print("I don\'t understand.")
			user = input(">").lower()
			cave_entrance(user)

def welcome(user):
	if user == "go north" or user == "north" or user == "n":
		print("You approach the square.")
		print("Upon closer inspection there is a small indentation in the center.")
		print("It has the words \'DO NOT TOUCH\' engraved in it.")
		user = input(">").lower()
		cave_entrance(user)
	elif user == "go east" or user == "go west" or user == "go south" or user == "east" or user == "west" or user == "south" or user == "e" or user == "w" or user == "s":
		print("You walk for what seems to be 5 miles, but you have not moved an inch.")
		user = input(">").lower()
		welcome(user)
	elif user == "l" or user == "look":
		print("You look around for something useful.")
		print("All you see is the open field and the concrete square to the north.")
		user = input(">").lower()
		welcome(user)
	elif user == "inspect" or user == "examine":
		print("There is nothing here to look at.")
		user = input(">").lower()
		welcome(user)
	else:
		if generic(user) == True:
			user = input(">").lower()
			welcome(user)
		else:
			print("I don\'t understand.")
			user = input(">").lower()
			welcome(user)

#Passes the player's first input into the function welcome.
welcome(user)
