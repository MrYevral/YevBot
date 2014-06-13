import socket
import string
import threading

botOwner = 'MrYevral'
nick = 'YevBot'
channel = '#mryevral'
server = 'irc.twitch.tv'
password = 'auth token goes here'
spamTimer = 0
irc = socket.socket()
irc.connect((server,6667))

irc.send('PASS ' + password + '\r\n')
irc.send('USER ' + nick + ' 0 *:' +botOwner+'\r\n')
irc.send('NICK ' + nick +'\r\n')
irc.send('JOIN ' + channel + '\r\n')

def message(msg):
	global spamTimer
	if spamTimer < 20:
		irc.send('PRIVMSG ' + channel + ' :' +msg+'\r\n')
		spamTimer+=1
	else:
		print 'Message Deleted'

def addMod(mod):
	global modList
	if isMod(mod):
		print mod + 'is already a mod on this channel'
	else:
		strippedMod = mod.strip()
		modFile = open(channel,'a')
		modFile.write(strippedMod+'\n')
		modFile.close()
		modList.append(strippedMod)
		modList.sort()
		print strippedMod + 'is now a mod'

def isMod(nick):
	print 'checking if: \'' + nick + '\' is a mod'
	print modList
	return nick in modList 


def fileLoad(file):
	try:
		with open(file) as f:
				return [l.rstrip() for l in f]
        except:
                File = open(file,'w+')
                return File.readlines()

def nameFind(msg):
        print msg + '\n'
        p1 = string.split(msg,':')
        print p1[1] + '\n'
        p0 = string.split(p1[1],'!')
        print p0[0] + '\n'
        return p0[0]

def isBad(word):
	swears = fileLoad(channel+"swears")
	return word in swears

def censor(msg):
	userText = string.split(msg,':',2)
	print userText[2]
	words = string.split(userText[2])
	for w in words:
		print w
		if isBad(w):
			message("/timeout "+nameFind(msg)+" 1")
			message("cleared")

			return
		



def infiniLoop():
	print 'in the loop'
	while True:

		data = irc.recv(1204)
		print data
		
		if data.find('PING') != -1:
			irc.send(data.replace('PING','PONG'))
		if data.find('!test') != -1:
			message('Hi')
		if data.find('!slow') != -1 and isMod(nameFind(data)):
			message('/slow 15')
			print 'hai'
		if data.find(' +o ') != -1:
			parts =  string.split(data,' +o ')
			print parts[1]
			addMod(parts[1])
		if data.find('JOIN') != -1:
			continue		

		censor(data)

found = False
while found!=True:
	data = irc.recv(2048)
	if data.find(":HISTORYEND") != -1:
		found = True
		modList  = fileLoad(channel)
infiniLoop()
