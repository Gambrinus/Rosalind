#!/usr/bin/env python

"""	Rosalind project - Problem: Overlap Graphs
	Problem
	A graph whose nodes have all been labeled can be represented by an adjacency list,
	in which each row of the list contains the two node labels corresponding to a unique edge.
	A directed graph (or digraph) is a graph containing directed edges, each of which
	has an orientation. That is, a directed edge is represented by an arrow instead of
	simply a segment; the starting and ending nodes of an edge form its tail and head,
	respectively. The directed edge with tail v and head w is represented by (v,w) (but not
	by (w,v)). A directed loop is a directed edge of the form (v,v).
	For a collection of strings and a positive integer k, the overlap graph for the strings
	is a directed graph Ok in which each string is represented by a node, and string s is connected
	to string t with a directed edge if and only if there is a length k suffix of s that matches
	a length k prefix of t. Directed loops are not allowed in the overlap graph.
	
	Given: A collection of DNA strings in FASTA format having total length at most 10 kbp.
	Return: The adjacency list corresponding to O3.
	
	Sample Dataset
	>Rosalind_0498
	AAATAAA
	>Rosalind_2391
	AAATTTT
	>Rosalind_2323
	TTTTCCC
	>Rosalind_0442
	AAATCCC
	>Rosalind_5013
	GGGTGGG
	Sample Output
	Rosalind_0498 Rosalind_2391
	Rosalind_0498 Rosalind_0442
	Rosalind_2391 Rosalind_2323
"""

__author__ = "Daniel J. Barnes"
__email__ = "ghen2000@gmail.com"
__status__ = "Working"

import types
import re

def pairwise(iterable):
    itnext = iter(iterable).next
    while True:
        yield itnext( ), itnext( )
        
def dictFromSequence(seq):
    return dict(pairwise(seq))

filename = raw_input("Enter input path: ")

filein = open(filename,'r')
fileout = open('GRPH_output.txt','w')

lines = filein.readlines()

seqnum = 0
for line in lines:
	if line.count('>'):
		seqnum += 1

lineeach = [str]*(seqnum *2)

i = 0
for line in lines:
	if line.count('>'):
		if i > 0:
			i += 1
		line = line.replace('>','')
		lineeach[i] = line.rstrip()
		i += 1
	else:
		if isinstance(lineeach[i], types.StringTypes):
			lineeach[i] = lineeach[i] + line.rstrip()
		else:
			lineeach[i] = line.rstrip()

seqdict = dictFromSequence(lineeach)

first = {}
last = {}
for key in iter(seqdict):
	seq = seqdict[key]
	lastthree = seq[-3] + seq[-2] + seq[-1]
	firstthree = seq[0] + seq [1] + seq[2]
	first[key] = firstthree
	last[key] = lastthree

for key1 in last:
	for key2 in first:
		if key1 != key2:
			if first[key2] == last[key1]:
				output = key1 + ' ' + key2 + '\n'
				print key1 , key2
				fileout.write(output)