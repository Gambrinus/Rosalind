#!/usr/bin/env python

""" Rosalind project - Problem: Inferring Protein from Spectrum
    Problem
    The prefix spectrum of a weighted string is the collection of all its prefix weights.

    Given: A list L of n (n<=100) positive real numbers.
    Return: A protein string of length n-1 whose prefix spectrum is equal to L (if multiple
    solutions exist, you may output any one of them). Consult the monoisotopic mass table.

    Sample Dataset
    3524.8542
    3710.9335
    3841.974
    3970.0326
    4057.0646
    Sample Output
    WMQS
"""

__author__ = "Daniel J. Barnes"
__email__ = "ghen2000@gmail.com"
__status__ = "Working"

filename = raw_input("Enter input path: ")

filein = open(filename,'r')
fileout = open('SPEC_output.txt','w')

lines = filein.read().splitlines()

mmt = { 71.04:'A',103.01:'C',115.03:'D',129.04:'E',147.07:'F',57.02:'G',
        137.06:'H',113.08:'I',128.09:'K',113.08:'L',131.04:'M',114.04:'N',
        97.05:'P',128.06:'Q',156.10:'R',87.03:'S',101.05:'T',99.07:'V',
        186.08:'W',163.06:'Y' }

i = 1
prot = ''
while i < len(lines):
    dif = round(float(lines[i])-float(lines[i-1]),2)
    prot += mmt[dif]
    i += 1

print prot
fileout.write(prot)