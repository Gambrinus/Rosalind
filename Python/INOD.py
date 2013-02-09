#!/usr/bin/env python

"""	Rosalind project - Problem: Counting Phylogenetic Ancestors
	Problem
	A binary tree is a tree in which each node has degree equal to at most 3. The binary
	tree will be our main tool in the construction of phylogenies.
	A rooted tree is a tree in which one node (the root) is set aside to serve as the
	pinnacle of the tree. A standard graph theory exercise is to demonstrate that there
	is exactly one path connecting any two nodes of a tree. In a rooted tree, every node
	v will therefore have a single parent, or the unique node w such that the path from v
	to the root contains {v,w}. Any other node x adjacent to v is called a child of v
	because v must be the parent of x; note that a node may have multiple children. A
	rooted tree therefore possesses an ordered hierarchy from the root down to its leaves.
	An unrooted binary tree is an unrooted tree in which all internal nodes have degree 3.
	A rooted binary tree is a rooted tree in which only the root has degree 2 (all other
	nodes have degree 1 or 3).

	Given: A positive integer n (3<=n<=10000).
	Return: The number of internal nodes of any unrooted binary tree having n leaves.
	
	Sample Dataset
	4
	Sample Output
	2

	Hint
	In solving 'Completing a Tree', you may have formed the conjecture that a graph
	with no cycles and n nodes is a tree precisely when it has n-1 edges. This is indeed
	a theorem of graph theory.
"""

__author__ = "Daniel J. Barnes"
__email__ = "ghen2000@gmail.com"
__status__ = "Working"

filename = raw_input("Enter input path: ")

filein = open(filename,'r')
fileout = open('INOD_output.txt','w')

lines = filein.read().splitlines()

leaves = lines[0]

root = 1	#there is always 1 root node

intnodes = int(leaves) - 1	#graph theory, an unrooted binary tree has leaves - 1 internal nodes
intnodes = intnodes - root	#have to account of the root node which is not an internal node

print intnodes
fileout.write(str(intnodes))