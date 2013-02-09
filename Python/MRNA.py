#!/usr/bin/env python

"""	Rosalind project - Problem: Inferring mRNA from Protein
	Problem
	
	Given: A protein string of length at most 50 aa.
	Return: The total number of different RNA strings from which the protein could have been translated.
	
	Sample Dataset
	MA
	Sample Output
	12
	
	Hint:
	Don't forget about the importance of the stop codon to protein translation.
	
	Codon Table:
	UUU F      CUU L      AUU I      GUU V
	UUC F      CUC L      AUC I      GUC V
	UUA L      CUA L      AUA I      GUA V
	UUG L      CUG L      AUG M      GUG V
	UCU S      CCU P      ACU T      GCU A
	UCC S      CCC P      ACC T      GCC A
	UCA S      CCA P      ACA T      GCA A
	UCG S      CCG P      ACG T      GCG A
	UAU Y      CAU H      AAU N      GAU D
	UAC Y      CAC H      AAC N      GAC D
	UAA Stop   CAA Q      AAA K      GAA E
	UAG Stop   CAG Q      AAG K      GAG E
	UGU C      CGU R      AGU S      GGU G
	UGC C      CGC R      AGC S      GGC G
	UGA Stop   CGA R      AGA R      GGA G
	UGG W      CGG R      AGG R      GGG G 
"""

__author__ = "Daniel J. Barnes"
__email__ = "ghen2000@gmail.com"
__status__ = "Working"

filename = raw_input("Enter input path: ")

filein = open(filename,'r')
fileout = open('MRNA_output.txt','w')

lines = filein.readlines()
prot = lines[0].rstrip() + '*'

counts = {'F':2,'L':6,'S':6,'Y':2,'C':2,'W':1,'P':4,'H':2,'Q':2,'R':6,'I':3,'M':1,'T':4,'N':2,'K':2,'V':4,'A':4,'D':2,'E':2,'G':4,'*':3}

total = 1
for aa in prot:
	print aa, counts[aa]
	total = total * counts[aa]

fileout.write(str(total))
print total