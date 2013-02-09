#!/usr/bin/env python

"""	Rosalind project - Problem: Completing a Tree
Problem
A graph is connected if there is a path connecting any two nodes. A tree
is a connected graph containing no cycles; this definition forces the tree
to have a branching structure organized around a central core of nodes,
just like its living counterpart.
In the creation of a phylogeny, taxa are encoded by the tree's leaves,
or nodes having degree 1. A node of a tree having degree larger than 1
is called an internal node.

Given: A positive integer n (n=1000) and an adjacency list corresponding to
a graph on n nodes that contains no cycles.
Return: The minimum number of edges that can be added to the graph to
produce a tree.

Sample Dataset
10
1 2
2 8
4 10
5 9
6 10
7 9
Sample Output
3

Extra Information
After solving this problem, a standard mathematical exercise for the technically
minded is to verify that every tree having 2 or more nodes must contain at least
two leaves.
"""

__author__ = "Daniel J. Barnes"
__email__ = "ghen2000@gmail.com"
__status__ = "Working"

import re

filename = raw_input("Enter input path: ")

filein = open(filename,'r')
fileout = open('TREE_output.txt','w')

lines = filein.read().splitlines()

nodes = int(lines.pop(0))

edges_given = list(set(lines))

edges_needed = nodes - 1 - len(edges_given)

print edges_needed
fileout.write(str(edges_needed))