#!/usr/bin/env python

"""	Rosalind project - Problem: SUBS
    Given two strings s=s1s2...sn and t=t1t2...tm where m<=n, t is a substring
    of s if t is contained as a contiguous collection of symbols in s.
    The position of a symbol in a string is the total number of symbols found
    to its left, including itself (e.g., the positions of all occurrences of U in AUGCUUCAGAAAGGUCUUACG
    are 2, 5, 6, 15, 17, and 18). The symbol at position i of s is denoted by s[i]. For that matter, a substring of s
    can be represented as s[j:k], where j and k represent the starting and ending positions of the substring in s.
    The location of a substring is its beginning position; note that t will have multiple locations in s if it occurs
    more than once as a substring of s (see the Sample sections below).

    Given: Two DNA strings s and t (each of length at most 1 kbp).
    Return: All locations of t as a substring of s.

    Sample Dataset
    ACGTACGTACGTACGT
    GTA
    Sample Output
    3 7 11
"""

__author__ = "Daniel J. Barnes"
__email__ = "ghen2000@gmail.com"
__status__ = "Working"

import re

filename = raw_input("Enter input path:")

filein = open(filename,'r')
fileout = open('SUBS_output.txt','w')

lines = filein.readlines()

seq = lines[0].rstrip('\n')
search ='(?=' + lines[1].rstrip('\n') + ')'						#format to find overlapping string

positions = [m.start() for m in re.finditer(search, seq)]	#finds overlapping search in seq

pos = ''
for loc in positions:
    loc += 1						#init for loc is 0, switch to 1
    loc = str(loc) + ' '			#formatting
    pos += loc

fileout.write(pos.rstrip())	#strips the final \s