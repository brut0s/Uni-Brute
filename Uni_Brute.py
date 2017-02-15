#!/usr/bin/python
#
#
import os
import sys, traceback
import time


print """



		             **************************************************
			     *			    _			      *
			     *  _   _ _ __ (_)     | |__  _ __ _   _| |_ ___  * 
		             * | | | | '_ \| |     | '_ \| '__| | | | __/ _ \ *
			     * | |_| | | | | |*****| |_) | |  | |_| | ||  __/ *
			     *  \__,_|_| |_|_|     |_.__/|_|   \__,_|\__\___| *
			     *						      *
			     **************************************************
                                               {{Author}}

                                              ***brut0s***

                                            {{Contributers}}

                                             ***Brandon*** #will be changed
               ++++__________________________|____________|_________________________++++
                 |+    This program is designed to bruteforcing website accounts    +|
                 |+ with interactive questions to generate profile about the Target +|
               ++++_________________________________________________________________++++

			   supports|:| http |:| https |:| irc |:| smtp |:|

"""

print "#" * 103
print "#########==Welcome to Uni-Brute, a universal bruteforcing program with Interactive Questions==#########"
print "#" * 103

print """
    [1]Create Password List
    [2]Create List of Usernames
    [3]Crack Account
    [4]Quit

    """


ans = raw_input("\n[!]...What would you like to do? ")



if ans == "1":





	print "#" * 69
	print "\n[!]...Ok Now I Need Some Intel About The Target"
	print "[!]...Enter The Target's Intel at The Prompt"
	print "[!]...Once completed, you will be asked to confirm The Current Settings"
print "#" * 69


first_name = raw_input("\n[1]...Please enter Target's Fist Name: ")
last_name = raw_input("\n[2]...Please Enter The Target's Last Name: ")
nick_name = raw_input("\n[3]...Please Enter The Target's Nick Nmae: ")
middle_name = raw_input("\n[4]...Please Enter The Target's Middle Initial: ")
yob = raw_input("\n[5]...Please Enter The Target's YOB: ")
last_four = raw_input("\n[6]...Please Enter The Target's Last 4 Of Digits Of Phone Number: ")
specail_char = raw_input("\n[7]...Please Enter Any Special Characters, like this '!, #, &' If Not Then Hit 'RETURN': ")
save_to_file = raw_input("\n[8]...Please Specify Path To Save Wordlists: ") #i also want to add the current path not #sure how

print "#" * 60

print """\nYou Entered:

	\n[1] First Name: %s
	\n[2] Last Name: %s
	\n[3] Nick Name: %s
	\n[4] Middle Initial/Name: %s
	\n[5] YOB: %s
	\n[6] Last Four Of Cell-Phone Number: %s
	\n[7] Specail Characters: %s
	\n[8] Path To Save WordList: %s
	\n\nIs This Correct? Enter [Y]/[N] If Yes Hit 'Return'""" % (

first_name, last_name, middle_name, yob, last_four, specail_char, save_to_file)



if ans == None:
        print "\n [-]...Not a Valid Option, Select From The Following"


if ans == "2":

	print "[!]...To Generate Custom List of UserNames I Need The Following: "

first_name = raw_input("\n[1]...Please enter Target's Fist Name: ")
last_name = raw_input("\n[2]...Please Enter The Target's Last Name: ")
nick_name = raw_input("\n[3]...Please Enter The Target's Nick Nmae: ")
yob = raw_input("\n[5]...Please Enter The Target's DOB: ")
specail_char = raw_input("\n[7]...Please Enter Any Special Characters If no the just hit 'RETURN': ")
save_to_file = raw_input("\n[8]...Please Specify Path To Save Wordlists: ") #i also want to add the current path not sure how

print "#" * 60

print """\nYou Entered:

	\n[1] First Name: %s
	\n[2] Last Name: %s
	\n[3] Nick Name: %s
	\n[4] YOB: %s
	\n[5] Specail Characters: %s
	\n[6] Path To Save WordList: %s
	\n\nIs This Correct? Enter [Y]/[N] If Yes Hit 'Return'""" % (

first_name, last_name, middle_name, yob, last_four, specail_char, save_to_file)

if ans == None:

	print "\n [-]...Not a Valid Option, Select From The Following"



while ans == "3":

	print "[!]...Before You can Attemp To Crack I The Targets Account You Need a Source"

print "#" * 60	
url_to_scrape = raw_input("[!]...Enter The Targets Source Account, via Website: ")
print "#" * 60



#url = requests.get(url_to_scrape)
