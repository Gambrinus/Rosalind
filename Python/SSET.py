#!/usr/bin/env python

""" Rosalind project - Problem: Enumerating Subsets
    Problem
    A set is the mathematical term for a loose collection of objects, called elements.
    Examples of sets include {the moon, the sun, Wilford Brimley} and R, the set
    containing all real numbers. We even have the empty set, represented by [] or {},
    which contains no elements at all. Two sets are equal when they contain the same
    elements. In other words, in contrast to permutations, the ordering of the elements
    of a set is unimportant (e.g., {the moon, the sun, Wilford Brimley} is equivalent
    to {Wilford Brimley, the moon, the sun}). Sets are not allowed to contain duplicate
    elements, so that {Wilford Brimley, the sun, the sun} is not a set.
    You may recognize sets from 'Overlap Graphs', where we introduced a two-element set {v,w}
    to represent an edge connecting nodes v and w.
    A set A is a subset of B if every element of A is also an element of B, and we write AU=B.
    For example, {the sun, the moon}U={the sun, the moon, Wilford Brimley}, and [] is a subset
    of every set (including itself!).
    The first natural question we can ask about subsets is: How many subsets can a given set have?

    Given: A positive integer n (n<=1000).
    Return: The total number of subsets of {1,2,...,n} modulo 1,000,000.

    Sample Dataset
    3
    Sample Output
    8

    Hint
    What does counting subsets have to do with characters and "ON"/"OFF" switches?
"""

__author__ = "Daniel J. Barnes"
__email__ = "ghen2000@gmail.com"
__status__ = "Working"

import itertools

filename = raw_input("Enter input path: ")

filein = open(filename,'r')
fileout = open('SSET_output.txt','w')

lines = filein.read().splitlines()
n = int(lines[0])
out = 2**n % 1000000
print out
fileout.write(str(out))