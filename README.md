-Name: masssms.py

-$ python masssms.py targetfile

You must create an accounts.txt file with at least 1 account to use
Linked Accounts use basic starttls authentication via SMTP server

-ACCOUNT FILE SYNTAX:

FULLLOGIN:PASSWORD:SERVER:PORT       (Login, may include domain):(Password):(SMTP server):(SMTP port)
FULLLOGIN:PASSWORD:SERVER:PORT

- You can have multiple targets, but each requires correct syntax and go after each other without gaps.
#	 TARGET FILE SYNTAX:

5				(Number Of Messages to send)
1234567890			(SMS/Email)
-1				(ID of Carrier to use; -1 unknown carrier, 0 if email address)
ya got shrekt m8 				(Message to send, 0 = Random)
(This line will be ignored when parsing file, separates each victim) 
10				
noob@gmail.com			
0
WILL YOU FLY AWAY WITH ME? <3
- Note: Be careful with the mass emails/sms. They can be spam depending on your jurisdiction and use, and mail servers can filter them or contact your SMTP server based on how you use them.
  				
			
-    http://www.emailtextmessages.com/ Good list sms conversions for carriers, Google more if necessary
