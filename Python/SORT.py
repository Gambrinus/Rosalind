#!/usr/bin/env python

""" Rosalind project - Problem: Sorting on Reversals
    Problem
    A reversal of a permutation can be encoded by the two indices at the endpoints of
    the interval that it inverts; for example, the reversal that transforms (4,1,2,6,3,5)
    into (4,1,3,6,2,5) is encoded by [3,5].
    A collection of reversals sorts p into g if the collection contains drev(p,g) reversals,
    which when successively applied to p yield g.

    Given: Two permutations p and g, each of length 10.
    Return: The reversal distance drev(p,g), followed by a collection of reversals sorting p into g.

    Sample Dataset
    1 2 3 4 5 6 7 8 9 10
    1 2 3 4 10 9 7 8 6 5

    Sample Output
    2
    5 10
    7 8
"""

__author__ = "Daniel J. Barnes"
__email__ = "ghen2000@gmail.com"
__status__ = "Working"

import os
import re

def call_grimm(seq1, seq2):
    #uses grimm (http://grimm.ucsd.edu/GRIMM/) to analyze reversals
    tmp = open("_grimm_tmp.txt", "w")
    tmp.write(">seq1\n")
    tmp.write(seq1 + " $\n")
    tmp.write(">seq2\n")
    tmp.write(seq2 + " $\n")
    tmp.close()
    os.system("grimm -f _grimm_tmp.txt -u -L -o _grimm_res.txt")
    tmp = open("_grimm_res.txt", "r")
    result = tmp.readlines()
    tmp.close
    os.remove("_grimm_tmp.txt")
    os.remove("_grimm_res.txt")
    ret = []
    for x in result:
        matchObj = re.search("Reversal Distance:\s*([0-9])",x)
        if matchObj:
            ret.append(matchObj.group(1))
        matches = re.findall("gene [0-9]",x)
        if matches:
            matches[0] = matches[0].replace('gene ','')
            matches[1] = matches[1].replace('gene ','')
            matches[0] = int(matches[0]) + 1
            matches[1] = int(matches[1]) + 1
            line = str(matches[0])+" "+str(matches[1])
            ret.append(line)
    return ret

filename = raw_input("Enter input path: ")

filein = open(filename,'r')
fileout = open('SORT_output.txt','w')

lines = filein.read().splitlines()  #gets rid of \n at the end of each line and spilts into a list

revlist = call_grimm(lines[0],lines[1])

out = '\n'.join(revlist)

print out
fileout.write(out)