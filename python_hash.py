#!/usr/bin/python
#Author: Drew Ballantine
#Date: 2016-11-01
#Description: A python script that prompts the user for a password and returns the Salted SHA-512 Hash.

import sys
import crypt
import getpass

option = 0

while option != 1 and option !=2 and option !=3:
    option = input('Please select what encryption level you would like:\n1. SHA512\n2. SHA256\n3. MD5\nOption: ')

    if option == 1:
        password = getpass.getpass("Please enter the password you wish to hash: ")
        print(crypt.crypt(str(password), crypt.mksalt(crypt.METHOD_SHA512)))
    elif option == 2:
        password = getpass.getpass("Please enter the password you wish to hash: ")
        print(crypt.crypt(str(password), crypt.mksalt(crypt.METHOD_SHA256)))
    elif option == 3:
        password = getpass.getpass("Please enter the password you wish to hash: ")
        print(crypt.crypt(str(password), crypt.mksalt(crypt.METHOD_MD5)))
    else:
        print "Please enter 1, 2 or 3"
