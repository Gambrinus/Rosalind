#!/usr/bin/env python

""" Rosalind project - Problem: Tree Distance Using Newick Format
    Problem
    Newick format is a way of representing trees even more concisely than using an adjacency list,
    especially when dealing with trees whose internal nodes have not been labeled.
    First, consider the case of a rooted tree T. A collection of leaves v1,v2,...,vn of T are neighbors
    if they are all adjacent to some internal node u. Newick format for T is obtained by iterating
    the following key step: delete all the edges {vi,u} from T and label u with (v1,v2,...,vn)u. This
    process is repeated all the way to the root, at which point a semicolon signals the end of the tree.
    A number of variations of Newick format exist. First, if a node is not labeled in T, then we
    simply leave blank the space occupied by the node. In the key step, we can write (v1,v2,...,vn) in
    place of (v1,v2,...,vn)u if the vi are labeled; if none of the nodes are labeled, we can write (,,...,).
    A second variation of Newick format occurs when T is unrooted, in which case we simply select any
    internal node to serve as the root of T. A particularly peculiar case of Newick format arises when
    we choose a leaf to serve as the root.
    Note that there will be a large number of different ways to represent T in Newick format; see Figure 1.

    Given: A collection of n trees (n<=40) in Newick format, with each tree containing at most 200 nodes;
    each tree Tk is followed by a pair of nodes xk and yk in Tk.
    Return: A collection of n positive integers, for which the kth integer represents the distance between
    xk and yk in Tk.

    Sample Dataset
    (cat)dog;
    dog cat

    (dog,cat);
    dog cat
    Sample Output
    1 2
"""

__author__ = "Daniel J. Barnes"
__email__ = "ghen2000@gmail.com"
__status__ = "Working"

from ete2 import Tree

def treeDist(nwck,nodes):
    tree = Tree(nwck,format=1)
    dist = tree.get_distance(nodes[0],nodes[1])
    return int(dist)

filename = raw_input("Enter input path: ")

filein = open(filename,'r')
fileout = open('NWCK_output.txt','w')

lines = filein.read().splitlines()

pairs = []
i=0
while i < len(lines):
    x = (lines[i],lines[i+1].split())
    pairs.append(x)
    i += 3

dist = []
for x in pairs:
    dist.append(treeDist(x[0],x[1]))

out = ''
for x in dist:
    out += str(x) + ' '

print out.rstrip()
fileout.write(str(out.rstrip()))