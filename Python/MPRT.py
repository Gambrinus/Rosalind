#!/usr/bin/env python

""" Rosalind project - Problem: Finding a Protein Motif
Problem
To allow for the presence of its varying forms, a protein motif is represented by a shorthand as
follows: [XY] means "either X or Y" and {X} means "any amino acid except X." For example, the
N-glycosylation motif is written as N{P}[ST]{P}.
You can see the complete description and features of a particular protein by its access ID
"uniprot_id" in the UniProt database, by inserting the ID number into
http://www.uniprot.org/uniprot/uniprot_id
Alternatively, you can obtain a protein sequence in FASTA format by following
http://www.uniprot.org/uniprot/uniprot_id.fasta
For example, the data for protein B5ZC00 can be found at http://www.uniprot.org/uniprot/B5ZC00.

Given: At most 15 UniProt Protein Database access IDs.
Return: For each protein possessing the N-glycosylation motif, output its given access ID followed
by a list of locations in the protein string where the motif can be found.

Sample Dataset
A2Z669
B5ZC00
P07204_TRBM_HUMAN
P20840_SAG1_YEAST
Sample Output
B5ZC00
85 118 142 306 395
P07204_TRBM_HUMAN
47 115 116 382 409
P20840_SAG1_YEAST
79 109 135 248 306 348 364 402 485 501 614

Note
Some entries in UniProt have one primary (citable) accession number and some secondary numbers,
appearing due to merging or demerging entries. In this problem, you may be given any type of ID.
If you type the secondary ID into the UniProt query, then you will be automatically redirected
to the page containing the primary ID. You can find more information about UniProt IDs here.
"""

__author__ = "Daniel J. Barnes"
__email__ = "ghen2000@gmail.com"
__status__ = "Working"

import sys
import urllib2
import re

def fetch_uniprot_seq(uniprot_id):
	url = 'http://www.uniprot.org/uniprot/' + uniprot_id + '.fasta'
	web_file = urllib2.urlopen(url).read().splitlines()
	web_file.pop(0)
	return ''.join(web_file)

def motif_positions(seq):
	positions = [str(m.start()+1) for m in re.finditer('(?=N[ARNDBCQEZGHILKMFSTWYV][ST][ARNDBCQEZGHILKMFSTWYV])', seq)]
	return ' '.join(positions)

if len(sys.argv) >= 3 and sys.argv[1] == "-i":
	filein = open(sys.argv[2], 'r')
	lines = filein.read().splitlines()
	filein.close
else:
	filein = open('rosalind_mprt.txt', 'r')
	lines = filein.read().splitlines()
	filein.close

out = ''
for id in lines:
	seq = fetch_uniprot_seq(id)
	pos = motif_positions(seq)
	if pos:
		if out:
			out += '\n' + id + '\n' + pos
		else:
			out += id + '\n' + pos

fileout = open('MPRT_output.txt','w')
fileout.write(out)						# writes to file, closes file, and rereads file
fileout.close 							# to make sure the output is correct in the file
fileout = open('MPRT_output.txt','r')
print fileout.read()
fileout.close