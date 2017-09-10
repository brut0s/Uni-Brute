#!/usr/bin/python
#
#

import os

print """

Module:

 _   _ _ __ (_)      _   _ ___  ___ _ __
| | | | '_ \| |_____| | | / __|/ _ \ '__|
| |_| | | | | |_____| |_| \__ \  __/ |
 \__,_|_| |_|_|      \__,_|___/\___|_|

\nWhat is Uni-User?
Uni-User is a Module Within 'Uni-Brute'
that makes a list of user names with the basic
info that Uni-User asks at each prompt.
With this Module you can quickly make a list
of possible user-names that you're target
might of used.

"""

################################################
##       Prompts you for basic info to        ##
################################################

first_name = raw_input("First Name: ")
last_name = raw_input("\nLast Name: ")
middle_init = raw_input("\nMiddle Initial: ")
nick = raw_input("\nNick Name: ")
four_yob = raw_input("\n4 Digit Year of Birth: ")
two_yob = raw_input("\n2 Digit Year of Birth: ")

print """
##############################################################
[!]...Generating, list of possible user-names, please wait..."
##############################################################
"""

################################################
##Scrambling of users input and saving to file##
################################################


file = "uni-user-list.txt"
wordlist = open(file, 'w')

wordlist.write(last_name + "-" + four_yob)
wordlist.write("\n")
wordlist.write(first_name + middle_init + two_yob)
wordlist.write("\n")
wordlist.write(first_name + middle_init + "-" + two_yob)
wordlist.write("\n")
wordlist.write(first_name + middle_init + "-" + four_yob)
wordlist.write("\n")
wordlist.write(first_name + middle_init + "_" + two_yob)
wordlist.write("\n")
wordlist.write(first_name + middle_init + "_" + four_yob)
wordlist.write("\n")
wordlist.write(first_name + "-" + four_yob)
wordlist.write("\n")
wordlist.write(last_name + middle_init + two_yob)
wordlist.write("\n")
wordlist.write(last_name + middle_init + "-" + two_yob)
wordlist.write("\n")
wordlist.write(last_name + middle_init + "-" + four_yob)
wordlist.write("\n")
wordlist.write(last_name + middle_init + "_" + two_yob)
wordlist.write("\n")
wordlist.write(last_name + middle_init + "_" + four_yob)
wordlist.write("\n")
wordlist.write(first_name + middle_init + last_name + two_yob)
wordlist.write("\n")
wordlist.write(first_name + middle_init + last_name + "-" + two_yob)
wordlist.write("\n")
wordlist.write(first_name + middle_init + last_name + "-" + four_yob)
wordlist.write("\n")
wordlist.write(first_name + middle_init + last_name + "_" + two_yob)
wordlist.write("\n")
wordlist.write(first_name + middle_init + last_name + "_" + four_yob)
wordlist.close()

print """
[+]...Wordlist Complete
\n[!]...Wordlist saved as, 'uni-user-list.txt'
##############################################################
"""
cont = raw_input("\n[!]...Press 'Return' to Continue")


