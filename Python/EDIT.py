#!/usr/bin/env python

""" Rosalind project - Problem: Edit Distance
    Problem
    Given two strings s and t (of possibly different lengths), the edit distance dE(s,t) is
    the minimum number of edit operations needed to transform s into t, where an edit operation
    is defined as the substitution, insertion, or deletion of a single symbol.
    The latter two operations incorporate the case in which a contiguous interval is
    inserted into or deleted from a string; such an interval is called a gap. For the purposes
    of this problem, the insertion or deletion of a gap of length k still counts as k distinct
    edit operations.

    Given: Two protein strings s and t (each of length at most 1000 aa).
    Return: The edit distance dE(s,t).

    Sample Dataset
    PLEASANTLY
    MEANLY
    Sample Output
    5
"""

__author__ = "Daniel J. Barnes"
__email__ = "ghen2000@gmail.com"
__status__ = "Working"

def levDist(s1,s2):
    if len(s1) > len(s2):
        s1,s2 = s2,s1
    dist = range(len(s1) + 1)
    for index2,char2 in enumerate(s2):
        newdist = [index2+1]
        for index1,char1 in enumerate(s1):
            if char1 == char2:
                newdist.append(dist[index1])
            else:
                newdist.append(1 + min((dist[index1],dist[index1+1],newdist[-1])))
        dist = newdist
    return dist[-1]

filename = raw_input("Enter input path: ")

filein = open(filename,'r')
fileout = open('EDIT_output.txt','w')

lines = filein.read().splitlines()

s1,s2 = lines[0],lines[1]

out = levDist(s1,s2)
print out
fileout.write(str(out))