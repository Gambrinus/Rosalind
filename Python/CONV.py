#!/usr/bin/env python

""" Rosalind project - Problem: Comparing Spectra with the Spectral Convolution
    Problem
    A multiset is a generalization of the notion of set to include a collection of objects in which
    each object may occur more than once (the order in which objects are given is still unimportant).
    For a multiset S, the multiplicity of an element x is the number of times that x occurs in the set;
    this multiplicity is denoted S(x). Note that every set is included in the definition of multiset.
    The Minkowski sum of multisets S1 and S2 containing real numbers is the new multiset S1+S2 formed by
    taking all possible sums s1+s2 of an element s1 from S1 and an element s2 from S2. The Minkowski sum
    could be defined more concisely as S1+S2=s1+s2:s1ES1,s2ES2, The Minkowski difference S1-S2 is defined
    analogously by taking all possible differences s1-s2.
    If S1 and S2 represent simplified spectra taken from two peptides, then S1-S2 is called the spectral
    convolution of S1 and S2. In this notation, the shared peaks count is represented by (S2-S1)(0), and
    the value of x for which (S2-S1)(x) has the maximal value is the shift value maximizing the number
    of shared masses of S1 and S2.

    Given: Two multisets of positive real numbers S1 and S2. The size of each multiset is at most 200.
    Return: The largest multiplicity of S1-S2, as well as the absolute value of the number x maximizing
    (S1-S2)(x) (you may return any such value if multiple solutions exist).

    Sample Dataset
    186.07931 287.12699 548.20532 580.18077 681.22845 706.27446 782.27613 968.35544 968.35544
    101.04768 158.06914 202.09536 318.09979 419.14747 463.17369
    Sample Output
    3
    85.03163

    Note
    Observe that S1xS2 is equivalent to S2+S1, but it is not usually the case that S1-S2 is the same as
    S2-S1; in this case, one multiset can be obtained from the other by negating every element.
"""

__author__ = "Daniel J. Barnes"
__email__ = "ghen2000@gmail.com"
__status__ = "Working"

import operator

filename = raw_input("Enter input path: ")

filein = open(filename,'r')
fileout = open('CONV_output.txt','w')

lines = filein.read().splitlines()

s1 = lines[0].split()
s2 = lines[1].split()

multi = []
for x in s1:
    for y in s2:
        z = round(float(x) - float(y),5)
        multi.append(z)

multi = sorted(multi)
multiset = sorted(set(multi))

occurences = {}
for x in multiset:
    occurences[float(x)] = 0
    for y in multi:
        if y > x:
            break
        if float(x) == float(y):
            occurences[float(x)] += 1

maxkey = max(occurences.iteritems(), key=operator.itemgetter(1))[0]
out = str(occurences[maxkey])+'\n'+str(maxkey)
print out
fileout.write(out)