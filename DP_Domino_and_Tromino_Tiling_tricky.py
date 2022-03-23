#https://leetcode.com/problems/domino-and-tromino-tiling/
import random
"""
there are three ways to transit the state
f(k) => return number of ways to fully cover the blocks with width k => [][][]
                                                                        [][][]

p(k) => return number of ways to partially cover the blocks with width k =>   [][]      [][][]
                                                                            [][][]  or    [][] , these two are the same
                                                                                                                             
There are three situations in total as mentioned above: 

f(k) = f(k-1) + f(k-2) + 2* p(k-1)

[|][][][][]
[|][][][][]  => f(k-1)

[-][-][][][]
[-][-][][][]  => f(k-2)

[*][*][][][]  
[*][ ][][][]
              => 2* p(k-1)
[*][ ][][][]  
[*][*][][][]

=========================p(k)=================

[][][][]  or  [][][]   => p(k) = p(k-1) + f(k-2)
  [][][]    [][][][]  

"""

from functools import cache
def numTilings(n: int) -> int:
    MOD = 1_000_000_007
    @cache
    def p(n):
        if n == 2:
            return 1
        return (p(n - 1) + f(n - 2)) % MOD

    @cache
    def f(n):
        if n <= 2:
            return n
        return (f(n - 1) + f(n - 2) + 2 * p(n - 1)) % MOD

    return f(n)