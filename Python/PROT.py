#!/usr/bin/env python

"""	Rosalind project - Problem: PROT
    The 20 commonly occurring amino acids are abbreviated by using the majority of symbols from the Roman alphabet (except for B, J, O, U, X, and Z). Protein strings are constructed from these 20 symbols. Henceforth, the term genetic string will incorporate protein strings with DNA strings and RNA strings.
    The RNA codon table dictates specific details regarding the encoding of specific codons into the amino acid alphabet.

    Given: An RNA string s corresponding to a strand of mRNA (of length at most 10 knt).
    Return: The protein string encoded by s.

    Sample Dataset
    AUGGCCAUGGCGCCCAGAACUGAGAUCAAUAGUACCCGUAUUAACGGGUGA
    Sample Output
    MAMAPRTEINSTRING
"""

__author__ = "Daniel J. Barnes"
__email__ = "ghen2000@gmail.com"
__status__ = "Working"

def split(str, num):
    return [ str[start:start+num] for start in range(0, len(str), num) ] 	#cut the string up into 'num' length fragments

filename = raw_input("Enter input path:")

filein = open(filename,'r')
fileout = open('PROT_output.txt','w')

seq = filein.read()

triplets = split(seq,3)	#use split to make the codons

prot = ''
for codon in triplets:
    codon = codon.upper()
    if codon in ['UUU','UUC']:
	prot+='F'
    if codon in ['UUA','UUG','CUU','CUC','CUA','CUG']:
	prot+='L'
    if codon in ['UCU','UCC','UCA','UCG','AGU','AGC']:
	prot+='S'
    if codon in ['UAU','UAC']:
	prot+='Y'
    if codon in ['UGU','UGC']:
	prot+='C'
    if codon in ['UGG']:
	prot+='W'
    if codon in ['CCU','CCC','CCA','CCG']:
	prot+='P'
    if codon in ['CAU','CAC']:
	prot+='H'
    if codon in ['CAA','CAG']:
	prot+='Q'
    if codon in ['CGU','CGC','CGA','CGG','AGA','AGG']:
	prot+='R'
    if codon in ['AUU','AUC','AUA']:
	prot+='I'
    if codon in ['AUG']:
	prot+='M'
    if codon in ['ACU','ACC','ACA','ACG']:
	prot+='T'
    if codon in ['AAU','AAC']:
	prot+='N'
    if codon in ['AAA','AAG']:
	prot+='K'
    if codon in ['GUU','GUC','GUA','GUG']:
	prot+='V'
    if codon in ['GCU','GCC','GCA','GCG']:
	prot+='A'
    if codon in ['GAU','GAC']:
	prot+='D'
    if codon in ['GAA','GAG']:
	prot+='E'
    if codon in ['GGU','GGC','GGA','GGG']:
	prot+='G'
    if codon in ['UAA','UAG','UGA']:
	prot+='*'

fileout.write(prot.split("*")[0])