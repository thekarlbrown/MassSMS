# Name: masssms.py

# $ python masssms.py targetfile

# You must create an accounts.txt file with at least 1 account to use, the target "can" be obtained at runtime
# Linked Accounts use basic starttls authentication via SMTP server
#    ACCOUNT FILE SYNTAX:

#    FULLLOGIN:PASSWORD:SERVER:PORT       (Login, may include domain):(Password):(SMTP server):(SMTP port)
#    FULLLOGIN:PASSWORD:SERVER:PORT

# You can have multiple targets, but each requires correct syntax and go after each other without gaps.
#	 TARGET FILE SYNTAX:

#	 5				(Number Of Messages to send)
#	 1234567890			(SMS/Email)
#	 -1				(ID of Carrier to use; -1 unknown carrier, 0 if email address)
#	 ya got shrekt m8 				(Message to send, 0 = Random)
#    (This line will be ignored when parsing file, separates each victim) 
#	 10				
#	 noob@gmail.com			
#	 0
#   WILL YOU FLY AWAY WITH ME? <3
#    Note: Be careful with the mass emails/sms. They can be spam depending on your jurisdiction and use, and mail servers can filter them or contact your SMTP server based on how you use them.
   				
				
#     http://www.emailtextmessages.com/ Good list sms conversions for carriers, Google more if necessary

import smtplib as s
import os
import sys
import random
import string

#Your carrier lists (which is modified based on need or projected likely carriers in target demographic) goes here
#If you are lazy, you can ignore the string when editing and mass add carriers, but your SMTP will get flooded with failed requests

# Carriers as String (default common US)
carrierString = " What is their carrier? \n    -1: Unknown \n    0:Email Address\n    1: Alltel\n    2: AT&T Or Cingular\n    3: Cricket\n    4: Boost Mobile\n    5: Comcast\n    6: MetroPCS\n    7: Orange\n    8: Rogers\n    9: Sprint\n    10: T-Mobile\n    11: Telus\n    12: Verizon\n    13: Virgin Mobile\n    14: Bell"
# Carriers as Array (default common US)
carrierArray = ["YouGoofed", "alltelmessage.com", "txt.att.net","myboostmobile.com","comcastpcs.textmsg.com","mymetropcs.com",  "sms.orange.pl","pcs.rogers.com", "messaging.sprintpcs.com", "tmomail.net", "msg.telus.com", "vtext.com", "vmob1.com", "txt.bell.ca"]
	
# Generation of garbage text if no message
def generateRandom():
	randomText = ''.join([random.choice(string.ascii_letters + string.digits) for n in xrange(120)])
	randomContent = randomText + randomText + randomText
	return randomContent

# The loop
def msgLoop(target, cellCarrier, message, goUntil):
	#assigned based on email, guessing provider, or known provider
	if(cellCarrier==0):
		fullAddress = str(target)
	elif (cellCarrier==-1):
		liststart=1
		tempAddress=""
		#adds from carrierArray and removes final ;
		while(liststart<len(carrierArray)):
			tempAddress = tempAddress + str(target) +"@" +str(carrierArray[liststart])+" "
			liststart+=1
		fullAddress=tempAddress[:len(tempAddress)-1]
	else:	
		fullAddress = str(target) +"@" +str(carrierArray[cellCarrier])
	tid = 0	
	while tid < goUntil:
		# This checks if you chose to generate a random message
		if message == 0:
			message = generateRandom()
		# Accounts should be in username:password:server:port format!
		accountsFile = open("accounts.txt", "r")
		#Pick a random account
		whichAccount = random.choice(accountsFile.readlines())
		# Delimiting username and password with :
		breakLine = whichAccount.split(":")
		#break apart your selected account
		username = breakLine[0]
		password = breakLine[1]
		smtpServer = breakLine[2]
		smtpPort = breakLine[3].strip('\n')
		# Preparing the SMTP connection
		obj = s.SMTP(smtpServer, smtpPort)
		obj.ehlo()
		obj.starttls()
		obj.ehlo()
		obj.login(username, password)
		# Sending the SMTP
		obj.sendmail(username, fullAddress.split(),message)
		# Informing you
		print("Message " + str(tid+1) + " of " + str(goUntil) + " (from " + str(username) + " to " + str(target) + ")")
		# Incrementing the number of emails sent
		tid = tid + 1		
#main program and intro
print("Mass SMS Bulk SMS/Email Client \n\r")
print("Accounts and information for the server are stored in accounts.txt \n \r")
print("No accounts? Any SMTP with starttls support works. Try https://cock.li/register \n\r")
# TargetFile parsing for premade/numerous targets
if len(sys.argv) > 1:
	targetFile = sys.argv[1]
	targetGet = open(targetFile, 'r').readlines()
	start=0
	targets=0
	target=[]
	goUntil=[]
	cellCarrier=[]
	message=[]
	#grabs them all, skips line, avoids potential end garbage
	while((start+2)<len(targetGet)):
		target.append(targetGet[start+1])
		goUntil.append(targetGet[start]) 
		cellCarrier.append(targetGet[start+2])
		message.append(targetGet[start+3])
		start+=5
		targets+=1
	loopstart=0
	while(loopstart<targets):
		msgLoop(target[loopstart], int(cellCarrier[loopstart]), str(message[loopstart]), int(goUntil[loopstart]))
		loopstart+=1
#Manual input of single target
else:
	print("Create a target file and you can do this quicker/automated\n\r")
	goUntil = input("Send this many: ")
	target = raw_input("Telephone Number/Email: ")
	cellCarrier = input(carrierString + "\n: ")
	print("What message would you like?\n")
	message = raw_input("(Type 0 for random text) :")
	msgLoop(target, int(cellCarrier), message, int(goUntil))
