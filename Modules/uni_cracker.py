#!/usr/bin/python
#
#
import uni_clear

print """

Module:
                                         _
 _   _ _ __ (_)       ___ _ __ __ _  ___| | _____ _ __
| | | | '_ \| |_____ / __| '__/ _` |/ __| |/ / _ \ '__|
| |_| | | | | |_____| (__| | | (_| | (__|   <  __/ |
 \__,_|_| |_|_|      \___|_|  \__,_|\___|_|\_\___|_|

\nwhat is uni-cracker?
uni-cracker is a module
within uni-brute,
that attemps to bruteforce
the following protocols
"""

def print_menu():
    print 12 * "-" , "Supported Protocols" , 13 * "-"
    print "##############################################"
    print "  [1]. HTTP/HTTPS 'COMING SOON!'"
    print "  [2]. SMTP"
    print "  [3]. Return to Main Menu"
    print "##############################################"
    print 46 * "-"

loop=True

while loop:
    print_menu()
    choice = input("\nSelect from the following Protocols [1-3]: ")


    if choice==1:

	uni_clear.clear()
	#import Protocols.http_https
	uni_clear.clear()


    elif choice==2:

        uni_clear.clear()
	import Protocols.smtp
	uni_clear.clear()


    elif choice==3:

        loop=False


    else:

        raw_input("\n[!]-Error That was a invalid Number, Select from [1-4]")
