#!/usr/bin/env python

""" Rosalind project - Problem: Finding a Shared Spliced Motif
    Problem
    A string u is a common subsequence of strings s and t if the symbols of u appear in order
    as a subsequence of both s and t. For example, ACTG is a common subsequence of AACCTTGG and
    ACACTGTGA.
    Analogously to the definition of longest common substring, u is a longest common subsequence
    of s and t if there does not exist a longer common subsequence of the two strings. Continuing
    our above example, ACCTTG is a longest common subsequence of AACCTTGG and ACACTGTGA, as is AACTGG.

    Given: Two DNA strings s and t (each having length at most 1 kbp).
    Return: A longest common subsequence of s and t. (If more than one solution exists, you may return
    any one.)

    Sample Dataset
    AACCTTGG
    ACACTGTGA
    Sample Output
    AACTGG
"""

__author__ = "Daniel J. Barnes" #functions found at http://wordaligned.org/articles/longest-common-subsequence
__email__ = "ghen2000@gmail.com"
__status__ = "Working"

from collections import defaultdict, namedtuple
from itertools import product

def lcs_grid(xs, ys):
    '''Create a grid for longest common subsequence calculations.
    
    Returns a grid where grid[(j, i)] is a pair (n, move) such that
    - n is the length of the LCS of prefixes xs[:i], ys[:j]
    - move is \, ^, <, or e, depending on whether the best move
      to (j, i) was diagonal, downwards, or rightwards, or None.
    
    Example:
       T  A  R  O  T
    A 0< 1\ 1< 1< 1<
    R 0< 1^ 2\ 2< 2<
    T 1\ 1< 2^ 2< 3\
    '''
    Cell = namedtuple('Cell', 'length move')
    grid = defaultdict(lambda: Cell(0, 'e'))
    sqs = product(enumerate(ys), enumerate(xs))
    for (j, y), (i, x) in sqs:
        if x == y:
            cell = Cell(grid[(j-1, i-1)].length + 1, '\\')
        else:
            left = grid[(j, i-1)].length
            over = grid[(j-1, i)].length
            if left < over:
                cell = Cell(over, '^')
            else:
                cell = Cell(left, '<')
        grid[(j, i)] = cell
    print grid
    return grid

def lcs(xs, ys):
    '''Return a longest common subsequence of xs, ys.'''
    # Create the LCS grid, then walk back from the bottom right corner
    grid = lcs_grid(xs, ys)
    i, j = len(xs) - 1, len(ys) - 1
    lcs = list()
    for move in iter(lambda: grid[(j, i)].move, 'e'):
        if move == '\\':
            lcs.append(xs[i])
            i -= 1
            j -= 1
        elif move == '^':
            j -= 1
        elif move == '<':
            i -= 1
    lcs.reverse()
    ret = ''.join(lcs)
    return ret

filename = raw_input("Enter input path: ")

filein = open(filename,'r')
fileout = open('LCSQ_output.txt','w')

lines = filein.read().splitlines()

out =  lcs(lines[0],lines[1])
print out
fileout.write(out)