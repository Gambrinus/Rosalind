#!/usr/bin/env python

"""	Rosalind project - Problem: GC Content
	Problem	
	DNA strings must be labeled when they are consolidated into a database. A commonly used
	method of string labeling is called FASTA format. In this format, the string is introduced
	by a line that begins with ">", followed by some information naming and characterizing the
	string. Subsequent lines contain the string itself; the next line starting with ">" indicates
	the label of the next string.
	In Rosalind's implementation, a string in FASTA format will be labeled by the ID "Rosalind_xxxx",
	where "xxxx" denotes a four-digit code between 0000 and 9999.
	
	Given: At most 10 DNA strings in FASTA format (of length at most 1 kbp each).
	Return: The ID of the string having the highest GC-content, followed by the GC-content of that
	string. The GC-content should have a precision of at least 2 decimal places.
	
	Sample Dataset
	>Rosalind_6404
	CCTGCGGAAGATCGGCACTAGAATAGCCAGAACCGTTTCTCTGAGGCTTCCGGCCTTCCC
	TCCCACTAATAATTCTGAGG
	>Rosalind_5959
	CCATCGGTAGCGCATCCTTAGTCCAATTAAGTCCCTATCCAGGCGCTCCGCCGAAGGTCT
	ATATCCATTTGTCAGCAGACACGC
	>Rosalind_0808
	CCACCCTCGTGGTATGGCTAGGCATTCAGGAACCGGAGAACGCTTCAGACCAGCCCGGAC
	TGGGAACCTGCGGGCAGTAGGTGGAAT
	
	Sample Output
	Rosalind_0808
	60.92%
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
fileout = open('GC_output.txt','w')

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
		lineeach[i] = line.rstrip()
		i += 1
	else:
		if isinstance(lineeach[i], types.StringTypes):
			lineeach[i] = lineeach[i] + line.rstrip()
		else:
			lineeach[i] = line.rstrip()

seqdict = dictFromSequence(lineeach)

gcdict = {}
for key in iter(seqdict):
	gc = 0
	total = 0
	for letter in seqdict[key]:
		if letter in ['G','C']:
			gc += 1
		total += 1
	pergc = float(gc) / float(total) * 100
	print key,pergc
	gcdict[key] = pergc
	
maxkey = max(gcdict, key=gcdict.get)
maxid = maxkey.replace('>','')
maxgc = str(round(gcdict[maxkey],2)) + '%'

print 'Max GC:\n' , maxid
print maxgc

fileout.write(maxid)
fileout.write('\n')
fileout.write(maxgc)