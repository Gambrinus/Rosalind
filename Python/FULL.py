#!/usr/bin/env python

""" Rosalind project - Problem: Inferring Peptide from Full Spectrum
    Problem
    Say that we have a string s containing t as an internal substring, so that there exist nonempty
    substrings s1 and s2 of s such that s can be written as s1ts2. A t-prefix contains all of s1 and
    none of s2; likewise, a t-suffix contains all of s2 and none of s1.

    Given: A list L containing 2n+3 positive real numbers (n<=100). The first number in L is the parent
    mass of a peptide P, and all other numbers represent the masses of some b-ions and y-ions of P
    (in no particular order). You may assume that if the mass of a b-ion is present, then so is that
    of its complementary y-ion, and vice-versa.
    Return: A protein string t of length n for which there exist two positive real numbers w1 and w2
    such that for every prefix p and suffix s of t, each of w(p)+w1 and w(s)+w2 is equal to an element
    of L. (In other words, there exists a protein string whose t-prefix and t-suffix weights correspond
    to the non-parent mass values of L.) If multiple solutions exist, you may output any one.

    Sample Dataset
    1988.21104821
    610.391039105
    738.485999105
    766.492149105
    863.544909105
    867.528589105
    992.587499105
    995.623549105
    1120.6824591
    1124.6661391
    1221.7188991
    1249.7250491
    1377.8200091
    Sample Output
    KEKEP
"""

__author__ = "Daniel J. Barnes"
__email__ = "ghen2000@gmail.com"
__status__ = "Working"

filename = raw_input("Enter input path: ")

filein = open(filename,'r')
fileout = open('FULL_output.txt','w')

lines = filein.read().splitlines()

mmt = { 71.04:'A',103.01:'C',115.03:'D',129.04:'E',147.07:'F',57.02:'G',
        137.06:'H',113.08:'I',128.09:'K',113.08:'L',131.04:'M',114.04:'N',
        97.05:'P',128.06:'Q',156.10:'R',87.03:'S',101.05:'T',99.07:'V',
        186.08:'W',163.06:'Y' }

n = (len(lines)-3)/2
full = float(lines[0])
lines.remove(lines[0])

suf = []
prot = ''
for x in lines:
    z=0
    for y in lines:
        dif = round(float(y)-float(x),2)
        if x in suf or x == lines[0]:
            if dif in mmt.keys():
                print x,y,dif,mmt[dif]
                if len(prot) < n:
                    prot += mmt[dif]
                suf.append(y)
                z = 1
            if z:
                break

print prot
fileout.write(prot)