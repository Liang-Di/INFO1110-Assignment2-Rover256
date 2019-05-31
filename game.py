import os
from terrain import Tile
from rover import Rover
from planet import Planet
from loader import load_level
from loader import check


def quit():
	"""
	Will quit the program
	"""
	exit()


def menu_help():
	"""
	Displays the help menu of the game
	"""
	print()
	print("START <level file> - Starts the game with a provided file.")
	print("QUIT - Quits the game")
	print("HELP - Shows this message")
	print()


def menu_start_game(filepath):
	"""
	Will start the game with the given file path
	"""
	if check(filepath):
		menu(filepath)


def menu(filename):
	"""
	Start the menu component of the game
	"""
	planet, rover = load_level(filename)
	while True:  #use infinity loop to get command, command can be one or
				#two characters
		command = input().split()  #cut the command
		if command[0] == "SCAN":  #use scan fuction
			print()
			rover.scan(command[1])
			print()
		elif command[0] == "MOVE":  #use move fuction
			rover.move(command[1], command[2])
		elif command[0] == "WAIT":  #use wait fuction
			rover.wait(command[1])
		elif command[0] == "STATS":  #use statistic fuction
			print()
			rover.statistic()
			print()
		elif command[0] == "FINISH":  #use finish fuction and break
			print()
			rover.finish()
			print()
			break
		else:
			print()
			print("No menu item")
			print()




while True:  #use infinity loop to get menu command
	command = input().split()
	if command[0] == "QUIT":  # exit the program
		quit()
	elif command[0] == "HELP":  # print help words
		menu_help()
	elif command[0] == "START":  # start the game and use menu fuction
		if len(command) == 2:
			menu_start_game(command[1])
		else:
			print("Invalid level file name")
	else:
		print()
		print("No menu item")
		print()

