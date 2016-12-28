#!/usr/bin/python
#Author: Drew Ballantine
#Date: 2016-11-01
#Description: A python script that prompts the user for a password and returns the Salted SHA-512 Hash.

import sys
import crypt
import getpass

option = 0

while option != 1 or option !=2 or option !=3 or option !=4 or option !=5 or option !=6:
    option = input('Please select what encryption level you would like:\n1. SHA512\n2. SHA256\n3. SHA128\n4. SHA2\n 5. SHA1\n 6. MD5 ')

    if option = 1:
        password = getpass.getpass("Please enter the password you wish to hash: ")
        print(crypt.crypt(str(password), crypt.mksalt(crypt.METHOD_SHA512)))
    elif option = 2:
        password = getpass.getpass("Please enter the password you wish to hash: ")
        print(crypt.crypt(str(password), crypt.mksalt(crypt.METHOD_SHA256)))
    elif option = 3:
        password = getpass.getpass("Please enter the password you wish to hash: ")
        print(crypt.crypt(str(password), crypt.mksalt(crypt.METHOD_SHA128)))
    elif option = 4:
        password = getpass.getpass("Please enter the password you wish to hash: ")
        print(crypt.crypt(str(password), crypt.mksalt(crypt.METHOD_SHA2)))
    elif option = 5:
        password = getpass.getpass("Please enter the password you wish to hash: ")
        print(crypt.crypt(str(password), crypt.mksalt(crypt.METHOD_SHA1)))
    elif option = 6:
        password = getpass.getpass("Please enter the password you wish to hash: ")
        print(crypt.crypt(str(password), crypt.mksalt(crypt.METHOD_MD5)))
    else:
        print "Please enter 1 through 6"
