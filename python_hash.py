#!/usr/bin/python
#Author: Drew Ballantine
#Date: 2016-11-01
#Description: A python script that prompts the user for a password and returns the Salted SHA-512 Hash.

import sys
import crypt
import getpass
password = getpass.getpass("Please enter the password you wish to hash: ")

print(crypt.crypt(str(password), crypt.mksalt(crypt.METHOD_SHA512)))
