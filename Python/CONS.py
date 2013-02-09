#!/usr/bin/env python

"""	Rosalind project - Problem: CONS
A matrix is a rectangular table of values divided into rows and columns. An mxn matrix
has m rows and n columns. Given a matrix A, we write Ai,j to indicate the value found at
the intersection of row i and column j.
Say that we have a collection of DNA strings, all having the same length n. Their profile
matrix is a 4xn matrix P in which P1,j represents the number of times that 'A' occurs in
the jth position of one of the strings, P2,j represents the number of times that C occurs
in the jth position, and so on (see below).
A consensus string c is a string of length n formed from our collection by taking the most
common symbol at each position; the jth symbol of c therefore corresponds to the symbol
having the maximum value in the j-th column of the profile matrix. Of course, there may be
more than one most common symbol, leading to multiple possible consensus strings.
DNA Strings :	A T C C A G C T
				G G G C A A C T
				A T G G A T C T
				A A G C A A C C
				T T G G A A C T
				A T G C C A T T
				A T G G C A C T
				
Profile:		A   5 1 0 0 5 5 0 0
				C   0 0 1 4 2 0 6 1
				G   1 1 6 3 0 1 0 0
				T   1 5 0 0 0 1 1 6
Consensus	A T G C A A C T

Given: A collection of at most 10 DNA strings of equal length (at most 1 kbp).
Return: A consensus string and profile matrix for the collection. (If several possible consensus string
exist, then you may return any one of them.)

Sample Dataset:
ATCCAGCT
GGGCAACT
ATGGATCT
AAGCAACC
TTGGAACT
ATGCCATT
ATGGCACT
Sample Output:
ATGCAACT
A: 5 1 0 0 5 5 0 0
C: 0 0 1 4 2 0 6 1
G: 1 1 6 3 0 1 0 0
T: 1 5 0 0 0 1 1 6
"""

__author__ = "Daniel J. Barnes"
__email__ = "ghen2000@gmail.com"
__status__ = "Working"

import re

filename = raw_input("Enter input path: ")

filein = open(filename,'r')
fileout = open('CONS_output.txt','w')

lines = filein.readlines()

seqs = []
for line in lines:
    line = line.rstrip()
    seqs.append(line)


transseq =  [[row[i] for row in seqs] for i in range(len(seqs[0]))]

a = []
c = []
g = []
t = []
cons = ''
for pos in transseq:
    a.append(pos.count('A'))
    c.append(pos.count('C'))
    g.append(pos.count('G'))
    t.append(pos.count('T'))

    counta = pos.count('A')
    countc = pos.count('C')
    countg = pos.count('G')
    countt = pos.count('T')

    if counta == max(counta,countc,countg,countt):
	cons += 'A'
    elif countc == max(counta,countc,countg,countt):
	cons += 'C'
    elif countg == max(counta,countc,countg,countt):
	cons += 'G'
    elif countt == max(counta,countc,countg,countt):
	cons += 'T'

astr = 'A:'
cstr = 'C:'
gstr = 'G:'
tstr = 'T:'

for x in a:
    astr = astr + ' ' + str(x)
for x in c:
    cstr = cstr + ' ' + str(x)
for x in g:
    gstr = gstr + ' ' + str(x)
for x in t:
    tstr = tstr + ' ' + str(x)

print cons
print astr
print cstr
print gstr
print tstr

cons += '\n'
astr += '\n'
cstr += '\n'
gstr += '\n'

fileout.write(cons)
fileout.write(astr)
fileout.write(cstr)
fileout.write(gstr)
fileout.write(tstr)