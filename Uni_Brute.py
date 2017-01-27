#!/usr/bin/python
#
#
import os
import sys, traceback
import time


print ("""

                                                              {{Author}}

                                                             ***brut0s***

                                                           {{Contributers}}

                                                            ***Brandon*** #will be changed
                              ++++__________________________|____________|_________________________++++
                                |+    This program is designed to bruteforcing website accounts    +|
                                |+ with interactive questions to generate profile about the Target +|
                              ++++_________________________________________________________________++++




supports|:| http |:| https |:| irc |:| smtp |:|

""")

print "Welcome to Uni-Brute, a universal bruteforce attack program with Interactive Questions about The Target supports: |html|http|https|smtp|IRC| "

print("""
    [1]Create Password List
    [2]Create List of Usernames
    [3]Crack Account
    [4]Quit
    """)
ans = raw_input("What would you like to do? ")
if ans == "1":
	print("\n Creating password list...")
	text_file = open("passwords.txt", "w")
	text_file.write("password1")
	text_file.write("\npassword2")
	text_file.write("\npassword3")
	text_file.close()
	print("\nPassword list created.")
if ans == "2":
    print("\n Create Custom List of UserNames")
if ans == "3":
    print("\n Cracking Account")
if ans == "4":
    print("\n Thank you for using UniBrute")

# Will uncomment the below line once I remember how to make this correctly work.
#if ans == None:
#	print("\n Not a Valid Option, Select From The Following")

while ans == "1":
	

print("""Ok Now I Need Some Intel About The Target,
		Select from the following and Input the Targets Info,
		Once completed, you will be asked to confirm The Current Settings""")

print("""
    [1]Enter DOB
    [2]Enter First Name
    [3]Enter Last Name
    [4]Enter Nick Name
    [5]Enter Middle Name/Middle Initial
    [6]
    [7]Enter Last 4 of CellPhone Number
    [8]Enter Special Characters
    [9]Save to File
    [10]Return to Main Menu	
    """)
	
#if ans == None:
#        print ("\n Not a Valid Option, Select From The Following")


while ans == "2":

print("To Generate Custom List of UserNames I Need The Following: "
	
print("""
    [1]Enter First Name
    [2]Enter Last Name
    [3]Enter Middle Initial
    [4]Return to Main Menu
    """)

#if ans == None:
#        print ("\n Not a Valid Option, Select From The Following"


while ans == "3":
	
	print("Before You can Attemp To Crack The Targets Account You Need a Source")
	
url_to_scrape = raw_input("Enter The Targets Source Account, via Website: ")

url = requests.get(url_to_scrape)

for inmates in inmates:
	
	if inmates['login'] in inmates

print inmate

#lines of code from 102-110 is a website crawler for scaping, printing out, and confirming the login page of site, still working on it






print("Ok Now We Have The Target's Source ")





