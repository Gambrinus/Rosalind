#!/usr/bin/env python

"""	Rosalind project - Problem: Error Correction in Reads
	Problem
	Given a finite collection of events x1,x2,...,xn, where xi has probability pi,
	the expected value for the number of events xi occurring is given by p1+p2+...+pn.
	
	Given: A positive integer m (m<=10), a positive integer n (n<=10,000), and an array
	A of length at most 20 containing real numbers between 0 and 1, inclusively.
	Return: An array B in which B[i] represents the expected number of substring matches
	of a random string of length m inside a random string of length n, where both are
	formed from GC-content A[i] (see Introduction to Probability). Each value in B should
	have a precision of at least three decimal places.
	
	Sample Dataset
	2 10
	0.32 0.42 0.81
	Sample Output
	0.717748 0.591669 1.078067
	
	Hints
	
	How can we use our solution from Introduction to Probability?
	Let xi be the event that t=s[i:i+m-1].
"""

__author__ = "Daniel J. Barnes"
__email__ = "ghen2000@gmail.com"
__status__ = "Working"

def prob(gc,m,n):
	probgc = (gc/2)**2			#prob of matching G or C
	probat = ((1-gc)/2)**2		#prob of matching A or T
	return float((2*probat+2*probgc)**m)*(n-(m-1))	#return combined prob of matching A,T,G, or C in an m-mer within a
													#string of n length (n-(m-1)) is the number of potential substrings of m length

filename = raw_input("Enter input path: ")

filein = open(filename,'r')
fileout = open('EVAL_output.txt','w')

lines = filein.read().splitlines()

mn = lines.pop(0)
m,n = mn.split()
gc = lines[0].split()

out = ''
for x in gc:
	print prob(float(x),int(m),int(n))
	
	out += str(prob(float(x),int(m),int(n))) + ' '
	
fileout.write(out.rstrip())