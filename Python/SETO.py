#!/usr/bin/env python

""" Rosalind project - Problem: Introduction to Set Operations
	Problem
	If A and B are sets, then their union AUB is the set comprising any elements in either A or B; their
	intersection AOB is the set of elements in both A and B; and their set difference A-B is the set of
	elements in A but not in B.
	Furthermore, if A is a subset of another set U, then the set complement of A with respect to U is
	defined as the set Ac=U-A. See the Sample sections below for examples.

	Given: A positive integer n (n<=20,000) and two subsets A and B of {1,2,...,n}.
	Return: Six sets: AUB, AOB, A-B, B-A, Ac, and Bc (where set complements are taken with respect to
	{1,2,...,n}).

	Sample Dataset
	10
	{1, 2, 3, 4, 5}
	{2, 8, 5, 10}
	Sample Output
	{1, 2, 3, 4, 5, 8, 10}
	{2, 5}
	{1, 3, 4}
	{8, 10}
	{8, 9, 10, 6, 7}
	{1, 3, 4, 6, 7, 9}

	Extra Information
	From the definitions above, one can see that AUB=BUA and AOB=BOA for all sets A and B, but it is not
	necessarily the case that A-B=B-A (as seen in the Sample sections above). This set theoretical fact
	parallels the arithmetical fact that addition is commutative but subtraction is not.
"""

__author__ = "Daniel J. Barnes"
__email__ = "ghen2000@gmail.com"
__status__ = "Working"

import sys

def set_union(x,y):
	c = [z for z in x]
	for z in y:
		if z not in x:
			c.append(z)
	return c

def set_intersection(x,y):
	c = []
	for z in x:
		if z in y:
			c.append(z)
	return c

def set_diff(x,y):
	c = [z for z in x]
	for z in x:
		if z in y:
			c.remove(z)
	return c

if len(sys.argv) == 2:
	filein = open(sys.argv[1], 'r')
else:
	filein = open("test_input.txt",'r')
lines = filein.read().splitlines()
fileout = open('SETO_output.txt','w')

n = int(lines[0])
a,b = lines[1].replace('{',''),lines[2].replace('{','')
a,b = a.replace('}',''),b.replace('}','')
a,b = a.replace(',',''),b.replace(',','')
a = [int(x) for x in a.split()]
b = [int(x) for x in b.split()]
u = range(1,n+1)

union = [str(x) for x in set_union(a,b)]
print "Union complete"
intersection = [str(x) for x in set_intersection(a,b)]
print "Intersection complete"
diffab = [str(x) for x in set_diff(a,b)]
print "A-B complete"
diffba = [str(x) for x in set_diff(b,a)]
print "B-A complete"
diffua = [str(x) for x in set_diff(u,a)]
print "Ac complete"
diffub = [str(x) for x in set_diff(u,b)]
print "Bc complete"

out = '{'+', '.join(union)+'}'+'\n'+'{'+', '.join(intersection)+'}'+'\n'+\
	  '{'+', '.join(diffab)+'}'+'\n'+'{'+', '.join(diffba)+'}'+'\n'+'{'+\
	  ', '.join(diffua)+'}'+'\n'+'{'+', '.join(diffub)+'}'
fileout.write(str(out))