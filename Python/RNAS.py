#!/usr/bin/env python

""" Rosalind project - Problem: Counting RNA Secondary Structures
	Given an RNA string s=s1...sn, a bonding graph for s is formed as follows. Create one node
	for each symbol in s, and connect adjacent symbols of s with solid edges. Then, we connect
	some of the pairs {A,U}, {C,G}, and {G,U} with dashed edges under the stipulation that no
	node can be used in two different dashed edges (i.e., to model the practical fact that every
	nucleotide can base pair with at most one other nucleotide).
	A valid bonding graph has the following two additional properties:
	A dashed edge cannot connect two symbols sj and sk unless k>=j+4 (i.e., hairpin loops shorter
	than three nucleotides long, which are sterically impossible, are inadmissible).
	There cannot be two dashed edges {sj,sk} and {sj',sk'} where j<j'<k<k' (this condition prevents
	pseudoknots).
	See Figure 3 for two equivalent valid bonding graphs encoding the same secondary structure for
	a given strand of RNA.

	Given: An RNA string s (of length at most 200 bp).
	Return: The total number of distinct valid bonding graphs for s.

	Sample Dataset
	AUGCUAGUACGGAGCGAGUCUAGCGAGCGAUGUCGUGAGUACUAUAUAUGCGCAUAAGCCACGU
	Sample Output
	284850219977421
"""

__author__ = "Daniel J. Barnes"
__email__ = "ghen2000@gmail.com"
__status__ = "Working"

import sys

class bonding_graphs():
    
    def __init__(memo,rna):
        memo.rna = rna
        memo.results = {}
        memo.count = memo.struc(0, len(memo.rna) - 1)

    def struc(memo,i,j):
        bonds = {'A':['U'],'C':['G'],'G':['C','U'],'U':['A','G']}
        if (i, j) in memo.results:
        	return memo.results[(i,j)]	# results already calculated so return them
        else:
			if j < i+4:	# hairpins must be larger than 3 nucleotides
			    n = 1		# so if it's shorter, only add 1 and stop counting
			else:
			    n = 0
			    base1 = memo.rna[i]
			    for k in range(i+4,j+1):	# range of all possible bonding pairs
			        base2 = memo.rna[k]
			        if base2 in bonds[base1]:			# check for base pairing
			            inside = memo.struc(i+1,k-1)	# count all pairing within the range
			            if k < j:
			                outside = memo.struc(k+1,j)	# count all pairing outside range
			            else:
			                outside = 1						# if there is no outside range, then it's just 1
			            n += inside * outside
			    n += memo.struc(i+1,j) 	# advance i one base to continue count
			memo.results[(i,j)] = n 	# store the count
			return n

if sys.argv[1] == "-i":
	filein = open(sys.argv[2], 'r')
	lines = filein.read().splitlines()
	filein.close
	seq = lines[0]
else:
	seq = sys.argv[1]

fileout = open('RNAS_output.txt','w')

out = str(bonding_graphs(seq).count)

fileout.write(out)						# writes to file, closes file, and rereads file
fileout.close 							# to make sure the output is correct in the file
fileout = open('RNAS_output.txt','r')
print fileout.read()
fileout.close