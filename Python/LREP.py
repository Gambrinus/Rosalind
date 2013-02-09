#!/usr/bin/env python

""" Rosalind project - Problem: Finding the Longest Multiple Repeat
    Problem
    A repeated substring of a string s of length n is simply a substring that appears in more than one location of s; more
    specifically, a k-fold substring appears in at least k distinct locations.
    The suffix tree of s, denoted T(s), is defined as follows:
    T(s) is a rooted tree having exactly n leaves.
    Every edge of T(s) is labeled with a substring of s*, where s* is the string formed by adding a placeholder symbol $ to
    the end of s.
    Every internal node of T(s) other than the root has at least two children; i.e., it has degree at least 3.
    The substring labels for the edges leading from a node to its children must begin with different symbols.
    By concatenating the substrings along edges, each path from the root to a leaf corresponds to a unique suffix of s*.
    See Figure 1 for an example of a suffix tree.

    Given: A DNA string s (of length at most 40 kbp) with $ appended, a positive integer k, and a list of edges defining the
    suffix tree of s. Each edge is represented by four components:
    the label of its parent node in T(s);
    the label of its child node in T(s);
    the location of the substring t of s* assigned to the edge; and
    the length of t.
    Return: The longest substring of s that occurs at least k times in s. (If multiple solutions exist, you may return any
    single solution.)

    Sample Dataset
    CATACATAC$
    2
    node1 node2 1 1
    node1 node7 2 1
    node1 node14 3 3
    node1 node17 10 1
    node2 node3 2 4
    node2 node6 10 1
    node3 node4 6 5
    node3 node5 10 1
    node7 node8 3 3
    node7 node11 5 1
    node8 node9 6 5
    node8 node10 10 1
    node11 node12 6 5
    node11 node13 10 1
    node14 node15 6 5
    node14 node16 10 1
    Sample Output
    CATAC

    Hint
    How can repeated substrings of s be located in T(s)?
"""

__author__ = "Daniel J. Barnes"
__email__ = "ghen2000@gmail.com"
__status__ = "Working, but slow"

import operator
import time

def lrep(seq,reps,tree,beg):
    parents = [int(x[0]) for x in tree]
    parents = sorted(list(set(parents)))
    
    print 'parents sorted','\t',len(parents),'\t',time.time()-beg,"sec"

    edges = {}
    for x in tree:
        if int(x[1]) in parents:
            edges[int(x[1])] = [int(x[0]),int(x[2]),int(x[3])]
    
    print 'edges done','\t',len(edges),'\t',time.time()-beg,"sec"

    paths = {}
    for key in edges:
        for key2 in edges:
            if key == edges[key2][0]:
                paths[key2] = [key]
    paths = find_path(paths)

    print 'paths done','\t',len(paths),'\t',time.time()-beg,"sec"

    depths = {}
    for key in paths:
        depths[min(paths[key])] = []
    for key in paths:
        sum = edges[key][2]
        for x in paths[key]:
            sum += edges[x][2]
        depths[min(paths[key])].append(sum)
    for key in depths:
        depths[key] = max(depths[key])

    print 'depths done','\t',len(depths),'\t',time.time()-beg,"sec"

    seqs = []
    for key in depths:
        i = edges[key][1]-1
        length = depths[key]
        j = i + length
        count = int(occurrences(seq,seq[i:j]))
        if count == reps:
            seqs.append(seq[i:j])

    print 'kpeats found','\t',len(seqs),'\t',time.time()-beg,"sec"

    return max(seqs,key=len)

def occurrences(string, sub):
    count = start = 0
    while True:
        start = string.find(sub, start) + 1
        if start > 0:
            count+=1
        else:
            return count

def find_path(paths):
    for key1 in paths:
        for key2 in paths:
            if key1 in paths[key2]:
                for x in paths[key1]:
                    paths[key2].append(x)
                break
    return paths

filename = raw_input("Enter input path: ")

filein = open(filename,'r')
fileout = open('LREP_output.txt','w')

lines = filein.read().splitlines()
beg = time.time()

seq = lines.pop(0)
reps = int(lines.pop(0))

print len(seq)-1,'bp sequence'
print reps, 'reps required'

lines = [x.replace('node','') for x in lines]
tree = [x.split() for x in lines]

print 'tree done','\t',len(tree),'\t',time.time()-beg,"sec"

out = lrep(seq,reps,tree,beg)
print out
fileout.write(out)