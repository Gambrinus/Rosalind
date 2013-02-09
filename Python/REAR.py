#!/usr/bin/env python

"""	Rosalind project - Problem: Reversal Distance
Problem
A reversal of a permutation creates a new permutation by inverting some interval of
the permutation; (5,2,3,1,4), (5,3,4,1,2), and (4,1,2,3,5) are all reversals of (5,3,2,1,4).
The reversal distance between two permutations p and s, written drev(p,s), is the minimum
number of reversals required to transform p into s (this assumes that p and s have the same
length).

Given: A collection of at most 5 pairs of permutations, all of which have length 10.
Return: The reversal distance between each permutation pair.

Sample Dataset
1 2 3 4 5 6 7 8 9 10
3 1 5 2 7 4 9 6 10 8

3 10 8 2 5 4 7 1 6 9
5 2 3 1 7 4 10 8 6 9

8 6 7 9 4 1 3 10 2 5
8 2 7 6 9 1 5 3 10 4

3 9 10 4 1 8 6 7 5 2
2 9 8 5 1 7 3 4 6 10

1 2 3 4 5 6 7 8 9 10
1 2 3 4 5 6 7 8 9 10
Sample Output
9 4 5 7 0

Hint
Don't be afraid to try an ugly solution.
"""

__author__ = "Daniel J. Barnes"
__email__ = "ghen2000@gmail.com"
__status__ = "Working"
                                                                                          
import random

def forward_reversal(pattern,test,j):
	k = test.find(pattern[j])+1
	test = test[:j]+test[j:k][::-1]+test[k:]
	return pattern,test

def reversals(perm):
	
	nums = []
	for x in range(0,100):
		altfirst,altsecond = str(''.join(x for x in perm[0].split())),str(''.join(x for x in perm[1].split()))
		altfirst,altsecond = altfirst.replace('10','0'),altsecond.replace('10','0')
		num=0
		j=0
		i=0
		while j<10:
			y = random.randint(1,2)
			if altfirst == altsecond:
				nums.append(num)
				j=10
				break
			if altfirst[j] == altsecond[j]:
				j+=1
			if altfirst[::-1][i] == altsecond[::-1][i]:
				i+=1
			elif y == 1:
				altfirst,altsecond = forward_reversal(altfirst,altsecond,j)
				num+=1
			elif y == 2:
				altfirst,altsecond = forward_reversal(altfirst[::-1],altsecond[::-1],i)
				altfirst,altsecond = altfirst[::-1],altsecond[::-1]
				num+=1
	return nums
	
filename = raw_input("Enter input path: ")

filein = open(filename,'r')
fileout = open('REAR_output.txt','w')

lines = filein.read().splitlines()	#gets rid of \n at the end of each line and spilts into a list

i=1
x=1
perms=[]
for line in lines:
	if i<len(lines):
		if line and lines[i]:
			perms.append([line,lines[i]])
		i+=1

nums=[]
for perm in perms:
	nums.append(reversals(perm))

out = ''
for num in nums:
	out += ' ' + str(min(num))
print out.lstrip()
fileout.write(out.lstrip())