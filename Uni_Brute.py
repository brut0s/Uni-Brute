#!/usr/bin/python
#
#
import os
import sys, traceback
import time





print """



		           **************************************************
			   *			  _			    *
			   *  _   _ _ __ (_)     | |__  _ __ _   _| |_ ___  * 
		           * | | | | '_ \| |     | '_ \| '__| | | | __/ _ \ *
			   * | |_| | | | | |*****| |_) | |  | |_| | ||  __/ *
			   *  \__,_|_| |_|_|     |_.__/|_|   \__,_|\__\___| *
			   *						    *
			   **************************************************
                                               {{Author}}

                                              ***brut0s***

                                            {{Contributers}}

                                             ***Brandon*** #will be changed
               ++++_________________________|_____________|________________________++++
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

specail_char = raw_input("\n[7]...Please Enter Any Special Characters If no the just hit 'RETURN': ")
print "\nCurrent Working Directory: %s" % os.getcwd()
save_to_file = raw_input("[8]...Please Specify Path To Save Wordlists: ")


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
	\n\nIs This Correct? Enter [Y]/[N] If Yes Hit 'Return': """ % (

first_name, last_name, nick_name, middle_name, yob, last_four, specail_char, save_to_file)


if ans == none:
	print "\n [-]...Not a Valid Option, Select From The Following"

print "\n\t[!]...Now Generating WordList of Possible PassWords..."
print "\n[!]...Please Wait..."


#variable of users input
pass_list = first_name, last_name, nick_name, middle_name, yob, last_four, specail_char

#scram_pass_list = []
#    for pass_list1 in pass_list:
#        scram_pass_list.append(pass_list1)
#    		for pass_list2 in pass_list:
#			komb001 = list(first_name(last_name, yob))
#       				 komb002 = list(first_name(last_name, specail_char, yob))
#       					 komb003 = list(first_name(specail_char, last_name))



#f = open("pass_list.txt", "w+")
#for i in range():
#	f.write(pass_list)



#STILL WORKING ON SCRAMBLING THE RAW_INPUT AND WRITING TO FILE


if ans == "2":

	print "[!]...To Generate Custom List of UserNames I Need The Following: "


first_name = raw_input("\n[1]...Please enter Target's Fist Name: ")

last_name = raw_input("\n[2]...Please Enter The Target's Last Name: ")

nick_name = raw_input("\n[3]...Please Enter The Target's Nick Nmae: ")

yob = raw_input("\n[5]...Please Enter The Target's DOB: ")

specail_char = raw_input("\n[7]...Please Enter Any Special Characters If no the just hit 'RETURN': ")
print "\n[!]...Current Working Directory: %s" % os.getcwd()
save_to_file = raw_input("\n[8]...Please Specify Path To Save Wordlists: ") 



print "#" * 60

print """\nYou Entered:

	\n[1] First Name: %s
	\n[2] Last Name: %s
	\n[3] Nick Name: %s
	\n[4] YOB: %s
	\n[5] Specail Characters: %s
	\n[6] Path To Save WordList: %s
	\n\nIs This Correct? Enter [Y]/[N] If Yes Hit 'Return'""" % (

first_name, last_name, nick_name, yob, specail_char, save_to_file)

if ans == none:
	print "\n [-]...Not a Valid Option, Select From The Following"


print "\n\t[!]...Now Generating WordList of Possible User-Names..."
print "\n[!]...Please Wait..."

#variable of users input
user_list = first_name, last_name, nick_name, yob, specail_char

#scram_user_list = []
#    for user_list1 in user_list:
#        scram_user_list.append(user_list1)
#       	 for user_list2 in user_list:
#       		 komb001 = list(first_name(last_name, yob))
#       			 komb002 = list(first_name(last_name, specail_char, yob))
#       				 komb003 = list(first_name(specail_char, last_name))


#f = open("user_list.txt", "w+")
#for i in range():
#        f.write(user_list)




#STILL WORKING ON SCRAMBLING THE RAW_INPUT AND WRITING TO FILE


while ans == "3":

	print "[!]...Before You can Attemp To Crack I The Targets Account You Need a Source"

print "#" * 60	
url_to_scrape = raw_input("[!]...Enter The Targets Source Account, via Website: ")
print "#" * 60






#
#code for this section is for adding the scraper for finding the login page from the users input of the source
#then add code to start the bruteforce attack
#
#once the attck is finish have it print out if it was found or not 
#and have it print out the % of the attack completed acording to how much of the wordlists was already used
#



#url = requests.get(url_to_scrape)






#
#and then add an options to loop back to the main menu or quit program 
#

