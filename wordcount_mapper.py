#!/usr/bin/env python
#the above just indicates to use python to intepret this file
# ---------------------------------------------------------------
#This mapper code will input a line of text and output <word, 1>
#
# ---------------------------------------------------------------
import sys #a python module with system functions for this O
for  line  in  sys.stdin:
	line  =  line.strip()
	keys = line.split() #split line at blanks (by default),
# and return a list of keys
	for key in keys: #a for loop through the list of keys
		value = 1
		print('{0}\t{1}'.format(key, value) )
