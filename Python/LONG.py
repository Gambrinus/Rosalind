#!/usr/bin/env python

"""	Rosalind project - Problem: Genome Assembly as Shortest Superstring
	Problem
	Given a collection of strings, a larger string containing every one of the smaller strings
	as a substring is called a superstring.
	By the assumption of parsimony, a shortest possible superstring over a collection of reads
	serves as a candidate chromosome.
	
	Given: At most 50 DNA strings of equal length not exceeding 1 kbp (which represent reads
	deriving from the same strand of a single linear chromosome).
	The dataset is guaranteed to satisfy the following condition: there exists a unique way to
	reconstruct the entire chromosome from these reads by gluing together pairs of reads that
	overlap by more than half their length.
	Return: A shortest superstring containing all the given strings (thus corresponding to a
	reconstructed chromosome).
	
	Sample Dataset
	ATTAGACCTG
	CCTGCCGGAA
	AGACCTGCCG
	GCCGGAATAC
	Sample Output
	ATTAGACCTGCCGGAATAC
	
	Extra Information:
	Although the goal of fragment assembly is to produce an entire genome, in practice it is only
	possible to construct several contiguous portions of each chromosome, called contigs.
	Furthermore, the assumption made above that reads all derive from the same strand is also
	practically unrealistic; in reality, researchers will not know the strand of DNA from which
	a given read has been sequenced.
"""

__author__ = "Daniel J. Barnes"
__email__ = "ghen2000@gmail.com"
__status__ = "Working"

import re

def combine(first,second):	#combines the first and second string at an overlap where first ends and second begins
	subset = 0
	for i in xrange(min(len(first),len(second))/2, 1+min(len(first),len(second))):	#sets i to iterate through 1 + half the length of shorter string
														#needs to be +1 because [x:y] splits between x and y-1
		beg = second[:i]		#makes a fragment of the beggining of of the second strand that is i long
		end = first[-i:]			#same for the end of first
		if end == beg:			#if the end and beginning match,
			subset = i			#the overlap is i in length
	return first + second[subset:]	#so, return the first concatenated to the second with i chars removed form the beginning

filename = raw_input("Enter input path: ")

filein = open(filename,'r')
fileout = open('LONG_output.txt','w')

lines = filein.read().splitlines()	#gets rid of \n at the end of each line and spilts into a list

while len(lines) > 1:	#if lines = 1 we are done
	firsthalf = {}
	lasthalf = {}
	for seq in lines:
		firsthalf[seq] = seq[:(len(seq)/2)]	#making a dict of all seqs and their first halves
		lasthalf[seq] = seq[(len(seq)/2):]	#likewise for second halves
	match = {}
	for key in firsthalf:
		match[key] = False				#initialize match with false defs
	for firstkey in firsthalf:
		if match[firstkey] == False:	#so we can check them hear
			for lastkey in lasthalf:
				if firstkey != lastkey:		#make sure we aren't matching the same seq
					if firstkey.count(lasthalf[lastkey]):	#if the first seq contains the last half of last seq
						match[firstkey] = lastkey			#we have a match, so we add both seqs to a dict
		if match[firstkey] == False:
			del match[firstkey]			#removes dict key for which there was no match (speeds things up)
	del lines[0:len(lines)]				#clearing lines in place so we can add the combined seqs to it
	for key in match:
		combined = combine(match[key],key) #combining the lines
		if combined:
			print len(combined)
			lines.append(combined)
	print '**',len(lines),'**'
	
for seq in lines:
	print seq
	fileout.write(seq)