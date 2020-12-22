from os import popen, name, system
from getpass import getuser
from socket import gethostname
from colorama import init, Style, Fore

init(autoreset=True)

# User-modifiable variables:
# prefix: Text shown before the input field
# shortcuts[]: List of commands that can be executed when typing something else.
prefix = Fore.CYAN + "[" + Fore.WHITE + getuser() + "@" + gethostname() + Fore.CYAN + "]" + Fore.RED + " > " + Fore.WHITE

# Shortcut format: [ ["Text to be typed", "Command to execute"], ["Text to be typed", "Command to execute"] ]
shortcuts = []

# ------------------------ End ------------------------

if name == "nt":
	system("cls")
else:
	system("clear")

while True:
	try:
		command = input(prefix)

		for shortcut in shortcuts:
			if command == shortcut[0]:
				command = shortcut[1]

		if command.lower() == "exit":
			break

		print(popen(command).read(), end="")
	except KeyboardInterrupt:
		print("\n", end="")
		pass
print("Good-bye.")