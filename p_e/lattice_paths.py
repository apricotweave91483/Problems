"""
say the grid is n x n
something to observe is that we need the same amount of left turns as right turns
and we need n each, so n + n turns total

so for a 2 x 2, we can sort of visualize it as a binary string
where 0101 is left right left right
and 1010 is also a valid solution, right left right left.

So it really comes down to how many binary strings of length n + n have n ones and n zeroes. which can be represented as n + n choose n, or 2n C n.
"""

from math import comb
from sys import argv

n = int(argv[1])
print(comb(2 * n, n)) 

