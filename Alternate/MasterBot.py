'''This gile will take arguments from the command line, if none are found it
will look for a .bot file, if that isn't found it will promt the user for auth
tokens :- with this information the masterbot will connect to its own twitch channel and await a !connect command'''
#Author MrYevral
#check for .bot file in current directory
import os
import sys
def getBotInfo():
	if len(sys.argv) > 2:
		if sys.argv[2] == '-c':
			newBotFile()
		else:
			print "incorrect use of flags please use -c for creating a bot"
'''for file in os.listdir("."):
	if file.endswith(".bot"):
		print file'''
