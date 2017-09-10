#!/usr/bin/python

import os
import sys
sys.dont_write_bytecode = True

print """

                     Welcome to

  _   _ _   _ ___      ____  ____  _   _ _____ _____
 | | | | \ | |_ _|    | __ )|  _ \| | | |_   _| ____|
 | | | |  \| || |_____|  _ \| |_) | | | | | | |  _|
 | |_| | |\  || |_____| |_) |  _ <| |_| | | | | |___
  \___/|_| \_|___|    |____/|_| \_\\___/  |_| |_____|

		        AKA
	   'Universal-BruteForcing-Script'
		    version 1.17

		     {{Author}}
		    ***brut0s***
   	     https://github.com/brut0s

\nWhat is Uni-Brute?
Uni-Brute is a script
much like 'Cupp',
\nLink: 'https://github.com/Mebus/cupp'
not only does uni-brute generates
a wordlist for you, it also has the
ability to bruteforce accounts!!
"""
def print_menu():
    print 12 * "-" , "Main-Menu" , 12 * "-"
    print "###################################"
    print "  [1]. Uni-Pass "
    print "  [2]. Uni-Users"
    print "  [3]. Uni-Cracker"
    print "  [4]. Exit"
    print "###################################"
    print 35 * "-"

loop=True

while loop:
    print_menu()
    choice = input("\nSelect an Option [1-4]: ")

    if choice==1:

	import Modules.uni_clear
	import Modules.uni_pass
	import Modules.uni_clear

    elif choice==2:

	import Modules.uni_clear
	import Modules.uni_users
	import Modules.uni_clear

    elif choice==3:

	import Modules.uni_clear
        import Modules.uni_cracker
        import Modules.uni_clear

    elif choice==4:

        print "\nThanks for using Uni-Brute"
        loop=False


    else:

        raw_input("\n[!]-Error That was a invalid Number, Select from [1-4]")
