#!/usr/bin/env python

"""	Rosalind project - Problem: Calculating Protein Mass
In a weighted alphabet, every symbol is assigned a positive real number called a weight.
A string formed from a weighted alphabet is called a weighted string, and its weight is
equal to the sum of the weights of its symbols.

The standard weight assigned to each member of the 20-symbol amino acid alphabet is
the monoisotopic mass of the corresponding amino acid.

Given: A protein string P of length at most 1000 aa.
Return: The weight of P to an accuracy of two decimal places. Consult the monoisotopic mass table.

Sample Dataset
SKADYEK
Sample Output
821.39

Monoisotopic mass table:
A   71.03711
C   103.00919
D   115.02694
E   129.04259
F   147.06841
G   57.02146
H   137.05891
I   113.08406
K   128.09496
L   113.08406
M   131.04049
N   114.04293
P   97.05276
Q   128.05858
R   156.10111
S   87.03203
T   101.04768
V   99.06841
W   186.07931
Y   163.06333
"""

__author__ = "Daniel J. Barnes"
__email__ = "ghen2000@gmail.com"
__status__ = "Working"

filename = raw_input("Enter input path: ")

filein = open(filename,'r')
fileout = open('PRTM_output.txt','w')

lines = filein.readlines()

mmt = {	'A':71.03711,'C':103.00919,'D':115.02694,'E':129.04259,'F':147.06841,'G':57.02146,'H':137.05891,
		'I':113.08406,'K':128.09496,'L':113.08406,'M':131.04049,'N':114.04293,'P':97.05276,'Q':128.05858,
		'R':156.10111,'S':87.03203,'T':101.04768,'V':99.06841,'W':186.07931,'Y':163.06333	}

mass = 0
for aa in lines[0].rstrip():
	mass += mmt[aa]
	
print round(mass,2)
fileout.write(str(round(mass,2)))